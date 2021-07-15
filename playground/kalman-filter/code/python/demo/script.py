## Usage
# conda activate kalman-ve
# python script.py

## Reference
# https://github.com/cyber-tuna/kalman_demo/blob/master/kalman_demo.py


import cv2 as cv
import numpy as np

cursor_x = 250
cursor_y = 250
start = False

img_height = 1500
img_width = 1500

img = np.zeros((img_height, img_width, 3), np.uint8)

kalman = cv.KalmanFilter(4, 2, 0, cv.CV_32F)


# <KalmanFilter object>	=	cv.KalmanFilter(	dynamParams, measureParams[, controlParams[, type]]	)
# Parameters
#    dynamParams	Dimensionality of the state.
#    measureParams	Dimensionality of the measurement.
#    controlParams	Dimensionality of the control vector.
#    type	Type of the created matrices that should be CV_32F or CV_64F. 

def update_cursor_pos(event, x, y, flags, param):
    global cursor_x, cursor_y, start, img
    if event == cv.EVENT_LBUTTONDOWN:
        start = True
        cursor_x = x
        cursor_y = y
        kalman.statePost = 1. * np.array([[cursor_x], [cursor_y], [0.], [0.]])
    # statePost means corrected state (x(k)): x(k)=x'(k)+K(k)*(z(k)-H*x'(k))
    # Example:
    # [[577.]
    # [320.]
    # [  0.]
    # [  0.]]
    elif event == cv.EVENT_LBUTTONDBLCLK:
        img = np.zeros((img_height, img_width, 3), np.uint8)
    elif event == cv.EVENT_MOUSEMOVE:
        cursor_x = x
        cursor_y = y


def main():
    cv.namedWindow("KalmanDemo")
    cv.setMouseCallback('KalmanDemo', update_cursor_pos)

    kalman.transitionMatrix = np.array([[1., 0., .7, 0.], [0., 1., 0., .7], [0., 0., 1., 0.], [0., 0., 0., 1.]])
    ##state transition matrix (A)
    # [[1.  0.  0.7 0. ]
    # [0.  1.  0.  0.7]
    # [0.  0.  1.  0. ]
    # [0.  0.  0.  1. ]]

    kalman.measurementMatrix = np.array([[1., 0., 0., 0.], [0., 1., 0., 0.]])
    ##measurement matrix (H)
    # [[1. 0. 0. 0.]
    # [0. 1. 0. 0.]]

    kalman.processNoiseCov = 1e-4 * np.eye(4)
    # process noise covariance matrix (Q)
    # [[0.0001 0.     0.     0.    ]
    # [0.     0.0001 0.     0.    ]
    # [0.     0.     0.0001 0.    ]
    # [0.     0.     0.     0.0001]]

    kalman.measurementNoiseCov = 5e-1 * np.eye(2)
    # measurement noise covariance matrix (R)
    # [[15.  0.]
    # [ 0. 15.]]

    kalman.errorCovPost = 1. * np.eye(4)
    # posteriori error estimate covariance matrix (P(k)): P(k)=(I-K(k)*H)*P'(k)
    # [[1. 0. 0. 0.]
    # [0. 1. 0. 0.]
    # [0. 0. 1. 0.]
    # [0. 0. 0. 1.]]

    while (True):
        if (start):
            measurement = 1. * np.array([[0.], [0.]])

            measured_x = cursor_x + np.random.randn(1, 1) * kalman.measurementNoiseCov[0, 0]
            measured_y = cursor_y + np.random.randn(1, 1) * kalman.measurementNoiseCov[1, 1]

            measurement[0] = 1.0 * measured_x
            measurement[1] = 1.0 * measured_y

            # print(measurement)

            prediction = kalman.predict()  # Computes a predicted state.
            # print (prediction)
            kalman.correct(measurement)  # Updates the predicted state from the measurement.
            # print (kalman.correct(measurement))

            cv.circle(img, (int(measurement[0]), int(measurement[1])), 2, (255, 255, 0), thickness=1)
            cv.circle(img, (int(kalman.statePost[0]), int(kalman.statePost[1])), 2, (0, 255, 255), thickness=10)

        cv.imshow("KalmanDemo", img)

        code = cv.waitKey(1)
        if code != -1:
            break

    cv.destroyWindow("Kalman")


if __name__ == "__main__":
    main()
