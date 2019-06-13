from qrcode.image.pil import PilImage
from PIL import ImageFont

class CrappyImage(PilImage):

    def drawrect(self, row, col):
        box = self.pixel_box(row, col)
        font = ImageFont.truetype('fonts/noto-emoji/NotoEmoji-Regular.ttf', 10)
        self._idr.text(box[0], u"\U0001F4A9", font=font, fill=self.fill_color)