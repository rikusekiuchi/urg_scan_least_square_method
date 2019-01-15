# urg_scan_least_square_method
測域センサを用いて、ロボットが壁に対してどの向きに向いているか調べるパッケージ

## Demonstration
- https://youtu.be/isTf9jK1yvA

## Requirements
- Raspberry Pi 3 Model B
  - ubuntu16.04
- Robot
  - Rasp
- 2 LEDs
  - Left LED :GPIO25
  - Right LED :GPIO24
  
## Usage
```
cd led_device_driver_2
make
sudo insmod myled.ko
sudo chmod 666 /dev/myled0
echo 1 > /dev/myled0 //2LEDs flash
echo 0 > /dev/myled0 //2LEDs solid
echo 3 > /dev/myled0 //Left LED flash
echo 2 > /dev/myled0 //Left LED solid
echo 5 > /dev/myled0 //Right LED flash
echo 4 > /dev/myled0 //Right LED solid
```

## Licence
This repository is licensed under the GPLv3 license
