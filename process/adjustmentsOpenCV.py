import cv2 as cv
import numpy as np
from datamodule.dataInfo import DataInfo
from PIL import Image

class AdjustmentsOpenCV():
    def __init__(self):
        pass

    def Convert(self, item: DataInfo):
        for i in range(len(item.listImage)):
            img = item.listImage[i]
            if item.trainingData.cvNormalize:
                img = self.__Normalize(img)

            if item.trainingData.cvEqualizeHist:
                img = self.__Equalize(img)
            item.listImage[i] = img

    def __Normalize(self, img: Image.Image) -> Image.Image:
        img_array = np.array(img)
        img_opencv = cv.cvtColor(img_array, cv.COLOR_RGB2BGR)
        img_normalized = cv.normalize(img_opencv, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
        return Image.fromarray(img_normalized)

    def __Equalize(self, img: Image.Image) -> Image.Image:
        img_array = np.array(img)
        img_opencv = cv.cvtColor(img_array, cv.COLOR_RGB2BGR)
        img_gray = cv.cvtColor(img_opencv, cv.COLOR_BGR2GRAY)
        img_equalized = cv.equalizeHist(img_gray)
        img_bgr_equalized = cv.cvtColor(img_equalized, cv.COLOR_GRAY2BGR)
        img_rgb_equalized = cv.cvtColor(img_bgr_equalized, cv.COLOR_BGR2RGB)
        return Image.fromarray(img_rgb_equalized)