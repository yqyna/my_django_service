# -*- coding: utf-8 -*-
import base64
import os
import io
import random

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class RandomChar(object):

    @staticmethod
    def unicode():
        cn_characters = "123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKMLNOPQRSTUVWXYZ"
        chr_length = len(cn_characters) - 1
        return cn_characters[random.randint(0, chr_length)]


class ImageChar(object):

    def __init__(self, font_color=(0, 0, 0),
                 size=(100, 40),
                 font_path=os.path.join(os.path.dirname(__file__), 'TAHOMABD.TTF'),
                 bg_color=(255, 255, 255),
                 font_size=22):
        self.size = size
        self.fontPath = font_path
        self.bgColor = bg_color
        self.fontSize = font_size
        self.fontColor = font_color
        self.font = ImageFont.truetype(
            self.fontPath, self.fontSize, encoding='unic')
        self.image = Image.new('RGB', size, bg_color)

    def rotate(self):
        self.image.rotate(random.randint(0, 30), expand=0)

    def draw_text(self, pos, txt, fill):
        draw = ImageDraw.Draw(self.image)
        draw.text(pos, txt, font=self.font, fill=fill)
        del draw

    def rand_rgb(self, base=0):
        return (random.randint(base, 255),
                random.randint(base, 255),
                random.randint(base, 255))

    def rand_point(self):
        (width, height) = self.size
        return (random.randint(0, width * 2) - width / 2,
                random.randint(0, height * 2) - height / 2)

    def rand_line(self, num):
        draw = ImageDraw.Draw(self.image)
        for i in range(0, num):
            draw.line([self.rand_point(), self.rand_point()],
                      self.rand_rgb(), width=random.randint(0, 3))
        del draw

    def rand_chinese(self, num):
        gap = 3
        start = 1
        uchr = ''
        for i in range(0, num):
            tmpchr = RandomChar().unicode()
            uchr = uchr + tmpchr
            x = start + self.fontSize * i + random.randint(0, gap) + gap * i
            self.draw_text((x, random.randint(-5, 5)), tmpchr, self.rand_rgb())
            self.rotate()
        self.rand_line(18)
        return uchr

    def save(self, path, format=None):
        self.image.save(path, format=format)


def gen_img_captcha():
    ic = ImageChar(font_color=(100, 211, 90))
    uchr = ic.rand_chinese(4)
    stream = io.BytesIO()
    ic.save(stream, format='png')
    stream.seek(0)
    return uchr, str(base64.b64encode(stream.getvalue())).replace("b'", "").replace("'", "")


if __name__ == '__main__':
    print(gen_img_captcha())
    code, data = gen_img_captcha()
    st = "data:image/png;base64," + data
    print(code, st)
