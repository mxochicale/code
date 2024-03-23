#include <iostream>
#include <cstdlib>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include "ThreadCam.h"
#define VID_HEIGHT 480
#define VID_WIDTH 640

int main()
{
    /// In this example, 4 cameras are used. This is not necessary. 
    /// You can control any number, one, two or, for example, six. It does not matter.    
    /// use a gray frame to indicate an empty field (lost connection with camera, for instance)
    ///  be sure every frame has the same size!
    ///  hconcat and vconcat expect equal width and height
    ///  otherwise OpenCV throws exceptions

    double Elapse;
    std::chrono::steady_clock::time_point Tbefore, Tafter;

    cv::Mat Frame1, Frame2, FrameCon1;
    cv::Mat Frame3, Frame4, FrameCon2, FrameTotal;
    cv::Mat FrameE(VID_HEIGHT, VID_WIDTH, CV_8UC3, cv::Scalar(128,128,128));  //a gray frame

    ThreadCam *Grb1, *Grb2, *Grb3, *Grb4;

    Grb1 = new ThreadCam();
    Grb2 = new ThreadCam();
    Grb3 = new ThreadCam();
    Grb4 = new ThreadCam();

    Grb1->Init("/dev/video0"); //Camera 1
    Grb2->Init("/dev/video2"); //Camera 2
    Grb3->Init("/dev/video4"); //Camera 3
    Grb4->Init("/dev/video6"); //Camera 3

    while(true)
    {
        //get the new frames
        std::cout << "---------------";

        Grb1->GetFrame(Frame1);

        //cv::Size s = Frame1.size();
        //std::cout << "---------------";
        //std::cout << s.height << s.width<<std::endl;
        
        Tbefore = std::chrono::steady_clock::now();
        if(!Frame1.empty()){
            ///place here your time consuming algorithms
            GaussianBlur(Frame1, Frame1, cv::Size(51, 51), 0);
        }
        else FrameE.copyTo(Frame1);

        Tafter   = std::chrono::steady_clock::now();
        Elapse = std::chrono::duration_cast<std::chrono::milliseconds> (Tafter - Tbefore).count(); 
        std::cout << Elapse << " milliseconds" <<std::endl;

        //get the new frame
        Grb2->GetFrame(Frame2);
        if(!Frame2.empty()){
            ///place here your time consuming algorithms
            GaussianBlur(Frame1, Frame1, cv::Size(1, 1), 0);
        }
        else FrameE.copyTo(Frame2);

        //get the new frame
        Grb3->GetFrame(Frame3);
        if(!Frame3.empty()){
            ///place here your time consuming algorithms
            GaussianBlur(Frame1, Frame1, cv::Size(1, 1), 0);
        }
        else FrameE.copyTo(Frame3);

        // //get the new frame
        Grb4->GetFrame(Frame4);
        if(!Frame4.empty()){
            ///place here your time consuming algorithms
            GaussianBlur(Frame1, Frame1, cv::Size(1, 1), 0);
        }
        else FrameE.copyTo(Frame4);

        //concat the four frames
        cv::hconcat(Frame1,Frame2,FrameCon1);
        cv::hconcat(Frame3,Frame4,FrameCon2);
        cv::vconcat(FrameCon1,FrameCon2,FrameTotal);

        //show the result
        //cv::imshow("Camera",Frame1);
        cv::imshow("Concatenated Cameras",FrameTotal);
        char esc = cv::waitKey(5);
        if(esc == 27) break;
    }
    
    /// Gracefully, terminate the threads.
    Grb1->Quit();
    Grb2->Quit();
    Grb3->Quit();
    Grb4->Quit();

    delete Grb1;
    delete Grb2;
    delete Grb3;
    delete Grb4;

    return 0;
}
