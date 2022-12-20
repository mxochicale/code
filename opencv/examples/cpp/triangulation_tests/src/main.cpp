/*=============================================================================
    TriangulatePointsUsingHartley

    References:
    SKSURGERYCVCPP: scikit-surgeryopencvcpp provides opencv functions in C++
    https://github.com/SciKit-Surgery/scikit-surgeryopencvcpp/blob/master/Testing/sksTriangulateTest.cpp
    https://github.com/SciKit-Surgery/scikit-surgeryopencvcpp/blob/master/Code/Lib/sksMaths.cpp

=============================================================================*/

#include <opencv2/opencv.hpp>

namespace sks
{
    //-----------------------------------------------------------------------------
    cv::Mat_<double> InternalTriangulatePointUsingSVD(
        const cv::Matx34d& P1,
        const cv::Matx34d& P2,
        const cv::Point3d& u1,
        const cv::Point3d& u2,
        const double& w1,
        const double& w2
        )
    {
      // Build matrix A for homogeneous equation system Ax = 0
      // Assume X = (x,y,z,1), for Linear-LS method
      // Which turns it into a AX = B system, where A is 4x3, X is 3x1 and B is 4x1
      cv::Matx43d A((u1.x*P1(2,0)-P1(0,0))/w1, (u1.x*P1(2,1)-P1(0,1))/w1, (u1.x*P1(2,2)-P1(0,2))/w1,
                    (u1.y*P1(2,0)-P1(1,0))/w1, (u1.y*P1(2,1)-P1(1,1))/w1, (u1.y*P1(2,2)-P1(1,2))/w1,
                    (u2.x*P2(2,0)-P2(0,0))/w2, (u2.x*P2(2,1)-P2(0,1))/w2, (u2.x*P2(2,2)-P2(0,2))/w2,
                    (u2.y*P2(2,0)-P2(1,0))/w2, (u2.y*P2(2,1)-P2(1,1))/w2, (u2.y*P2(2,2)-P2(1,2))/w2
                   );


      cv::Matx41d B(-(u1.x*P1(2,3) -P1(0,3))/w1,
                    -(u1.y*P1(2,3) -P1(1,3))/w1,
                    -(u2.x*P2(2,3) -P2(0,3))/w2,
                    -(u2.y*P2(2,3) -P2(1,3))/w2
                   );

      cv::Mat_<double> X;
      cv::solve(A,B,X,cv::DECOMP_SVD);

      return X;
    }

    //-----------------------------------------------------------------------------
    cv::Point3d InternalIterativeTriangulatePointUsingSVD(
        const cv::Matx34d& P1,
        const cv::Matx34d& P2,
        const cv::Point3d& u1,
        const cv::Point3d& u2
        )
    {
      double epsilon = 0.00000000001;
      double w1 = 1, w2 = 1;
      cv::Mat_<double> X(4,1);

      for (int i=0; i<10; i++) // Hartley suggests 10 iterations at most
      {
        cv::Mat_<double> X_ = InternalTriangulatePointUsingSVD(P1,P2,u1,u2,w1,w2);
        X(0) = X_(0);
        X(1) = X_(1);
        X(2) = X_(2);
        X(3) = 1.0;

        double p2x1 = cv::Mat_<double>(cv::Mat_<double>(P1).row(2)*X)(0);
        double p2x2 = cv::Mat_<double>(cv::Mat_<double>(P2).row(2)*X)(0);

        if(fabs(w1 - p2x1) <= epsilon && fabs(w2 - p2x2) <= epsilon)
          break;

        w1 = p2x1;
        w2 = p2x2;
      }

      cv::Point3d result;
      result.x = X(0);
      result.y = X(1);
      result.z = X(2);

      return result;
    }


    //-----------------------------------------------------------------------------
    cv::Mat TriangulatePointsUsingHartley(
      const cv::Mat& inputUndistortedPoints,
      const cv::Mat& leftCameraIntrinsicParams,
      const cv::Mat& rightCameraIntrinsicParams,
      const cv::Mat& leftToRightRotationMatrix,
      const cv::Mat& leftToRightTranslationVector
      )
    {

      int numberOfPoints = inputUndistortedPoints.rows;

      cv::Mat outputPoints = cv::Mat(numberOfPoints, 3, CV_64FC1);

      cv::Mat K1    = cv::Mat(3, 3, CV_64FC1);
      cv::Mat K2    = cv::Mat(3, 3, CV_64FC1);
      cv::Mat K1Inv = cv::Mat(3, 3, CV_64FC1);
      cv::Mat K2Inv = cv::Mat(3, 3, CV_64FC1);
      cv::Mat R1    = cv::Mat::eye(3, 3, CV_64FC1);
      cv::Mat R2    = leftToRightRotationMatrix;
      cv::Mat E1    = cv::Mat::eye(4, 4, CV_64FC1);
      cv::Mat E1Inv = cv::Mat::eye(4, 4, CV_64FC1);
      cv::Mat E2    = cv::Mat::eye(4, 4, CV_64FC1);
      cv::Mat L2R   = cv::Mat(4, 4, CV_64FC1);
      cv::Matx34d P1d, P2d;

      // Construct:
      // E1 = Object to Left Camera = Left Camera Extrinsics.
      // E2 = Object to Right Camera = Right Camera Extrinsics.
      // K1 = Copy of Left Camera intrinsics.
      // K2 = Copy of Right Camera intrinsics.
      // Copy data into cv::Mat data types.
      // Camera calibration routines are 32 bit, as some drawing functions require 32 bit data.
      // These triangulation routines need 64 bit data.
      for (int r = 0; r < 3; r++)
      {
        for (int c = 0; c < 3; c++)
        {
          K1.at<double>(r, c) = leftCameraIntrinsicParams.at<double>(r, c);
          K2.at<double>(r, c) = rightCameraIntrinsicParams.at<double>(r, c);
          E2.at<double>(r, c) = R2.at<double>(r, c);
        }
        E2.at<double>(r, 3) = leftToRightTranslationVector.at<double>(r, 0);
      }

      // We invert the intrinsic params, so we can convert from pixels to normalised image coordinates.
      K1Inv = K1.inv();
      K2Inv = K2.inv();

      // We want output coordinates relative to left camera.
      E1Inv = E1.inv();
      L2R = E2 * E1Inv;

      // Reading Prince 2012 Computer Vision, the projection matrix, is just the extrinsic parameters,
      // as our coordinates will be in a normalised camera space. P1 should be identity, so that
      // reconstructed coordinates are in Left Camera Space, to P2 should reflect a right to left transform.
      P1d(0,0) = 1; P1d(0,1) = 0; P1d(0,2) = 0; P1d(0,3) = 0;
      P1d(1,0) = 0; P1d(1,1) = 1; P1d(1,2) = 0; P1d(1,3) = 0;
      P1d(2,0) = 0; P1d(2,1) = 0; P1d(2,2) = 1; P1d(2,3) = 0;

      for (int i = 0; i < 3; i++)
      {
        for (int j = 0; j < 4; j++)
        {
          P2d(i,j) = L2R.at<double>(i,j);
        }
      }

      #pragma omp parallel
      {
        cv::Mat u1    = cv::Mat(3, 1, CV_64FC1);
        cv::Mat u2    = cv::Mat(3, 1, CV_64FC1);
        cv::Mat u1t   = cv::Mat(3, 1, CV_64FC1);
        cv::Mat u2t   = cv::Mat(3, 1, CV_64FC1);

        cv::Point3d u1p, u2p;            // Normalised image coordinates. (i.e. relative to a principal point of zero, and in millimetres not pixels).
        cv::Point3d reconstructedPoint;  // the output 3D point, in reference frame of left camera.

        #pragma omp for
        for (int i = 0; i < numberOfPoints; i++)
        {
          u1.at<double>(0,0) = inputUndistortedPoints.at<double>(i, 0);
          u1.at<double>(1,0) = inputUndistortedPoints.at<double>(i, 1);
          u1.at<double>(2,0) = 1;

          u2.at<double>(0,0) = inputUndistortedPoints.at<double>(i, 2);
          u2.at<double>(1,0) = inputUndistortedPoints.at<double>(i, 3);
          u2.at<double>(2,0) = 1;

          // Converting to normalised image points
          u1t = K1Inv * u1;
          u2t = K2Inv * u2;

          u1p.x = u1t.at<double>(0,0);
          u1p.y = u1t.at<double>(1,0);
          u1p.z = u1t.at<double>(2,0);

          u2p.x = u2t.at<double>(0,0);
          u2p.y = u2t.at<double>(1,0);
          u2p.z = u2t.at<double>(2,0);

          reconstructedPoint = InternalIterativeTriangulatePointUsingSVD(P1d, P2d, u1p, u2p);

          outputPoints.at<double>(i, 0) = reconstructedPoint.x;
          outputPoints.at<double>(i, 1) = reconstructedPoint.y;
          outputPoints.at<double>(i, 2) = reconstructedPoint.z;
        } // end for
      } // end parallel block
      return outputPoints;
    }


    //-----------------------------------------------------------------------------
    double ComputeRMSBetweenCorrespondingPoints(const cv::Mat& a, const cv::Mat& b)
    {
      double rms = 0;
      double diff = 0;
      double squaredDiff = 0;

      if (a.rows != b.rows)
      {
        std::cout << "a has " << a.rows << " rows, but b has " << b.rows;
      }

      if (a.cols != 3)
      {
        std::cout << "a does not have 3 columns.";
      }

      if (b.cols != 3)
      {
        std::cout << "b does not have 3 columns.";
      }

      for (unsigned int r = 0; r < a.rows; r++)
      {
        for (unsigned int c = 0; c < a.cols; c++)
        {
          diff = (b.at<double>(r, c) - a.at<double>(r, c));
          squaredDiff = diff * diff;
          rms += squaredDiff;
        }
      }
      rms /= static_cast<double>(a.rows);
      rms = std::sqrt(rms);
      return rms;
    }

}

int main(int, char**)
{

    std::cout << "Hello, OpenCV\n";

    cv::Mat leftIntrinsic = cv::Mat::eye(3, 3, CV_64FC1);
    leftIntrinsic.at<double>(0, 0) = 2012.186314;
    leftIntrinsic.at<double>(1, 1) = 2017.966019;
    leftIntrinsic.at<double>(0, 2) = 944.7173708;
    leftIntrinsic.at<double>(1, 2) = 617.1093984;

    cv::Mat rightIntrinsic = cv::Mat::eye(3, 3, CV_64FC1);
    rightIntrinsic.at<double>(0, 0) = 2037.233928;
    rightIntrinsic.at<double>(1, 1) = 2052.018948;
    rightIntrinsic.at<double>(0, 2) = 1051.112809;
    rightIntrinsic.at<double>(1, 2) = 548.0675962;

    cv::Mat leftRotation = cv::Mat::eye(3, 3, CV_64FC1);
    leftRotation.at<double>(0, 0) = 0.966285949;
    leftRotation.at<double>(0, 1) = -0.1053020017;
    leftRotation.at<double>(0, 2) = 0.2349530874;
    leftRotation.at<double>(1, 0) = -0.005105986897;
    leftRotation.at<double>(1, 1) = 0.9045241988;
    leftRotation.at<double>(1, 2) = 0.4263917244;
    leftRotation.at<double>(2, 0) = -0.2574206552;
    leftRotation.at<double>(2, 1) = -0.4132159994;
    leftRotation.at<double>(2, 2) = 0.8734913532;

    cv::Mat leftTranslation = cv::Mat::eye(3, 1, CV_64FC1);
    leftTranslation.at<double>(0, 0) = 9.847672184;
    leftTranslation.at<double>(1, 0) = -22.45992103;
    leftTranslation.at<double>(2, 0) = 127.7836183;

    cv::Mat rightRotation = cv::Mat::eye(3, 3, CV_64FC1);
    rightRotation.at<double>(0, 0) = 0.958512625;
    rightRotation.at<double>(0, 1) = -0.1175427792;
    rightRotation.at<double>(0, 2) = 0.2596868167;
    rightRotation.at<double>(1, 0) = -0.0115032253;
    rightRotation.at<double>(1, 1) = 0.8943292319;
    rightRotation.at<double>(1, 2) = 0.4472615574;
    rightRotation.at<double>(2, 0) = -0.2848178778;
    rightRotation.at<double>(2, 1) = -0.4316930854;
    rightRotation.at<double>(2, 2) = 0.8558737386;

    cv::Mat rightTranslation = cv::Mat::eye(3, 1, CV_64FC1);
    rightTranslation.at<double>(0, 0) = 8.461514886;
    rightTranslation.at<double>(1, 0) = -19.3242747;
    rightTranslation.at<double>(2, 0) = 129.0937601;

    cv::Mat pointsIn2D = cv::Mat::zeros(4, 4, CV_64FC1);
    pointsIn2D.at<double>(0, 0) = 1100.16;
    pointsIn2D.at<double>(0, 1) = 262.974;
    pointsIn2D.at<double>(0, 2) = 1184.84;
    pointsIn2D.at<double>(0, 3) = 241.915;
    pointsIn2D.at<double>(1, 0) = 1757.74;
    pointsIn2D.at<double>(1, 1) = 228.971;
    pointsIn2D.at<double>(1, 2) = 1843.52;
    pointsIn2D.at<double>(1, 3) = 204.083;
    pointsIn2D.at<double>(2, 0) = 1065.44;
    pointsIn2D.at<double>(2, 1) = 651.593;
    pointsIn2D.at<double>(2, 2) = 1142.75;
    pointsIn2D.at<double>(2, 3) = 632.817;
    pointsIn2D.at<double>(3, 0) = 1788.22;
    pointsIn2D.at<double>(3, 1) = 650.41;
    pointsIn2D.at<double>(3, 2) = 1867.78;
    pointsIn2D.at<double>(3, 3) = 632.59;

    cv::Mat leftToRightRotation = cv::Mat::eye(3, 3, CV_64FC1);
    leftToRightRotation.at<double>(0, 0) = 0.999678;
    leftToRightRotation.at<double>(0, 1) = 0.000151;
    leftToRightRotation.at<double>(0, 2) = 0.025398;
    leftToRightRotation.at<double>(1, 0) = -0.000720;
    leftToRightRotation.at<double>(1, 1) = 0.999749;
    leftToRightRotation.at<double>(1, 2) = 0.022394;
    leftToRightRotation.at<double>(2, 0) = -0.025388;
    leftToRightRotation.at<double>(2, 1) = -0.022405;
    leftToRightRotation.at<double>(2, 2) = 0.999426;

    cv::Mat leftToRightTranslation = cv::Mat::eye(3, 1, CV_64FC1);
    leftToRightTranslation.at<double>(0, 0) = -4.631472;
    leftToRightTranslation.at<double>(1, 0) = 0.268695;
    leftToRightTranslation.at<double>(2, 0) = 1.300256;

    cv::Mat modelPoints = cv::Mat::eye(4, 3, CV_64FC1);
    modelPoints.at<double>(0, 0) = 0;
    modelPoints.at<double>(0, 1) = 0;
    modelPoints.at<double>(0, 2) = 0;
    modelPoints.at<double>(1, 0) = 39;
    modelPoints.at<double>(1, 1) = 0;
    modelPoints.at<double>(1, 2) = 0;
    modelPoints.at<double>(2, 0) = 0;
    modelPoints.at<double>(2, 1) = 27;
    modelPoints.at<double>(2, 2) = 0;
    modelPoints.at<double>(3, 0) = 39;
    modelPoints.at<double>(3, 1) = 27;
    modelPoints.at<double>(3, 2) = 0;


    cv::Mat modelPointsTransposed;
    cv::transpose(modelPoints, modelPointsTransposed);
    std::cout << "modelPointsTransposed: \n" << modelPointsTransposed << std::endl;

    cv::Mat rotatedModelPoints = cv::Mat(modelPointsTransposed.rows, modelPointsTransposed.cols, CV_64FC1);
    cv::gemm(leftRotation, modelPointsTransposed, 1, cv::Mat(), 0, rotatedModelPoints);
    std::cout << "rotatedModelPoints: \n" << rotatedModelPoints << std::endl;

    cv::Mat modelPointsRotatedAndTransposed;
    cv::transpose(rotatedModelPoints, modelPointsRotatedAndTransposed);
    std::cout << "modelPointsRotatedAndTransposed: \n" << modelPointsRotatedAndTransposed << std::endl;

    cv::Mat transformedModelPoints = cv::Mat(modelPointsRotatedAndTransposed.rows, modelPointsRotatedAndTransposed.cols, CV_64FC1);
    for (int r = 0; r < modelPointsRotatedAndTransposed.rows; r++)
        {
            for (int c = 0; c < modelPointsRotatedAndTransposed.cols; c++)
                {
                transformedModelPoints.at<double>(r, c) = modelPointsRotatedAndTransposed.at<double>(r, c) + leftTranslation.at<double>(c, 0);
                }
        }

    std::cout << "transformedModelPoints: \n" << transformedModelPoints << std::endl;

    std::cout << "TriangulatePointsUsingHartley> pointsIn2D: \n" << pointsIn2D << std::endl;
    std::cout << "TriangulatePointsUsingHartley> leftIntrinsic: \n" << leftIntrinsic << std::endl;
    std::cout << "TriangulatePointsUsingHartley> rightIntrinsic: \n" << rightIntrinsic << std::endl;
    std::cout << "TriangulatePointsUsingHartley> leftToRightRotation: \n" << leftToRightRotation << std::endl;
    std::cout << "TriangulatePointsUsingHartley> leftToRightTranslation: \n" << leftToRightTranslation << std::endl;

    cv::Mat pointsFromHartley = sks::TriangulatePointsUsingHartley(pointsIn2D,
                                                                 leftIntrinsic,
                                                                 rightIntrinsic,
                                                                 leftToRightRotation,
                                                                 leftToRightTranslation
                                                                );
    std::cout << "pointsFromHartley: \n" << pointsFromHartley << std::endl;

    double rmsHartley = sks::ComputeRMSBetweenCorrespondingPoints(transformedModelPoints, pointsFromHartley);
    std::cout << "rmsHartley: \n" << rmsHartley << std::endl;

    return 0;
}
