from datamodule.trainingData import TrainingData

class PrepareTrainingData():
    def __init__(self, params: list[tuple]):
        self.__params = params

    def Data(self) -> TrainingData:
        result = TrainingData()

        #popler pdf to image
        result.pplDpi = self.__params[0]
        result.pplTransparent = self.__params[1]
        result.pplGrayscale = self.__params[2]

        #openCV
        result.cvEqualizeHist = self.__params[3]
        result.cvNormalize = self.__params[4]

        #tesseract
        result.tssDpi = self.__params[5]
        result.tssOem = self.__params[6]
        result.tssPsm = self.__params[7]

        return result