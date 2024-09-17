# Temperature Monitoring
Python project with multiple DS18B20 sensors. Config and reporting over MQTT to Home Assistant


## Quick configuration
One-wire configuration needs to be enabledcd, run and enable in settings
```
sudo raspi-config
```

To enable readings run following commands and reboot.
```
sudo modprobe w1-gpio
sudo modprobe w1-therm
```

Connect wires and read temperature

```
cd /sys/bus/w1/devices
```

There should be a folder 28-xxxxxxxxxxxx

With following command the measurements are shown
```
cat w1_slave
```

## Hardware setup
Example of physical connection can be found here, also in depth configuration steps
* https://www.hackster.io/vinayyn/multiple-ds18b20-temp-sensors-interfacing-with-raspberry-pi-d8a6b0

* http://www.d3noob.org/2015/02/raspberry-pi-multiple-temperature.html

![image](https://hackster.imgix.net/uploads/attachments/1479988/ds18b20_9_sensor_bb_h4la0fG72z.jpg)

![image](https://github.com/user-attachments/assets/ca20eaf3-342f-4385-acd8-c1ddcadda2b7)
![image](https://github.com/user-attachments/assets/98ac1eb9-0d5f-4e79-af5b-dc056d884dca)

![image](https://github.com/user-attachments/assets/e4bd06a6-9218-481a-b7ae-445eff599753)
