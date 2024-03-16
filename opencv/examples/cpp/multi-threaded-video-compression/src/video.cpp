#include <iostream>
#include <opencv2/opencv.hpp>
#include <thread>
#include <mutex>
#include <iomanip>

using namespace std;
using namespace cv;

// Function to compress the frame
void compressFrame(Mat& frame, Mat& compressed_frame, mutex& mtx, int compression_level)
{
    vector<uchar> buf;
    vector<int> params;
    params.push_back(IMWRITE_JPEG_QUALITY);
    params.push_back(compression_level);

    while (true)
    {
        // Compress the frame
        Mat local_frame;
        mtx.lock();
        frame.copyTo(local_frame);
        mtx.unlock();

        imencode(".jpg", local_frame, buf, params);
        mtx.lock();
        compressed_frame = imdecode(buf, IMREAD_COLOR);
        mtx.unlock();
    }
}

int main(int argc, char * argv[])
{
    // "Enter the compression level (0-100): ";
    int compression_level = strtol(argv[1], NULL, 10);
    std::cout << "Compresion level " << compression_level << std::endl;

    // Open the webcam for video capture
    VideoCapture cap(0);
    if (!cap.isOpened())
    {
        cout << "Failed to open the webcam." << endl;
        return -1;
    }

    // Create a window for the original video
    namedWindow("Original Video", WINDOW_NORMAL);

    // Create a window for the compressed output video
    namedWindow("Compressed Output", WINDOW_NORMAL);

    // Mutex for thread synchronization
    mutex mtx;

    // Read the first frame to get the frame size
    Mat frame;
    cap.read(frame);

    // Create a Mat to hold the compressed frame
    Mat compressed_frame(frame.size(), CV_8UC3);

    // Start the compression thread
    thread compression_thread(compressFrame, ref(frame), ref(compressed_frame), ref(mtx), compression_level);

    // Process frames from the webcam
    while (true)
    {
        cap.read(frame);

        // Display the original video
        imshow("Original Video", frame);

        // Display the compressed output video
        Mat local_compressed_frame;
        mtx.lock();
        compressed_frame.copyTo(local_compressed_frame);
        mtx.unlock();

        // Calculate the compression percentage
        vector<uchar> compressed_buf;
        imencode(".jpg", local_compressed_frame, compressed_buf);
        size_t original_size = frame.total() * frame.elemSize();
        size_t compressed_size = compressed_buf.size();
        double compression_percentage = static_cast<double>(compressed_size) / original_size * 1000.0;


        // Convert the compression percentage to a string
        stringstream ss;
        ss << fixed << setprecision(2) << "Compression: " << compression_percentage << "%";
        string compression_text = ss.str();

        // Display the compressed output video with compression percentage
        putText(local_compressed_frame, compression_text, Point(10, 30), FONT_HERSHEY_SIMPLEX, 1, Scalar(255, 255, 255), 2, LINE_AA);
        imshow("Compressed Output", local_compressed_frame);

        // Check for the 'q' key to exit the loop
        if (waitKey(1) == 'q')
            break;
    }

    // Release the VideoCapture object
    cap.release();

    // Join the compression thread
    compression_thread.join();

    // Destroy any OpenCV windows
    destroyAllWindows();

    return 0;
}
