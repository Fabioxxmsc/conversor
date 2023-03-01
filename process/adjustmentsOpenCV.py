import cv2 as cv
import numpy as np
from datamodule.dataInfo import DataInfo
from PIL import Image

class AdjustmentsOpenCV():
    def __init__(self):
        pass

    def Convert(self, item: DataInfo):
        for img in item.listImage:
            self.__Execute(img)

    def __Execute(self, img: Image.Image):        
        img_array = np.array(img)
        img_opencv = cv.cvtColor(img_array, cv.COLOR_RGB2BGR)
        img_gray = cv.cvtColor(img_opencv, cv.COLOR_BGR2GRAY)
        img_equalized = cv.equalizeHist(img_gray)
        img_bgr_equalized = cv.cvtColor(img_equalized, cv.COLOR_GRAY2BGR)
        img = Image.fromarray(img_bgr_equalized)