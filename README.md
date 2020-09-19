ALPR-(Automatic India Car License Reader )

important modules:
    opencv
    numpy
    pillow
    pytesseract

Important files:

    Tesseract-OCR


if you are getting any problem in pytesseract then add the below code in the file at the time of package imports

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
