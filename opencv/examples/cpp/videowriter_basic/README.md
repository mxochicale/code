# Video Recording

## video features
```
v4l2-ctl --list-formats-ext
ioctl: VIDIOC_ENUM_FMT
	Type: Video Capture

	[0]: 'MJPG' (Motion-JPEG, compressed)
		Size: Discrete 1280x720
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 960x540
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 848x480
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 640x480
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 640x360
			Interval: Discrete 0.033s (30.000 fps)
	[1]: 'YUYV' (YUYV 4:2:2)
		Size: Discrete 640x480
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 640x360
			Interval: Discrete 0.033s (30.000 fps)
```

v4l2-ctl --all
```
...
Video input : 0 (Input 1: ok)
Format Video Capture:
	Width/Height      : 640/480
	Pixel Format      : 'YUYV' (YUYV 4:2:2)
	Field             : None
	Bytes per Line    : 1280
	Size Image        : 614400
	Colorspace        : sRGB
	Transfer Function : Rec. 709

```


## clean, build and execute 
```
bash build.bash
```


## execute 
```
./build/videowriter
vlc live.avi
```

## clean 
```  
rm -rf build live.avi
```


## Reference 
https://docs.opencv.org/4.9.0/df/d94/samples_2cpp_2videowriter_basic_8cpp-example.html#a5  
https://github.com/Myzhar/simple-opencv-kalman-tracker
https://www.myzhar.com/blog/tutorials/tutorial-opencv-ball-tracker-using-kalman-filter/
https://www.youtube.com/watch?v=sG-h5ONsj9s&feature=emb_title



