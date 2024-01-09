import sys
from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def ocr_file(src_image, dest_text_file, write_flag):
    img = Image.open(src_image)
    text = pytesseract.image_to_string(img)
    print(text)
    with open(dest_text_file, write_flag, encoding="utf-8") as text_file:
        text_file.write(text)


def main():
    n = len(sys.argv)
    print(sys.argv)
    if n != 3:
        print("2 arguments only!")
        sys.exit()
    cwd = os.getcwd()
    src_file = os.path.join(cwd, sys.argv[1])
    if not os.path.isfile(src_file):
        print("Source path does not exist: " + src_file)
        sys.exit()
    dst_file = os.path.join(cwd, sys.argv[2])
    if os.path.isfile(dst_file):
        file_write_flag = 'a'
    else:
        file_write_flag = 'w'

    ocr_file(src_file, dst_file, file_write_flag)
    print("Done")



if __name__ == '__main__':
    main()
