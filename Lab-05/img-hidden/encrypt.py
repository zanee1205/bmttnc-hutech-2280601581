import sys
from PIL import Image

def encode_image(image_path, message):
    image = Image.open(image_path)
    width, height = image.size
    pixel_index = 0

    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'

    data_index = 0
    for row in range(height):
        for col in range(width):
            pixel = list(image.getpixel((col, row)))
            
            for color_channel in range(3):
                if data_index < len(binary_message):
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1
                    
            image.putpixel((col, row), tuple(pixel))
            
        if data_index >= len(binary_message):
            break
    
    encoded_image_path = "encoded_image.png"
    image.save(encoded_image_path)
    print("Steganoraphy completed. Encoded image saved as", encoded_image_path)
    
def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return
    
    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)
    
if __name__ == "__main__":
    main()