# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from time import time
import os
 
class ISS:
    def __init__(self):
        self.base_image = 'fly/fly/iss.jpg'
        self.font = 'Arial.ttf'
    
    def fly(self, text):
        text = text.replace('°', ' degrees')
        file = os.path.join(os.getcwd(), self.base_image)
        img = Image.open(file).convert('RGB')
        watermark = Image.new('RGBA', img.size, (0,0,0,0))
        size = 42
        n_font = ImageFont.truetype(self.font, size)
        draw = ImageDraw.Draw(watermark, 'RGBA')
        x, y = 515, 300
        for line in text.split('<br/>'):
            draw.text((x, y), line.lstrip(), font=n_font)
            y += 55
        alpha = watermark.split()[3]
        out_file = 'iss' + str(int(time())) + '.jpg'
        Image.composite(watermark, img, watermark).save(out_file, 'JPEG')
        return out_file
