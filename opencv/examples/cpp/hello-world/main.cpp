#include <iostream>
#include <opencv2/opencv.hpp>

int main() {
    std::cout << "Hello, OpenCV\n";

    cv::Mat image = cv::imread("lena.png", cv::IMREAD_GRAYSCALE);
    if (image.empty()) {
        std::cerr << "Image not found\n";
        return 1;
    }

    const std::string window_name{"lena"};
    cv::namedWindow(window_name);
    cv::imshow(window_name, image);
    cv::waitKey(0);
    return 0;

}
