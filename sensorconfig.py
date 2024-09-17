import os
import time
import paho.mqtt.publish as publish
import json
import sys


#sensor config
sensors = ["28-062019773640", "28-0620198db2b9", "28-3ce1e381906c","28-3ce1e3819964"]
sensors_map = { sensors[0]: "probe_0",
                sensors[1]: "probe_1",
                sensors[2]: "probe_2",
                sensors[3]: "probe_3"}
#dictionary
sensors_name = {sensors[0]: "Sea water",
                sensors[1]: "Outdoor",
                sensors[2]: "Indoor"}


#ha broker config
Broker = '100.77.110.64' #'192.168.0.150'
auth = {
    'username': 'usr',
    'password': 'pw',
}

#mqtt topic for updatd values
pub_topic = 'kokki/'

reconnect_count = 0



#mqtt discovery
#https://www.home-assistant.io/integrations/mqtt/#discovery-topic
#The discovery topic needs to follow a specific format:
#<discovery_prefix>/<component>/[<node_id>/]<object_id>/config
def createDiscovery(probe):
    discovery_topic0 = 'homeassistant/sensor/kokki/'+probe+'/config'
    discovery_msg0 ={
    "name": probe,
    "state_topic": pub_topic+probe,
    "state_class": "measurement",

    "device": { "identifiers": "kokki","name":"kokki" },
    "unit_of_measurement": "°C",
    "icon": "hass:thermometer",
    "platform": "mqtt",
    "unique_id": probe
    }


    return discovery_topic0, json.dumps(discovery_msg0)



def atStartup():
  print("Setting Up Sensors In HA..")

  for probe in sensors_map.values():
    #print("Setting Up Sensors In HA.. %s" % probe)

    discovery_topic,discovery_msg =  createDiscovery(probe)
#    print("disc topic",discovery_topic)
#    print("disc msg",discovery_msg)
    try:
        publish.single(discovery_topic,discovery_msg, hostname=Broker, auth=auth,retain=True)

    except:
        pass
       #try again...


def read_temp(id):
  sensor = "/sys/devices/w1_bus_master1/" + id + "/w1_slave"
  temp = -99  # error value do not send
  try:
    f = open(sensor, "r")
    data = f.read()
    f.close()
    if "YES" in data:
      partitioned = data.partition(' t=')
      temp = float(partitioned[2]) / 1000.0
  except Exception:
    pass

  if temp != -99:
#return only good values
    return temp


#not in use
def print_temp ():

  for sensor in sensors:
#    print('print_temp %d' %( sensor))
    temp = read_temp(sensor)
    print('%s: %s = %.2fC' % (time.asctime(),sensors_name[sensor], temp))
    temps[sensor]=temp
   #to csv?



def sendHA():
  for sensor in sensors:
    temp = read_temp(sensor)
    #print("sendha sensor %s", sensor)
    if temp is not None:
       #commented out to reduce log
       #print("topic ",pub_topic+sensors_map[sensor])
       #print('%s: %s = %.2fC' % (time.asctime(),sensors_name[sensor], temp))

       try:
           publish.single(pub_topic+sensors_map[sensor], str(temp), hostname=Broker, auth=auth)
       except Exception as err:
           global reconnect_count
           reconnect_count = reconnect_count+1
           print("%s Error: %s, reconnecting attempt %d" % ( time.asctime(),err,reconnect_count))
           time.sleep(5)
           atStartup()
    time.sleep(1)



if __name__ == '__main__':
  atStartup()

  print("Started: ",time.asctime())
  try:
    while True:
      sendHA()
      time.sleep(300) 

     # time.sleep(1)  # Check the exit flag every second
  except KeyboardInterrupt:
    print(" Ctrl+C pressed. Setting exit flag...")
    #client.loop_stop()
    exit_flag = True
    #stop_event.set()  # Signal the threads to stop
    sys.exit(0)  # Exit the script
    
    
    
#todo should be improved https://github.com/emqx/MQTT-Client-Examples/blob/master/mqtt-client-Python3/pub_sub_tcp.py

