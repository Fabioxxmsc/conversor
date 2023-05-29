import pytesseract
from pdf2image import exceptions, convert_from_bytes
import itertools
import os
import sys
import colorama
import time

sys.path.append(os.getcwd())
import utils.consts as cst

colorama.init()

pathRaizTesseract = r'C:\Program Files\Tesseract-OCR'
pathTesseractExe = os.path.join(pathRaizTesseract, 'tesseract.exe')
pathTessData = os.path.join(pathRaizTesseract, 'tessdata')

os.environ['TESSDATA_PREFIX'] = pathTessData
pytesseract.pytesseract.tesseract_cmd = pathTesseractExe
lang = 'por'

print('Tesseract OCR version ' + str(pytesseract.get_tesseract_version()))

pdf = r'D:\Workspace\Python\tcc\conversor\test\dataset\1\doc.pdf'
file = open(pdf, 'rb')
binaryDoc = file.read()
file.close()

args = list(itertools.product(cst.ARGS_TESSERACT_OEM, cst.ARGS_TESSERACT_PSM))
print('Args:', len(args))

images = convert_from_bytes(pdf_file=binaryDoc)

errors = ''
countIgnore = 0
countSucess = 0
countError = 0
oem = 0
psm = 1

for img in images:
    for arg in args:
        customConfig = r'--loglevel ALL --dpi 300 --oem {} --psm {}'.format(str(arg[oem]), str(arg[psm]))
        if (arg[oem] in [0, 2]) or (arg[psm] in [0, 2]):
            print(colorama.Fore.CYAN + 'Args ignored\t' + 'lang ' + lang + str(customConfig))
            countIgnore += 1
            continue
        
        try:            
            text_from_image = pytesseract.image_to_string(img, lang=lang, config=customConfig, output_type=pytesseract.Output.STRING)
            if text_from_image != '':
                print(colorama.Fore.GREEN + 'Args sucess\t' + 'lang ' + lang + str(customConfig))
            countSucess += 1
        except (Exception, pytesseract.TesseractError) as e:
            countError += 1
            print(colorama.Fore.RED + 'Args error\t' + 'lang ' + lang + str(customConfig))
            errors += 'Error\t' + 'lang ' + lang + str(customConfig) + str(e) + '\n'
            time.sleep(1)

if errors != '':
    print(colorama.Fore.RED + 'Errors:', errors)
        
print(colorama.Fore.CYAN + 'Count ignored:', countIgnore)
print(colorama.Fore.GREEN + 'Count sucess:', countSucess)
print(colorama.Fore.RED + 'Count errors:', countError)