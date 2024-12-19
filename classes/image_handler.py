from PIL import Image

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None

    def load_image(self):
        self.image = Image.open(self.image_path)
        return self.image

    def save_image(self, save_path):
        if self.image:
            self.image.save(save_path)
        else:
            print("Изображение не загружено")

    def create_thumbnail(self, max_size=(200, 200)):
        if self.image:
            self.image.thumbnail(max_size)
        else:
            print("Изображение не загружено")

    def save_thumbnail(self, save_path):
        if self.image:
            thumbnail = self.image.copy()
            thumbnail.thumbnail((200, 200))
            thumbnail.save(save_path)
        else:
            print("Изображение не загружено")

    def get_image(self):
        return self.image
