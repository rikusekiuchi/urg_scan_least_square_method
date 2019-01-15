# urg_scan_least_square_method
測域センサを用いて、ロボットが壁に対してどの向きに向いているか調べるパッケージ

## Demonstration
- https://youtu.be/isTf9jK1yvA

## Requirements

- pc側
  - ubuntu16.04

- ラズパイマウス(アールティ社)
  - Raspberry Pi 3 Model B
  - ubuntu16.04

- レーザーレンジファインダー
  - URG-04LX-UG01(北陽電機)
  
## Usage

ラズパイマウス側
```
roscore
sudo apt install ros-kinetic-urg-node   //別のターミナルから
rosrun urg_node urg_node

```

PC側

```
git clone https://github.com/rikusekiuchi/urg_scan_least_square_method.git
roscd urg_scan_least_square_method/script/
chmod +x scandata_least_square_method_60.py
chmod +x scandata_least_square_method_90.py
rosrun urg_scan_least_square_method scandata_least_square_method_60.py
rosrun urg_scan_least_square_method scandata_least_square_method_90.py
```


## Licence
This software is released under the MIT License, see LICENSE.txt.
