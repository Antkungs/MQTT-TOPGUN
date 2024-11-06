# MQTT-TOPGUN
 
ให้ทำการตั้งค่า mosquitto.conf
    listener 1883 0.0.0.0
    allow_anonymous true
    persistence true
    persistence_location /mosquitto/data/
    log_dest file /mosquitto/log/mosquitto.log
    log_dest stdout

run:
docker run -dp 1883:1883 -v ../PATHYOU MOSQUITTO FOLDER/:/mosquitto/ --restart always --name NAME_IN_DOCKER eclipse-mosquitto

request lib python
pip install paho-mqtt

test with MQTTX_APP
