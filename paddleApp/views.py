from django.shortcuts import render
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import os

# Create your views here.
def ocr_detect(filePath:str):
    '''
     orc识别
    '''
    print("filePath is ", filePath)
    ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # need to run only once to download and load model into memory
    result = ocr.ocr(filePath, cls=True)
    result_list = result
    (path,fileName) = os.path.split(filePath)
    image = Image.open(filePath).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='./template/fonts/Deng.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save(os.path.join(path, "draw-" + fileName))
