import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, return_code):
    if return_code == 0:
        print("Connected successfully")
        client.subscribe("hello/a")
    else:
        print(f"Not connected, return code: {return_code}")
        client.failed_connect = True

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

broker_hostname = "localhost"  # Use host IP if needed, or "host.docker.internal" for Docker
port = 1883

client = mqtt.Client()
# client.username_pw_set(username="USER", password="PWD")  # Uncomment if you have credentials
client.on_connect = on_connect  # Assign the function, not call it
client.on_message = on_message  # Assign the function, not call it
client.failed_connect = False

client.connect(broker_hostname, port)
client.loop_start()

try:
    i = 0
    while i < 15 and not client.failed_connect:
        time.sleep(1)
        i += 1
    if client.failed_connect:
        print("Connection failed, exiting...")

finally:
    client.disconnect()
    client.loop_stop()
