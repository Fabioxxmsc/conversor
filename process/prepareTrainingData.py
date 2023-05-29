from datamodule.trainingData import TrainingData

class PrepareTrainingData():
    __params: list[tuple] = None

    def __init__(self, params: list[tuple]):
        self.__params = params

    def Data(self) -> TrainingData:
        result = TrainingData()

        result.idCombination = int(self.__params['idcombinacoes'])

        # Popler pdf to image
        result.pplDpi = int(self.__params['ppldpi'])
        result.pplTransparent = self.__params['ppltransparent'] in ['True', 'true', '1']
        result.pplGrayscale = self.__params['pplgrayscale'] in ['True', 'true', '1']

        # OpenCV
        result.cvEqualizeHist = self.__params['cvequalizehist'] in ['True', 'true', '1']
        result.cvNormalize = self.__params['cvnormalize'] in ['True', 'true', '1']

        # Tesseract-OCR
        result.tssDpi = int(self.__params['tssdpi'])
        result.tssOem = int(self.__params['tssoem'])
        result.tssPsm = int(self.__params['tsspsm'])

        return result