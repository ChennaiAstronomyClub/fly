# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from time import time
import sys
import urllib2
import cStringIO
 
class ISS:
    def __init__(self):
        self.base_image = 'http://www.chennaiastronomyclub.org/img/fly/iss.jpg'
        self.font = 'Arial.ttf'
    
    def fly(self, text):
        text = text.replace('°', ' degrees')
        url = 'http://www.chennaiastronomyclub.org/img/fly/iss.jpg'
        header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'
        }
        req = urllib2.Request(url, headers=header)
        file = cStringIO.StringIO(urllib2.urlopen(req).read())
        img = Image.open(file).convert('RGB')
        watermark = Image.new('RGBA', img.size, (0,0,0,0))
        size = 42
        n_font = ImageFont.truetype(self.font, size)
        draw = ImageDraw.Draw(watermark, 'RGBA')
        x, y = 525, 300
        for line in text.split('<br/>'):
            draw.text((x, y), line.lstrip(), font=n_font)
            y += 55
        alpha = watermark.split()[3]
        out_file = 'iss' + str(int(time())) + '.jpg'
        Image.composite(watermark, img, watermark).save(out_file, 'JPEG')