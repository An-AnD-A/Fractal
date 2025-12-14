import PIL.Image

ASCII_CHAR = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHAR[pixel // 25] for pixel in pixels])
    return ascii_str

def main(image_path, new_width=100):
    try:
        image = PIL.Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}. {e}")
        return

    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_img = "\n".join([ascii_str[i:(i + img_width)] for i in range(0, len(ascii_str), img_width)])

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)

    print(ascii_img)

    return ascii_img

if __name__ == "__main__":

    main (image_path="/home/weirdonerdo/Downloads/pics/Pic3.jpg", 
          new_width=100)