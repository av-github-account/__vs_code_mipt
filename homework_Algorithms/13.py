from PIL import Image

def build_color_tree(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    color_tree = {}

    for pixel in pixels:
        if pixel in color_tree:
            color_tree[pixel] += 1
        else:
            color_tree[pixel] = 1

    sorted_colors = sorted(color_tree.items(), key=lambda x: x[1], reverse=True)

    for color, count in sorted_colors:
        print(f"Color: {color}, Count: {count}")

image_path = "test.bmp"
build_color_tree(image_path)
