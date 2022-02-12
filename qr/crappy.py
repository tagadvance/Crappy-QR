#!/usr/bin/env python3

import argparse
import qrcode
import sys

from CrappyImage import CrappyImage

parser = argparse.ArgumentParser(description='Generate a crappy QR code')
parser.add_argument('--data', nargs='?', default=sys.stdin, help='the input data')
parser.add_argument('--out', nargs='?', default=sys.stdout, help='the output file')
args = parser.parse_args()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    # must match font size
    box_size=10,
    border=4,
)
qr.add_data(args.data)
qr.make(fit=True)

image = qr.make_image(back_color='white', fill_color='brown', image_factory=CrappyImage)
image.save(args.out, 'PNG')
