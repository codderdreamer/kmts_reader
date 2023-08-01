from Modules.WebsocketModule import *
from Modules.FlaskModule import *
import time
from Modules.Config import *
from Modules.ModbusModule import *
from Modules.CameraModule import *
from Modules.ProcessModule import *

BootError=False

class Application():
    def __init__(self):

        self.test_1_file_path = "/home/pi/Desktop/kmts_reader/static/assets/test_1/"

        # Config Dosyasını Oku
        self.config = Config(self)
        data = self.config.read_config_file()
        self.config.write_config_to_variables(data)

        # Modbusı Başlat
        self.modbus = ModbusModule(self)
        self.modbus.connect_modbus()

        # Websocketi Başlat
        self.websocket_module = WebsocketModule(self)
        self.websocket_module.run()

        # Flaskı Başlat
        self.flask_module = FlaskModule(__name__)
        self.flask_module.run(BootError)

        # Kamerayı Başlat
        self.camera = CameraModule(self)
        threading.Thread(target=self.camera.connect_colourful,daemon=True).start()

        self.process = ProcessModule(self)
        threading.Thread(target=self.process.run,daemon=True).start()

Application()
while True:
    time.sleep(10)
    if BootError:
        print("BootError")
        time.sleep(10)
        break
        