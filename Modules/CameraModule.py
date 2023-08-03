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
import os
import easyocr
import cv2
from matplotlib import pyplot as plt

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

# Colourful Image Cutting
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
        y2 = int(1030)
        x3 = int(685)
        y3 = 0
        x4 = int(685)
        y4 = int(1030)
        return np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
    
    def cut_colourful_image(self,frame):
        matrix = cv2.getPerspectiveTransform(self.get_colourful_points(),self.get_colourful_resolution_points())
        frame = cv2.warpPerspective(frame,matrix,(685,1030))
        return frame

# Data Matrix Cutting
    def get_colourful_dataMatrix_points(self):
        x1 = int(self.application.config.camera.colourful.dataMatrixPoints.left_top_x)
        y1 = int(self.application.config.camera.colourful.dataMatrixPoints.left_top_y)
        x2 = int(self.application.config.camera.colourful.dataMatrixPoints.left_bottom_x)
        y2 = int(self.application.config.camera.colourful.dataMatrixPoints.left_bottom_y)
        x3 = int(self.application.config.camera.colourful.dataMatrixPoints.right_top_x)
        y3 = int(self.application.config.camera.colourful.dataMatrixPoints.right_top_y)
        x4 = int(self.application.config.camera.colourful.dataMatrixPoints.right_bottom_x)
        y4 = int(self.application.config.camera.colourful.dataMatrixPoints.right_bottom_y)
        return np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
    
    def get_colourful_dataMatrix_resolution_points(self):
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = int(self.application.config.camera.colourful.resolution_datamatrix)
        x3 = int(self.application.config.camera.colourful.resolution_datamatrix)
        y3 = 0
        x4 = int(self.application.config.camera.colourful.resolution_datamatrix)
        y4 = int(self.application.config.camera.colourful.resolution_datamatrix)
        return np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
    
    def cut_colourful_image_dataMatrix(self,frame):
        matrix = cv2.getPerspectiveTransform(self.get_colourful_dataMatrix_points(),self.get_colourful_dataMatrix_resolution_points())
        frame = cv2.warpPerspective(frame,matrix,(int(self.application.config.camera.colourful.resolution_datamatrix),int(self.application.config.camera.colourful.resolution_datamatrix)))
        return frame
    
# Seri No 1 Cutting
    def get_colourful_seriNo_1_points(self):
        x1 = int(self.application.config.camera.colourful.seriNoPoints1.left_top_x)
        y1 = int(self.application.config.camera.colourful.seriNoPoints1.left_top_y)
        x2 = int(self.application.config.camera.colourful.seriNoPoints1.left_bottom_x)
        y2 = int(self.application.config.camera.colourful.seriNoPoints1.left_bottom_y)
        x3 = int(self.application.config.camera.colourful.seriNoPoints1.right_top_x)
        y3 = int(self.application.config.camera.colourful.seriNoPoints1.right_top_y)
        x4 = int(self.application.config.camera.colourful.seriNoPoints1.right_bottom_x)
        y4 = int(self.application.config.camera.colourful.seriNoPoints1.right_bottom_y)
        return np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
    
    def get_colourful_seriNo_1_resolution_points(self):
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 60
        x3 = 180
        y3 = 0
        x4 = 180
        y4 = 60
        return np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
    
    def cut_colourful_image_seriNo_1(self,frame):
        matrix = cv2.getPerspectiveTransform(self.get_colourful_seriNo_1_points(),self.get_colourful_seriNo_1_resolution_points())
        frame = cv2.warpPerspective(frame,matrix,(180,60))
        return frame
    
# Seri No 2 Cutting
    def get_colourful_seriNo_2_points(self):
        x1 = int(self.application.config.camera.colourful.seriNoPoints2.left_top_x)
        y1 = int(self.application.config.camera.colourful.seriNoPoints2.left_top_y)
        x2 = int(self.application.config.camera.colourful.seriNoPoints2.left_bottom_x)
        y2 = int(self.application.config.camera.colourful.seriNoPoints2.left_bottom_y)
        x3 = int(self.application.config.camera.colourful.seriNoPoints2.right_top_x)
        y3 = int(self.application.config.camera.colourful.seriNoPoints2.right_top_y)
        x4 = int(self.application.config.camera.colourful.seriNoPoints2.right_bottom_x)
        y4 = int(self.application.config.camera.colourful.seriNoPoints2.right_bottom_y)
        return np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
    
    def get_colourful_seriNo_2_resolution_points(self):
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 70
        x3 = 245
        y3 = 0
        x4 = 245
        y4 = 70
        return np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])


    def cut_colourful_image_seriNo_2(self,frame):
        matrix = cv2.getPerspectiveTransform(self.get_colourful_seriNo_2_points(),self.get_colourful_seriNo_2_resolution_points())
        frame = cv2.warpPerspective(frame,matrix,(245,70))
        return frame
    
# Seri No 3 Cutting
    def get_colourful_seriNo_3_points(self):
        x1 = int(self.application.config.camera.colourful.seriNoPoints3.left_top_x)
        y1 = int(self.application.config.camera.colourful.seriNoPoints3.left_top_y)
        x2 = int(self.application.config.camera.colourful.seriNoPoints3.left_bottom_x)
        y2 = int(self.application.config.camera.colourful.seriNoPoints3.left_bottom_y)
        x3 = int(self.application.config.camera.colourful.seriNoPoints3.right_top_x)
        y3 = int(self.application.config.camera.colourful.seriNoPoints3.right_top_y)
        x4 = int(self.application.config.camera.colourful.seriNoPoints3.right_bottom_x)
        y4 = int(self.application.config.camera.colourful.seriNoPoints3.right_bottom_y)
        return np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
    
    def get_colourful_seriNo_3_resolution_points(self):
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 215
        x3 = 70
        y3 = 0
        x4 = 70
        y4 = 215
        return np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])


    def cut_colourful_image_seriNo_3(self,frame):
        matrix = cv2.getPerspectiveTransform(self.get_colourful_seriNo_3_points(),self.get_colourful_seriNo_3_resolution_points())
        frame = cv2.warpPerspective(frame,matrix,(70,215))
        return frame
    
# Digimark Cutting
    def get_colourful_digimark_points(self):
        x1 = int(self.application.config.camera.colourful.digimarkCodePoints.left_top_x)
        y1 = int(self.application.config.camera.colourful.digimarkCodePoints.left_top_y)
        x2 = int(self.application.config.camera.colourful.digimarkCodePoints.left_bottom_x)
        y2 = int(self.application.config.camera.colourful.digimarkCodePoints.left_bottom_y)
        x3 = int(self.application.config.camera.colourful.digimarkCodePoints.right_top_x)
        y3 = int(self.application.config.camera.colourful.digimarkCodePoints.right_top_y)
        x4 = int(self.application.config.camera.colourful.digimarkCodePoints.right_bottom_x)
        y4 = int(self.application.config.camera.colourful.digimarkCodePoints.right_bottom_y)
        return np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
    
    def get_colourful_digimark_resolution_points(self):
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 215
        x3 = 220
        y3 = 0
        x4 = 220
        y4 = 215
        return np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])


    def cut_colourful_image_digimark(self,frame):
        matrix = cv2.getPerspectiveTransform(self.get_colourful_digimark_points(),self.get_colourful_digimark_resolution_points())
        frame = cv2.warpPerspective(frame,matrix,(220,215))
        return frame


    def image_rotate_clockwise(self,frame,counter):
        if counter != 0:
            for i in range(0,counter):
                frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        return frame
    
    def connect_colourful(self):
        print("USB CAMERA bağlanılıyor...")
        self.colourful = cv2.VideoCapture('/dev/v4l/by-id/usb-Sonix_Technology_Co.__Ltd._USB_2.0_Camera-video-index0')
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
                frame = self.image_rotate_clockwise(frame,self.application.config.camera.colourful.rotation_clockwise_counter)
                frame = self.cut_colourful_image(frame)
                frame = self.image_rotate_clockwise(frame,2)
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

        image_original = self.cut_colourful_image_dataMatrix(image_original)

        cv2.imwrite(self.application.test_1_file_path + str(stage) + '/' + 'dataMatrix.png',image_original)

        image_original = 255 - image_original

        threshold_counter = 0.5

        _, threshold = cv2.threshold(image_original, np.max(image_original)*threshold_counter, 256, cv2.THRESH_BINARY)
        cv2.imwrite(self.application.test_1_file_path + str(stage) + '/' + 'dataMatrixThresh.png',threshold)
        data = pylibdmtx.decode(threshold)
        finish = time.time()
        print("Decode edilme:", finish-start)
        print(data)
        if len(data)>0:
            return data[0][0].decode("utf-8")
        else:
            return None


    def seri_no_1_verification(self,stage):
        print("Seri No Verification")
        start = time.time()
        image_original = cv2.imread(self.application.test_1_file_path + str(stage) + '/' + 'colourful.png')

        image_original = self.cut_colourful_image_seriNo_1(image_original)

        cv2.imwrite(self.application.test_1_file_path + str(stage) + '/' + 'seriNo1.png',image_original)

        # Changing the image path
        IMAGE_PATH = self.application.test_1_file_path + str(stage) + '/' + 'seriNo1.png'
        # Same code here just changing the attribute from ['en'] to ['zh']
        # reader = easyocr.Reader(['tr'])
        # result = reader.readtext(IMAGE_PATH,paragraph="False")
        time.sleep(3)
        result = "123"
        print (result)
        if len(result)>0:
            # return result[0][1]
            return result
        else:
            return None

    def seri_no_2_verification(self,stage):
        print("Seri No Verification")
        start = time.time()
        image_original = cv2.imread(self.application.test_1_file_path + str(stage) + '/' + 'colourful.png')

        image_original = self.cut_colourful_image_seriNo_2(image_original)

        cv2.imwrite(self.application.test_1_file_path + str(stage) + '/' + 'seriNo2.png',image_original)

        # Changing the image path
        IMAGE_PATH = self.application.test_1_file_path + str(stage) + '/' + 'seriNo2.png'
        # Same code here just changing the attribute from ['en'] to ['zh']
        # reader = easyocr.Reader(['tr'])
        # result = reader.readtext(IMAGE_PATH,paragraph="False")
        time.sleep(3)
        result = "123"
        print (result) 
        if len(result)>0:
            # return result[0][1]
            return result
        else:
            return None

    def seri_no_3_verification(self,stage):
        print("Seri No Verification")
        start = time.time()
        image_original = cv2.imread(self.application.test_1_file_path + str(stage) + '/' + 'colourful.png')

        image_original = self.cut_colourful_image_seriNo_3(image_original)

        image_original = self.image_rotate_clockwise(image_original,1)

        cv2.imwrite(self.application.test_1_file_path + str(stage) + '/' + 'seriNo3.png',image_original)

        # Changing the image path
        IMAGE_PATH = self.application.test_1_file_path + str(stage) + '/' + 'seriNo3.png'
        # Same code here just changing the attribute from ['en'] to ['zh']
        # reader = easyocr.Reader(['tr'])
        # result = reader.readtext(IMAGE_PATH,paragraph="False")
        time.sleep(3)
        result = "123"
        print (result) 
        if len(result)>0:
            # return result[0][1]
            return result
        else:
            return None

    def dataMatrix_Verification(self,stage):
        print("Data Matrix Verification")
        start = time.time()
        image_original = cv2.imread(self.application.test_1_file_path + str(stage) + '/' + 'colourful.png')

        image_original = self.cut_colourful_image_digimark(image_original)

        cv2.imwrite(self.application.test_1_file_path + str(stage) + '/' + 'digimark.png',image_original)

    def result(self,stage):
        print("Result")
        start = time.time()

        
        start_point_dataMatrix = (self.application.config.camera.colourful.dataMatrixPoints.left_top_x, self.application.config.camera.colourful.dataMatrixPoints.left_top_y)
        end_point_dataMatrix = (self.application.config.camera.colourful.dataMatrixPoints.right_bottom_x, self.application.config.camera.colourful.dataMatrixPoints.right_bottom_y)

        start_point_seriNo1 = (self.application.config.camera.colourful.seriNoPoints1.left_top_x, self.application.config.camera.colourful.seriNoPoints1.left_top_y)
        end_point_seriNo1 = (self.application.config.camera.colourful.seriNoPoints1.right_bottom_x, self.application.config.camera.colourful.seriNoPoints1.right_bottom_y)

        start_point_seriNo2 = (self.application.config.camera.colourful.seriNoPoints2.left_top_x, self.application.config.camera.colourful.seriNoPoints2.left_top_y)
        end_point_seriNo2 = (self.application.config.camera.colourful.seriNoPoints2.right_bottom_x, self.application.config.camera.colourful.seriNoPoints2.right_bottom_y)

        start_point_seriNo3 = (self.application.config.camera.colourful.seriNoPoints3.left_top_x, self.application.config.camera.colourful.seriNoPoints3.left_top_y)
        end_point_seriNo3 = (self.application.config.camera.colourful.seriNoPoints3.right_bottom_x, self.application.config.camera.colourful.seriNoPoints3.right_bottom_y)

        start_point_digimark = (self.application.config.camera.colourful.digimarkCodePoints.left_top_x, self.application.config.camera.colourful.digimarkCodePoints.left_top_y)
        end_point_digimark = (self.application.config.camera.colourful.digimarkCodePoints.right_bottom_x, self.application.config.camera.colourful.digimarkCodePoints.right_bottom_y)


        
        
        color = (255, 0, 0)
        thickness = 2

        image_original = cv2.imread(self.application.test_1_file_path + str(stage) + '/' + 'colourful.png')

        image_original = cv2.rectangle(image_original, start_point_dataMatrix, end_point_dataMatrix, color, thickness)
        image_original = cv2.rectangle(image_original, start_point_seriNo1, end_point_seriNo1, color, thickness)
        image_original = cv2.rectangle(image_original, start_point_seriNo2, end_point_seriNo2, color, thickness)
        image_original = cv2.rectangle(image_original, start_point_seriNo3, end_point_seriNo3, color, thickness)
        image_original = cv2.rectangle(image_original, start_point_digimark, end_point_digimark, color, thickness)

        cv2.imwrite(self.application.test_1_file_path + str(stage) + '/' + 'result.png',image_original)




        
