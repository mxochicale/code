#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <stdio.h>
using namespace cv;
using namespace std;

#define VID_WIDTH 640
#define VID_HEIGHT 480
#define VIDEO_IN "/dev/video0"

int main(int, char**)
{
    Mat src;
    // use default camera as video source
    VideoCapture cap(VIDEO_IN);
    // check if we succeeded
    if (!cap.isOpened()) {
        cerr << "ERROR! Unable to open camera\n";
        return -1;
    }

    // get one frame from camera to know frame size and type
    cap >> src;
    // check if we succeeded
    if (src.empty()) {
        cerr << "ERROR! blank frame grabbed\n";
        return -1;
    }

    cout << "Original video size " << src.size() << endl;
    Size targetSize(VID_WIDTH, VID_HEIGHT);
    cap.set(cv::CAP_PROP_FRAME_WIDTH, VID_WIDTH);
    cap.set(cv::CAP_PROP_FRAME_HEIGHT, VID_HEIGHT);
    cout << "Target video size " << targetSize << endl;

    cout << "Source type " << src.type() << endl;
    bool isColor = (src.type() == CV_8UC3);

    //--- INITIALIZE VIDEOWRITER
    VideoWriter writer;
    int codec = VideoWriter::fourcc('M', 'J', 'P', 'G');  // select desired codec (must be available at runtime)
    double fps = 30.0;                          // framerate of the created video stream
    string filename = "./live.avi";             // name of the output video file
    //writer.open(filename, codec, fps, src.size(), isColor);
    writer.open(filename, codec, fps, targetSize, isColor);
    // check if we succeeded
    if (!writer.isOpened()) {
        cerr << "Could not open the output video file for write\n";
        return -1;
    }
    //--- GRAB AND WRITE LOOP
    cout << "Writing videofile: " << filename << endl
         << "Press any key to terminate" << endl;
    for (;;)
    {
        // check if we succeeded
        if (!cap.read(src)) {
            cerr << "ERROR! blank frame grabbed\n";
            break;
        }
        // encode the frame into the videofile stream
        writer.write(src);
        // show live and wait for a key with timeout long enough to show images
        imshow("Live Video Stream", src);
        if (waitKey(5) >= 0)
            break;
    }
    // the videofile will be closed and released automatically in VideoWriter destructor
    return 0;
}
