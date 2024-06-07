# %% [markdown]
# # Image compression

# %%
from PIL import Image
import numpy as np
import images
from imageai.Detection import ObjectDetection

# %%
basic_colors = [
    (255, 255, 255),  # white
    (0, 0, 0),        # black
    (255, 0, 0),      # red
    (0, 255, 0),      # green
    (0, 0, 255),      # blue
    (255, 255, 0),    # yellow
    (255, 0, 255),    # magenta
    (0, 255, 255)     # cyan
]

def rgb2hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def rle_encode(image):
    img = Image.open(image).convert('RGB')
    pixels = list(img.getdata())

    imagename = image.rsplit('.',1)[0]

    output_file = f'{imagename}.txt'

    encoded_data = []

    count = 1

    prev_pixel = rgb2hex(*pixels[0])

    for current_pixel in pixels[1:]:
        current_pixel_hex = rgb2hex(*current_pixel)

        if current_pixel_hex == prev_pixel:
            count += 1
        else:
            encoded_data.append(f'{prev_pixel}{count}')
            count = 1
            prev_pixel = current_pixel_hex
    encoded_data.append(f'{prev_pixel}{count}')

    with open(output_file,'w') as file:
        file.write('\n'.join(encoded_data))
    print(f'{output_file} created')

def color_distance(color1, color2):
    return np.linalg.norm(np.array(color1) - np.array(color2))

def closest_color(color):
    return min(basic_colors, key=lambda bc: color_distance(color, bc))

def reduce_colors(image_path):

    output_path = f'new_{image_path}'

    img = Image.open(image_path).convert('RGB')
    pixels = np.array(img)

    reduced_pixels = np.array([[closest_color(pixel) for pixel in row] for row in pixels], dtype=np.uint8)

    reduced_img = Image.fromarray(reduced_pixels)
    reduced_img.save(output_path, 'JPEG')

    print(f'{output_path} created')

def object_detection(image):
    Detector = ObjectDetection()

    Detector.setModelTypeAsTinyYOLOv3()

    Detector.setModelPath("tiny-yolov3.pt")

    Detector.loadModel()
    
    Detections = Detector.detectObjectsFromImage(image, minimum_percentage_probability=30)
    
    if len(Detections) == 0:
            print("No objects found!")

    Detections = reversed(Detections)
    
    Object_Count_Dict = {}

    for object in Detections:

        Object_Name = object["name"]

        if Object_Name in Object_Count_Dict: 

            Object_Count_Dict[Object_Name] +=1

        else:

            Object_Count_Dict[Object_Name] = 1
    
    for name, count in Object_Count_Dict.items():
        print(count, name)


# %%
def main():
    imageName = input().strip().lower()

    try:
        rle_encode(imageName)
        reduce_colors(imageName) 
        object_detection(imageName)
    except:
        print("There went something wrong!")

if __name__ == "__main__":
    main()


