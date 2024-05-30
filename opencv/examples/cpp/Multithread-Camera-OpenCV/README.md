# Multithread-Camera-OpenCV

## Check video devices
```
v4l2-ctl --list-devices
	/dev/video0
	/dev/video1
#v4l2-ctl --list-formats-ext --device /dev/video0
#v4l2-ctl --list-ctrls --device /dev/video0
```

## Build and run app
```
bash conf_build 
```

## Gstreamer
```
##TEST in the terminal
gst-launch-1.0 v4l2src device=/dev/video0 ! videoconvert ! videoscale ! video/x-raw, width=640, height=480, framerate=30/1 ! autovideosink
##TEST in cpp
Grb1->Init("v4l2src device=/dev/video0 ! videoconvert ! videoscale ! video/x-raw, width=640, height=480, framerate=30/1 ! autovideosink", cv::CAP_GSTREAMER);
#ERROR candidate expects 1 argument, 2 provided
```

## Warnings 
```
#WITH DEFTAUL OPECV BUILD
(main:98841): GStreamer-CRITICAL **: 09:04:33.886: gst_element_make_from_uri: assertion 'gst_uri_is_valid (uri)' failed
[ WARN:9@2.132] global cap_gstreamer.cpp:1436 open OpenCV | GStreamer warning: Error opening bin: no source element for URI "/dev/video4"
[ WARN:9@2.133] global cap_gstreamer.cpp:1173 isPipelinePlaying OpenCV | GStreamer warning: GStreamer: pipeline have not been created
 
#WITH cmake -D WITH_FFMPEG=ON -D OPENCV_GENERATE_PKGCONFIG=ON -D WITH_GSTREAMER=ON -D BUILD_EXAMPLES=OFF
(main:122125): GStreamer-CRITICAL **: 11:34:40.556: gst_element_make_from_uri: assertion 'gst_uri_is_valid (uri)' failed
[ WARN:10@4.283] global cap_gstreamer.cpp:1436 open OpenCV | GStreamer warning: Error opening bin: no source element for URI "/dev/video2"
[ WARN:10@4.283] global cap_gstreamer.cpp:1173 isPipelinePlaying OpenCV | GStreamer warning: GStreamer: pipeline have not been created
```

## Reference 
* https://github.com/Qengineering/Multithread-Camera-OpenCV
* To put together CMakelists.txt: https://github.com/surfertas/fun_with_cpp/tree/master/project_euler/PrimeUtil
* https://decovar.dev/blog/2021/03/08/cmake-cpp-library/#the-library
* https://stackoverflow.com/questions/10508843/what-is-dev-null-21 

