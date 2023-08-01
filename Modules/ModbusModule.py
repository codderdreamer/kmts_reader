
'''
Coils 0 İşaret Doğrulamayı Başlat (True yapıldığında ölçüme başlar ölçüm bitiminde False olur.)
Coils 1 Beyaz LED Kontrol
Coils 2 Mavi LED Kontrol
Coils 3 IR LED Kontrol

Coils 5 Buton durumu (Butona basılırsa "True" olur komut işlendikten sonra karşı taraf "False" yapmalıdır.)

HoldingRegisters 0 İşaret doğrulama şiddeti        (0-2500 aralğında ayarlanmalı.)
HoldingRegisters 1 Beyaz LED şiddeti               (0-4095 aralğında ayarlanmalı.)
HoldingRegisters 2 Mavi LED şiddeti                (0-4095 aralğında ayarlanmalı.)
HoldingRegisters 3 IR LED şiddeti                  (0-4095 aralğında ayarlanmalı.)


InputRegisters 0               647nm şiddeti (0-32768 Aralığında değer alabilir.)
InputRegisters 1               690nm şiddeti (0-32768 Aralığında değer alabilir.)
InputRegisters 2               730nm şiddeti (0-32768 Aralığında değer alabilir.)
InputRegisters 3               850nm şiddeti (0-32768 Aralığında değer alabilir.)
InputRegisters 4               Ortam Sıcaklık Sensörü (Ölçülen Sıcaklığın 100 katı)
InputRegisters 5               PCB Sıcaklık Sensörü      (Ölçülen Sıcaklığın 100 katı)

'''
from pymodbus.client import ModbusSerialClient
from threading import Thread
import time

class ModbusModule():
    def __init__(self,application):
        self.application = application
        self.client = None

    def connect_modbus(self):
        try:
            self.client = ModbusSerialClient(port=self.application.config.modbus_port, baudrate=9600, method = "rtu")
            self.client.connect()
            if self.client.connected:
                print("Modbus bağlandı.")
                self.close_all_coils()
            else:
                print("Modbus bağlanmadı!")
        except Exception as e:
            print(e)

####################################### COILS WRITE #######################################

    '''
    Sensörden Okuma Yap! 
    Coils 0 İşaret Doğrulamayı Başlat (True yapıldığında ölçüme başlar ölçüm bitiminde False olur.)
    '''
    def open_sensor(self):
        try:
            self.client.write_coils(0,[1,0,0,0],1)
            return True
        except Exception as e:
            print(e)
            return False
        
    '''
    Sadece Beyaz Ledi Yak!
    Coils 1 Beyaz LED Kontrol
    '''
    def open_white_led(self):
        try:
            self.set_white_light_intensity(self.application.config.light_intensity.white)
            self.client.write_coils(0,[0,1,0,0],1)
            return True
        except Exception as e:
            print(e)
            return False

    '''
    Sadece Mavi Ledi Yak!
    Coils 2 Mavi LED Kontrol
    '''
    def open_blue_led(self):
        try:
            self.set_blue_light_intensity(self.application.config.light_intensity.blue)
            self.client.write_coils(0,[0,0,1,0],1)
            return True
        except Exception as e:
            print(e)
            return False

    '''
    Sadece IR Ledi Yak!
    Coils 3 IR LED Kontrol
    '''
    def open_IR_led(self):
        try:
            self.set_IR_light_intensity(self.application.config.light_intensity.IR)
            self.client.write_coils(0,[0,0,0,1],1)
            return True
        except Exception as e:
            print(e)
            return False

    '''
    Bütün Ledleri ve Sensörü Kapat!
    '''
    def close_all_coils(self):
        try:
            self.client.write_coils(0,[0,0,0,0],1)
        except Exception as e:
            print(e)

####################################### HOLDING REGISTER #######################################

    '''
    İşaret Doğrulama Led Şiddeti Ayarla
    HoldingRegisters 0 İşaret doğrulama şiddeti        (0-2500 aralğında ayarlanmalı.)
    '''
    def set_sing_verification_light_intensity(self,value):
        try:
            self.client.write_register(0,value,1)
        except Exception as e:
            print(e)

    '''
    Beyaz Led Şiddeti Ayarla
    HoldingRegisters 1 Beyaz LED şiddeti               (0-4095 aralğında ayarlanmalı.)
    '''
    def set_white_light_intensity(self,value):
        try:
            self.client.write_register(1,value,1)
        except Exception as e:
            print(e)

    '''
    Mavi Led Şiddeti Ayarla
    HoldingRegisters 2 Mavi LED şiddeti                (0-4095 aralğında ayarlanmalı.)
    '''
    def set_blue_light_intensity(self,value):
        try:
            self.client.write_register(2,value,1)
        except Exception as e:
            print(e)

    '''
    IR Led Şiddeti Ayarla
    HoldingRegisters 3 IR LED şiddeti                  (0-4095 aralğında ayarlanmalı.)
    '''
    def set_IR_light_intensity(self,value):
        try:
            self.client.write_register(3,value,1)
        except Exception as e:
            print(e)

####################################### INPUT REGISTERS #######################################
# InputRegisters 0               647nm şiddeti (0-32768 Aralığında değer alabilir.)
# InputRegisters 1               690nm şiddeti (0-32768 Aralığında değer alabilir.)
# InputRegisters 2               730nm şiddeti (0-32768 Aralığında değer alabilir.)
# InputRegisters 3               850nm şiddeti (0-32768 Aralığında değer alabilir.)
# InputRegisters 4               Ortam Sıcaklık Sensörü (Ölçülen Sıcaklığın 100 katı)
# InputRegisters 5               PCB Sıcaklık Sensörü      (Ölçülen Sıcaklığın 100 katı)

    '''
    Sensörden Gelen Değerleri Oku!
    '''
    def read_input_registers(self):
        try:
            input_registers = self.client.read_input_registers(0,5,1).registers
            x=input_registers[1]
            y=input_registers[2]
            input_registers[1]=y
            input_registers[2]=x
            return input_registers
        except Exception as e:
            print(e)
            return False
        


