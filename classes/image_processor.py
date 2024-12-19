from PIL import Image, ImageDraw, ImageFont, ImageFilter

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def apply_contour(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.CONTOUR)
        else:
            print("Изображение не загружено")

    def add_text(self, text, position=None, font="arial.ttf", font_size=20, color=(255, 0, 0)):
        if self.image:
            draw = ImageDraw.Draw(self.image)
            try:
                font = ImageFont.truetype(font, font_size)
            except IOError:
                font = ImageFont.load_default()
            if not position:
                width, height = self.image.size
                text_bbox = draw.textbbox((0, 0), text, font=font)
                text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
                position = ((width - text_width) // 2, (height - text_height) // 2)
            draw.text(position, text, font=font, fill=color)
        else:
            print("Изображение не загружено")

    def save_image(self, save_path):
        if self.image:
            self.image.save(save_path)
        else:
            print("Изображение не загружено")
