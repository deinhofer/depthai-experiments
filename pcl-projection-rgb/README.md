

# Sample video
![](https://media.giphy.com/media/kf89fLK4b6DvAKEDnu/giphy.gif)

# RGB-D conversion

In this experiment `rgbd_creating_o3d.py/rgbd_creating_no_o3d.py` allows you to convert depth in rectified_right frame to rgb camera frame

`rgbd_creating_no_o3d.py` will consists of some noise.

# Point cloud with rgb 
![demogif](https://media.giphy.com/media/mH321k0lCXAgP4bY21/giphy.gif)

use `colorized_point_cloud.py` to obtain point could in rgb camera reference frame with color.(if you don't need color overlapped with rgb you can skip 2 steps)

## Installation

```
python3 -m pip install -r requirements.txt
```


## Calibrate camera (if needed)

To run this application, your device needs to be calibrated with rgb camera which was not carried out in devices before Dec 2020. Will soon provide an update new calibration tool to obtain rgb camera calibration

If you received the EEPROM error, like the one below:

```
legacy, get_right_intrinsic() is not available in version -1
recalibrate and load the new calibration to the device. 
```
