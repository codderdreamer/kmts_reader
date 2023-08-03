import time
import os
from datetime import datetime

class ProcessModule():
    def __init__(self,application):
        self.application = application
        self.simu = False

    def run(self):
        

        while True:
            print("Running...")
            if self.application.modbus.open_white_led():
                self.application.websocket_module.send_message_to_all("white-led-text-1","Beyaz Led Yakıldı.")
            else:
                self.application.websocket_module.send_message_to_all("white-led-text-1","Beyaz Led Yakılamadı!")
                return False
            time.sleep(1)

            self.application.websocket_module.send_message_to_all("Clear")
            # 1. örnek için renkli kameradan renkli görüntüyü al
            self.application.websocket_module.send_message_to_all("colourful-img-text")

            if self.application.camera.save_colourful_image(1):
                self.application.websocket_module.send_message_to_all("colourful-img")
            else:
                return False
            
            # Data Matrix Araması
            print("************************* Data Matrix Araması *************************")
            self.application.websocket_module.send_message_to_all("dataMatrix-text")
            data = self.application.camera.dataMatrix_verification(1)
            self.application.websocket_module.send_message_to_all("dataMatrix-img")
            self.application.websocket_module.send_message_to_all("dataMatrix-result",data)
            
            # Seri No 1 Araması
            print("************************* Seri No 1 Araması *************************")
            self.application.websocket_module.send_message_to_all("seriNo1-text")
            data = self.application.camera.seri_no_1_verification(1)
            self.application.websocket_module.send_message_to_all("seriNo1-result",data)
            self.application.websocket_module.send_message_to_all("seriNo1-img")
            

            # Seri No 2 Araması
            print("************************* Seri No 2 Araması *************************")
            self.application.websocket_module.send_message_to_all("seriNo2-text")
            data = self.application.camera.seri_no_2_verification(1)
            self.application.websocket_module.send_message_to_all("seriNo2-result",data)
            self.application.websocket_module.send_message_to_all("seriNo2-img")

            # Seri No 3 Araması
            print("************************* Seri No 3 Araması *************************")
            self.application.websocket_module.send_message_to_all("seriNo3-text")
            data = self.application.camera.seri_no_3_verification(1)
            self.application.websocket_module.send_message_to_all("seriNo3-result",data)
            self.application.websocket_module.send_message_to_all("seriNo3-img")

            # Digimark Araması
            print("************************* Digimark Araması *************************")
            self.application.websocket_module.send_message_to_all("digimark-text")
            self.application.camera.dataMatrix_Verification(1)
            time.sleep(3)
            self.application.websocket_module.send_message_to_all("digimark-img")

            # Mürekkep Araması
            print("************************* Mürekkep Araması *************************")
            self.application.websocket_module.send_message_to_all("ink-text")
            if self.application.modbus.open_sensor():
                time.sleep(1)
                input_registers = self.application.modbus.read_input_registers()
                print("Okunan sensör değerleri: ",input_registers)
                self.application.websocket_module.send_message_to_all("ink-result",input_registers)
            else:
                print("Sensör açma komutu gönderilemedi !!!")

            # Sonuç
            self.application.camera.result(1)
            self.application.websocket_module.send_message_to_all("result-img")
            
            




            print(" while döngüsü başa dönüyor")
            time.sleep(5)