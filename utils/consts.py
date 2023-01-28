CLASSE_VALOR_DATA = 1
CLASSE_VALOR_INSCRICAO = 2
CLASSE_VALOR_VALOR = 3

#https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc

#Tesseract PSM
TSS_PSM_00 = 0  # Orientation and script detection (OSD) only.
TSS_PSM_01 = 1  # Automatic page segmentation with OSD.
TSS_PSM_02 = 2  # Automatic page segmentation, but no OSD, or OCR. (not implemented)
TSS_PSM_03 = 3  # Fully automatic page segmentation, but no OSD. (Default)
TSS_PSM_04 = 4  # Assume a single column of text of variable sizes.
TSS_PSM_05 = 5  # Assume a single uniform block of vertically aligned text.
TSS_PSM_06 = 6  # Assume a single uniform block of text.
TSS_PSM_07 = 7  # Treat the image as a single text line.
TSS_PSM_08 = 8  # Treat the image as a single word.
TSS_PSM_09 = 9  # Treat the image as a single word in a circle.
TSS_PSM_10 = 10 # Treat the image as a single character.
TSS_PSM_11 = 11 # Sparse text. Find as much text as possible in no particular order.
TSS_PSM_12 = 12 # Sparse text with OSD.
TSS_PSM_13 = 13 # Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.

#Tesseract OEM
TSS_OEM_00 = 0  # Original Tesseract only.
TSS_OEM_01 = 1  # Neural nets LSTM only.
TSS_OEM_02 = 2  # Tesseract + LSTM.
TSS_OEM_03 = 3  # Default, based on what is available.