import sys

from super_image import MsrnModel, ImageLoader
from PIL import Image


model = MsrnModel.from_pretrained('eugenesiow/msrn', scale=2)


def usage() -> None:
    print("Usage:\n\timage_upscaler <file_name>", file=sys.stderr)
    sys.exit(1)


def upscale(image_name: str) -> None:
    index = image_name.rfind(".")
    if index < 0:
        usage()
    target_name = image_name[:index] + "_2x.png"

    print(f"Processing {image_name}")
    image = ImageLoader.load_image(Image.open(image_name))
    ImageLoader.save_image(model(image), target_name)
    print(f"Saved {target_name}")


if __name__ == '__main__':
    # if len(sys.argv) != 2:
    #     usage()
    # upscale(sys.argv[1])
    #upscale("/Users/ericthiebaut-george/Downloads/Liam1x1k.png")
    pass
