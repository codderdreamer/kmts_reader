import os
import json

file_path = "/home/pi/Desktop/cpbox_kutu/"

class Config():
    def __init__(self,application):
        self.application = application
        self.camera = Camera()
        self.modbus_port = None
        self.light_intensity = LightIntensity()

    def read_config_file(self):
        data = None
        try:
            with open(file_path + "config.json", "r") as jsonfile:
                data = json.load(jsonfile)
                print("Config file readed successful")  
        except Exception as e:
            print("Config file cannot read!: ",e)
        return data
    
    def write_config_to_variables(self,data):
        # infrared
        print(data)
        self.camera.infrared.exposure = int(data["camera"]["infrared"]["exposure"])
        self.camera.infrared.points.left_top_x = int(data["camera"]["infrared"]["points"]["left_top_x"])
        self.camera.infrared.points.left_top_y = int(data["camera"]["infrared"]["points"]["left_top_y"])
        self.camera.infrared.points.left_bottom_x = int(data["camera"]["infrared"]["points"]["left_bottom_x"])
        self.camera.infrared.points.left_bottom_y = int(data["camera"]["infrared"]["points"]["left_bottom_y"])
        self.camera.infrared.points.right_top_x = int(data["camera"]["infrared"]["points"]["right_top_x"])
        self.camera.infrared.points.right_top_y = int(data["camera"]["infrared"]["points"]["right_top_y"])
        self.camera.infrared.points.right_bottom_x = int(data["camera"]["infrared"]["points"]["right_bottom_x"])
        self.camera.infrared.points.right_bottom_y = int(data["camera"]["infrared"]["points"]["right_bottom_y"])
        self.camera.infrared.resolution = int(data["camera"]["infrared"]["resolution"])
        self.camera.infrared.rotation_clockwise_counter = int(data["camera"]["infrared"]["rotation_clockwise_counter"])
        print(float(data["camera"]["infrared"]["threshold"]))
        self.camera.infrared.threshold = float(data["camera"]["infrared"]["threshold"])
        # colourful
        self.camera.colourful.exposure = int(data["camera"]["colourful"]["exposure"])
        self.camera.colourful.points.left_top_x = int(data["camera"]["colourful"]["points"]["left_top_x"])
        self.camera.colourful.points.left_top_y = int(data["camera"]["colourful"]["points"]["left_top_y"])
        self.camera.colourful.points.left_bottom_x = int(data["camera"]["colourful"]["points"]["left_bottom_x"])
        self.camera.colourful.points.left_bottom_y = int(data["camera"]["colourful"]["points"]["left_bottom_y"])
        self.camera.colourful.points.right_top_x = int(data["camera"]["colourful"]["points"]["right_top_x"])
        self.camera.colourful.points.right_top_y = int(data["camera"]["colourful"]["points"]["right_top_y"])
        self.camera.colourful.points.right_bottom_x = int(data["camera"]["colourful"]["points"]["right_bottom_x"])
        self.camera.colourful.points.right_bottom_y = int(data["camera"]["colourful"]["points"]["right_bottom_y"])
        self.camera.colourful.resolution = int(data["camera"]["colourful"]["resolution"])
        self.camera.colourful.rotation_clockwise_counter = int(data["camera"]["colourful"]["rotation_clockwise_counter"])
        self.camera.colourful.threshold = float(data["camera"]["colourful"]["threshold"])
        # modbus port
        self.modbus_port = data["modbus"]["port"]
        # light intensity
        self.light_intensity.white = int(data["light_intensity"]["white"])
        self.light_intensity.blue = int(data["light_intensity"]["blue"])
        self.light_intensity.IR = int(data["light_intensity"]["IR"])

class Camera():
    def __init__(self) -> None:
        self.infrared = Image()
        self.colourful = Image()

class LightIntensity():
    def __init__(self) -> None:
        self.white = None
        self.blue = None
        self.IR = None

class Image():
    def __init__(self) -> None:
        self.points = Points()
        self.exposure = None
        self.resolution = None
        self.rotation_clockwise_counter = None
        self.threshold = None


class Points():
    def __init__(self) -> None:
        self.left_top_x = None
        self.left_top_y = None

        self.left_bottom_x = None
        self.left_bottom_y = None

        self.right_top_x = None
        self.right_top_y = None

        self.right_bottom_x = None
        self.right_bottom_y = None








        