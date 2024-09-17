# Temperature Monitoring
Python project with multiple DS18B20 sensors. Config and reporting over MQTT to Home Assistant

To enable the one-wire interface use raspi config
  sudo raspi-config

To enable readings run
  sudo modprobe w1-therm


Measurements will be in folder, navigate to 
  cd /sys/bus/w1/devices 

There should be a folder  28-xxxxxxxxxxxx

With command the measurements are shown
  cat w1_slave


Example of physical connection can be found here
https://www.hackster.io/vinayyn/multiple-ds18b20-temp-sensors-interfacing-with-raspberry-pi-d8a6b0
or here
http://www.d3noob.org/2015/02/raspberry-pi-multiple-temperature.html

From the terminal as the ‘pi’ user run the command;
sudo modprobe w1-gpio

![image](https://github.com/user-attachments/assets/ca20eaf3-342f-4385-acd8-c1ddcadda2b7)
![image](https://github.com/user-attachments/assets/98ac1eb9-0d5f-4e79-af5b-dc056d884dca)

![image](https://github.com/user-attachments/assets/e4bd06a6-9218-481a-b7ae-445eff599753)
