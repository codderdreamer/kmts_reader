import time
import os
from datetime import datetime

class ProcessModule():
    def __init__(self,application):
        self.application = application
        self.simu = False

    def run(self):
        
        print("Running...")
        if self.application.modbus.open_white_led():
            self.application.websocket_module.send_message_to_all("white-led-text-1","Beyaz Led Yakıldı.")
        else:
            self.application.websocket_module.send_message_to_all("white-led-text-1","Beyaz Led Yakılamadı!")
            return False
        time.sleep(2)

        # 1. örnek için renkli kameradan renkli görüntüyü al
        if self.application.camera.save_colourful_image(1):
            self.application.websocket_module.send_message_to_all("colourful-img-1")
        else:
            self.application.websocket_module.send_message_to_all("colourful-text-1","Renkli kamera görüntüsü alınamadı!")
            return False
        
        # Data Matrix Araması
        self.application.camera.dataMatrix_verification(1)




        time.sleep(1)