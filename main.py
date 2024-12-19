from classes import ImageHandler, ImageProcessor

if __name__ == "__main__":
    handler = ImageHandler("image.jpg")
    handler.load_image()
    handler.create_thumbnail()
    handler.save_thumbnail("new photo.jpg")

    processor = ImageProcessor(handler.get_image())
    processor.apply_contour()
    processor.add_text("Вариант 3")
    processor.save_image("new photo2.jpg")
