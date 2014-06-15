"""生成二维码

"""
from qrcode import *

qr = QRCode(version=1, error_correction=ERROR_CORRECT_L)
qr.add_data("hello world")
qr.make()

img = qr.make_image()
img.save('test.png')


