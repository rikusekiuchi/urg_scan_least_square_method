# urg_scan_least_square_method
- 測域センサを用いて、ロボットが壁に対してどの向きに向いているか調べるパッケージ
- 測域センサで得られた距離のデータとレーザーが出る角度からx,y直行座標系に変換して最小二乗法により計算しています。
- 壁に対して並行で右向きにロボットが向いている向きを0度として計測
- 左右に45度ずつ、左右30度ずつの値を受け取り計算するプログラム(scandata_least_square_method_90.py , scandata_least_square_method_60.py)
- resultに書かれている結果が計測した角度

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
