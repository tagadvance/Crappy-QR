import qrcode

from CrappyImage import CrappyImage

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    # must match font size
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

image = qr.make_image(back_color='white', fill_color='brown', image_factory=CrappyImage)
image.save('/tmp/qr-test.jpeg', 'PNG')