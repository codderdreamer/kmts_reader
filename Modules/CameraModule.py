import numpy as np
import cv2
from threading import Thread
import time
import platform
import json
import os
from pyzbar.pyzbar import decode
from pylibdmtx import pylibdmtx
import math

class CameraModule():
    def __init__(self,application):
        self.application = application
        self.camera_index_4K = None
        self.camera_index_arducam = None
        self.infrared = None
        self.colourful = None
       
        self.cam2pts1 = np.float32([[591,255],[574,1174],[1413,262],[1427,1160]])
        self.cam2pts2 = np.float32([[0,0],[0,700],[700,0],[700,700]])

        self.colourful_counter = 0
        self.colourful_connected = False

        self.infrared_counter = 0
        self.infrared_connected = False

        self.barcode_x = None
        self.barcode_y = None
        self.barcode_w = None
        self.barcode_h = None

        self.center_of_gravity_x = None
        self.center_of_gravity_y = None

        self.actual_r = 1
        self.actual_g = 57
        self.actual_b = 8

        self.circle_center = [None,None]
        self.actual_center = [None,None]

        self.threshold_image = None

        self.datamatrix_readed = False

    def get_colourful_points(self):
        x1 = int(self.application.config.camera.colourful.points.left_top_x)
        y1 = int(self.application.config.camera.colourful.points.left_top_y)
        x2 = int(self.application.config.camera.colourful.points.left_bottom_x)
        y2 = int(self.application.config.camera.colourful.points.left_bottom_y)
        x3 = int(self.application.config.camera.colourful.points.right_top_x)
        y3 = int(self.application.config.camera.colourful.points.right_top_y)
        x4 = int(self.application.config.camera.colourful.points.right_bottom_x)
        y4 = int(self.application.config.camera.colourful.points.right_bottom_y)
        return np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
    
    def get_colourful_resolution_points(self):
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = int(self.application.config.camera.colourful.resolution)
        x3 = int(self.application.config.camera.colourful.resolution)
        y3 = 0
        x4 = int(self.application.config.camera.colourful.resolution)
        y4 = int(self.application.config.camera.colourful.resolution)
        return np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
    
    def cut_colourful_image(self,frame):
        matrix = cv2.getPerspectiveTransform(self.get_colourful_points(),self.get_colourful_resolution_points())
        frame = cv2.warpPerspective(frame,matrix,(700,700))
        return frame
    
    def image_rotate_clockwise(self,frame,counter):
        if counter != 0:
            for i in range(0,counter):
                frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        return frame
    
    def connect_colourful(self):
        print("USB CAMERA bağlanılıyor...")
        self.colourful = cv2.VideoCapture('/dev/v4l/by-id/usb-Arducam_Technology_Co.__Ltd._Arducam_16MP_SN0001-video-index0')
        self.colourful.set(cv2.CAP_PROP_EXPOSURE, int(self.application.config.camera.colourful.exposure))
        self.colourful.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M','J','P','G'))
        self.colourful.set(cv2.CAP_PROP_FRAME_WIDTH,1600)
        self.colourful.set(cv2.CAP_PROP_FRAME_HEIGHT,1200)
        if self.colourful.isOpened():
            print("USB CAMERA Bağlandı.")
            self.colourful_connected = True
            DataToSend = {"Command": "Colourful Camera", "Data": "Opened"}
            self.application.websocket_module.websocket.send_message_to_all(json.dumps(DataToSend))
        else:
            print("USB CAMERA Bağlanmadı!!")
            self.colourful_connected = False
            DataToSend = {"Command": "Colourful Camera", "Data": "Closed"}
            self.application.websocket_module.websocket.send_message_to_all(json.dumps(DataToSend))
            time.sleep(5)
            self.connect_colourful()

    def save_colourful_image(self,stage):
        print("Renkli kameradan görüntüler alınıyor...")
        if self.colourful:
            for i in range(0,6):
                success,frame = self.colourful.read()
            if success:
                self.colourful_counter = 0
                frame = self.cut_colourful_image(frame)
                frame = self.image_rotate_clockwise(frame,self.application.config.camera.colourful.rotation_clockwise_counter)
                # frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
                cv2.imwrite( self.application.test_1_file_path + str(stage) + '/' +  'colourful.png', frame)
                return True
            else:
                print("Kameradan görüntü okunamadı tekrar deneniyor!")
                self.colourful_counter += 1
                if self.colourful_counter > 10:
                    print("Kameradan görüntü 10 kere okunamadı !!! işlem sonlandı !!!")
                    return False
                else:
                    self.save_colourful_image(stage)
        else:
            self.colourful_connected = False
            print("Kamera bağlantısı kopmuş. Tekrar bağlanıp denenecek!")
            Thread(target=self.connect_colourful,daemon=True).start()
            time_start = time.time()
            while self.colourful_connected == False:
                time.sleep(1)
                if time.time() - time_start > 5:
                    break
            if self.colourful_connected:
                print("Kameraya tekrar bağlandı.")
                self.save_colourful_image(stage)
            else:
                print("Kameraya bağlanılamadı !!! işlem sonlandı !!!")
                return False
            
    def dataMatrix_verification(self,stage):
        print("Data Matrix Verification...")
        start = time.time()
        image_original = cv2.imread(self.application.test_1_file_path + str(stage) + '/' + 'colourful.png')
        image_original = 255 - image_original

        data_matrix_finded = False
        threshold_counter = 0.7

        _, threshold = cv2.threshold(image_original, np.max(image_original)*threshold_counter, 256, cv2.THRESH_BINARY)
        cv2.imwrite(self.application.test_1_file_path + str(stage) + '/' + 'thresh.png',threshold)
        data = pylibdmtx.decode(threshold)
        finish = time.time()
        print("Decode edilme:", finish-start)
        print(data)

        # while data_matrix_finded == False:
        #     print("Deneniyor threshold_counter:",threshold_counter )
        #     if threshold_counter > 1:
        #         print("İşlem sonlandı. Data matrix bulunamadı. Ththreshold_counter 1")
        #         break
            
        #     _, threshold = cv2.threshold(image_original, np.max(image_original)*threshold_counter, 256, cv2.THRESH_BINARY)
        #     data = pylibdmtx.decode(threshold)
        #     if len(data) != 0:
        #         print("******** Data bulundu: ", data)
        #         data_matrix_finded = True
        #     else:
        #         print("threshold_counter: ",threshold_counter, " Bulunamadı.")
            
        #     threshold_counter = threshold_counter + 0.1

        #     time.sleep(1)
        
