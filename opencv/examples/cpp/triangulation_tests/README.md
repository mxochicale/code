# Video Recording


## Logs
```
$HOME/repositories/mxochicale/code/opencv/examples/cpp/triangulation_tests/build

./triangulation_tests 
Hello, OpenCV
modelPointsTransposed: 
[0, 39, 0, 39;
 0, 0, 27, 27;
 0, 0, 0, 0]
rotatedModelPoints: 
[0, 37.685152011, -2.8431540459, 34.8419979651;
 0, -0.199133488983, 24.4221533676, 24.223019878617;
 0, -10.0394055528, -11.1568319838, -21.1962375366]
modelPointsRotatedAndTransposed: 
[0, 0, 0;
 37.685152011, -0.199133488983, -10.0394055528;
 -2.8431540459, 24.4221533676, -11.1568319838;
 34.8419979651, 24.223019878617, -21.1962375366]
transformedModelPoints: 
[9.847672184, -22.45992103, 127.7836183;
 47.532824195, -22.659054518983, 117.7442127472;
 7.0045181381, 1.9622323376, 116.6267863162;
 44.6896701491, 1.763098848616998, 106.5873807634]
TriangulatePointsUsingHartley> pointsIn2D: 
[1100.16, 262.974, 1184.84, 241.915;
 1757.74, 228.971, 1843.52, 204.083;
 1065.44, 651.593, 1142.75, 632.817;
 1788.22, 650.41, 1867.78, 632.59]
TriangulatePointsUsingHartley> leftIntrinsic: 
[2012.186314, 0, 944.7173708;
 0, 2017.966019, 617.1093984;
 0, 0, 1]
TriangulatePointsUsingHartley> rightIntrinsic: 
[2037.233928, 0, 1051.112809;
 0, 2052.018948, 548.0675962;
 0, 0, 1]
TriangulatePointsUsingHartley> leftToRightRotation: 
[0.999678, 0.000151, 0.025398;
 -0.00072, 0.999749, 0.022394;
 -0.025388, -0.022405, 0.999426]
TriangulatePointsUsingHartley> leftToRightTranslation: 
[-4.631472;
 0.268695;
 1.300256]
pointsFromHartley: 
[9.882561793478274, -22.44358672047434, 127.9216596991245;
 48.46473971483012, -23.09607651651325, 119.9524462287327;
 6.946803109459471, 1.973326991586282, 115.7921729428552;
 44.77458535398358, 1.768363607856355, 106.8097293986459]
rmsHartley: 
1.29547

``` 


## Reference 
https://github.com/Myzhar/simple-opencv-kalman-tracker
https://www.myzhar.com/blog/tutorials/tutorial-opencv-ball-tracker-using-kalman-filter/
https://www.youtube.com/watch?v=sG-h5ONsj9s&feature=emb_title



