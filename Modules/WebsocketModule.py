import websocket_server
import json
import threading


class WebsocketModule():
    def __init__(self,application):
        self.application = application
        self.websocket = websocket_server.WebsocketServer('0.0.0.0', 9000 )

    def run(self):
        self.websocket.set_fn_new_client(self.NewClientws)
        self.websocket.set_fn_client_left(self.ClientLeftws)
        self.websocket.set_fn_message_received(self.MessageReceivedws)
        threading.Thread(target=self.websocket.run_forever,daemon=True).start()
        print("Websocket Started.")

    def send_colourful_camera_opened(self,client):
        DataToSend = {"Command": "Colourful Camera", "Data": "Opened"}
        self.websocket.send_message(client,json.dumps(DataToSend))

    def send_colourful_camera_closed(self,client):
        DataToSend = {"Command": "Colourful Camera", "Data": "Closed"}
        self.websocket.send_message(client,json.dumps(DataToSend))

    def send_modbus_opened(self,client):
        DataToSend = {"Command": "Modbus", "Data": "Opened"}
        self.websocket.send_message(client,json.dumps(DataToSend))

    def send_modbus_closed(self,client):
        DataToSend = {"Command": "Modbus", "Data": "Closed"}
        self.websocket.send_message(client,json.dumps(DataToSend))

    def NewClientws(self,client, server):
        print("New client connected and was given id %d" % client['id'], client["address"])

        # Colourful Camera
        if hasattr(self.application, "camera"):
            if hasattr(self.application.camera, "colourful"):
                if hasattr(self.application.camera.colourful, "isOpened"):
                    if self.application.camera.colourful.isOpened():
                        self.send_colourful_camera_opened(client)
                    else:
                        self.send_colourful_camera_closed(client)
                else:
                    self.send_colourful_camera_closed(client)
            else:
                self.send_colourful_camera_closed(client)
        else:
            self.send_colourful_camera_closed(client)

        # Modbus      
        if hasattr(self.application, "modbus"):
            if hasattr(self.application.modbus, "client"):
                if hasattr(self.application.modbus.client, "connected"):
                    if self.application.modbus.client.connected:
                        self.send_modbus_opened(client)
                    else:
                        self.send_modbus_closed(client)
                else:
                    self.send_modbus_closed(client)
            else:
                self.send_modbus_closed(client)
        else:
            self.send_modbus_closed(client)


    def send_message_to_all(self, command = None, data = None):
        DataToSend = {"Command": command, "Data": data}
        self.websocket.send_message_to_all(json.dumps(DataToSend))

    def ClientLeftws(self,client, server):
        print("Client(%d) disconnected" % client['id'])

    def MessageReceivedws(self, client, server, message):
        IncomingData = json.loads(message)
        print(IncomingData)