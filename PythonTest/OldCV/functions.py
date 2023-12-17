import pyautogui
import PIL
from PIL import Image, ImageFilter
import time
import json
import os


def read_screen(last_value):
    time.sleep(1)
    screenshot = pyautogui.screenshot(region=(1880,506, 35, 32))
    screenshot.save("temp_image.png")
    image = Image.open("temp_image.png")
    width, height = int(image.size[0]), int(image.size[1])

    # Process every pixel

    for y in range(height):
        for x in range(width):
            current_color = image.getpixel( (x,y) )
            if current_color != (255, 85, 85):
                image.putpixel((x,y), (0, 0, 0))
            else:
                image.putpixel((x,y), (255, 255, 255))

    image.save("temp_image.png")

    img_left = image.crop((0, 5, 17, 28))
    img_right = image.crop((18, 5, 35, 28))

    img_left.save("temp_imageLegt.png")
    img_right.save("temp_imageRight.png")

    number = read_image(img_right, img_left, last_value)
    image.close()
    img_left.close()
    img_right.close()

    os.remove("temp_imageRight.png")
    os.remove("temp_imageLegt.png")
    os.remove("temp_image.png")

    print(number)
    return number

def read_segment(image):
    with open('data.json') as f:
        data = json.load(f)

    for number in range(10):
        image_data = list(image.getdata())
        image_data = [list(seg) for seg in image_data]
        saved_data = data[str(number)]

        if saved_data == image_data:
            return str(number)
    return ""


def read_image(image_r, image_l, last_value):
    left_num = read_segment(image_l)
    right_num = read_segment(image_r)

    text = left_num + right_num
    
    if not verify_text(text):
        return last_value
    
    return int(text)

def verify_text(text):
    try:
        text = int(text.replace("&",""))
        text/10
        return True
    except ValueError:
        return False
    else:
        return False
if __name__ == "__main__":
    read_screen(100)