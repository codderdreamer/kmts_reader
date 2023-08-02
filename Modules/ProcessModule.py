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
            if self.application.camera.save_colourful_image(1):
                self.application.websocket_module.send_message_to_all("colourful-img-1")
            else:
                self.application.websocket_module.send_message_to_all("colourful-text-1","Renkli kamera görüntüsü alınamadı!")
                return False
            
            # Data Matrix Araması
            self.application.camera.dataMatrix_verification(1)

            # Seri No 1 Araması
            self.application.camera.seri_no_1_verification(1)

            # Seri No 2 Araması
            self.application.camera.seri_no_2_verification(1)

            # Seri No 3 Araması
            self.application.camera.seri_no_3_verification(1)



            print(" while döngüsü başa dönüyor")




        time.sleep(1)