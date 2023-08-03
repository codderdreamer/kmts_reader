import time
import os
from datetime import datetime

class ProcessModule():
    def __init__(self,application):
        self.application = application
        self.simu = False

    def run(self):
        if self.application.modbus.open_white_led():
            self.application.websocket_module.send_message_to_all("white-led-text-1","Beyaz Led Yakıldı.")
        else:
            self.application.websocket_module.send_message_to_all("white-led-text-1","Beyaz Led Yakılamadı!")
            return False
        time.sleep(1)

        while True:
            print("Running...")
            self.application.websocket_module.send_message_to_all("Clear")
            # 1. örnek için renkli kameradan renkli görüntüyü al
            self.application.websocket_module.send_message_to_all("colourful-img-text")

            if self.application.camera.save_colourful_image(1):
                self.application.websocket_module.send_message_to_all("colourful-img")
            else:
                return False
            
            # Data Matrix Araması
            self.application.websocket_module.send_message_to_all("dataMatrix-text")
            data = self.application.camera.dataMatrix_verification(1)
            self.application.websocket_module.send_message_to_all("dataMatrix-img")
            self.application.websocket_module.send_message_to_all("dataMatrix-result",data)
            
            # Seri No 1 Araması
            self.application.websocket_module.send_message_to_all("seriNo1-text")
            data = self.application.camera.seri_no_1_verification(1)
            self.application.websocket_module.send_message_to_all("seriNo1-result",data)
            self.application.websocket_module.send_message_to_all("seriNo1-img")
            

            # Seri No 2 Araması
            self.application.websocket_module.send_message_to_all("seriNo2-text")
            data = self.application.camera.seri_no_2_verification(1)
            self.application.websocket_module.send_message_to_all("seriNo2-result",data)
            self.application.websocket_module.send_message_to_all("seriNo2-img")

            # Seri No 3 Araması
            self.application.websocket_module.send_message_to_all("seriNo3-text")
            data = self.application.camera.seri_no_3_verification(1)
            self.application.websocket_module.send_message_to_all("seriNo3-result",data)
            self.application.websocket_module.send_message_to_all("seriNo3-img")

            # Digimark Araması
            self.application.websocket_module.send_message_to_all("digimark-text")
            self.application.camera.dataMatrix_Verification(1)
            self.application.websocket_module.send_message_to_all("digimark-img")
            




            print(" while döngüsü başa dönüyor")
            time.sleep(2)