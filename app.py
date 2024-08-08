from PIL import Image, ImageDraw
import os
import math
from pillow_heif import register_heif_opener

# Register HEIF opener
register_heif_opener()

def convert_heic_to_jpg(heic_path):
    image = Image.open(heic_path)
    jpg_path = os.path.splitext(heic_path)[0] + '.jpg'
    image.save(jpg_path, 'JPEG')
    return jpg_path

def create_collage(folder_path, output_path, base_image_size=(400, 400), scale_factor=2, border_width=10):
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.heic')
    image_paths = set()

    for f in os.listdir(folder_path):
        if f.lower().endswith(image_extensions) and os.path.isfile(os.path.join(folder_path, f)):
            file_path = os.path.join(folder_path, f)
            if f.lower().endswith('.heic'):
                file_path = convert_heic_to_jpg(file_path)
            image_paths.add(file_path)

    image_paths = sorted(list(image_paths))
    num_images = len(image_paths)

    # Calculate layout
    if num_images <= 4:
        cols, rows = 2, 2
    else:
        cols, rows = 3, 3

    # Limit the number of images to 9
    num_images = min(num_images, cols * rows)

    # Calculate scaled image size and collage size
    image_size = (base_image_size[0] * scale_factor, base_image_size[1] * scale_factor)
    collage_width = cols * image_size[0] + (cols + 1) * border_width
    collage_height = rows * image_size[1] + (rows + 1) * border_width

    # Create a new image for the collage with white background
    collage = Image.new('RGB', (collage_width, collage_height), (255, 255, 255))

    # Paste images into the collage
    for index, image_path in enumerate(image_paths[:num_images]):
        row = index // cols
        col = index % cols
        image = Image.open(image_path)
        image = image.resize(image_size, resample=Image.BICUBIC)
        x_offset = col * (image_size[0] + border_width) + border_width
        y_offset = row * (image_size[1] + border_width) + border_width
        collage.paste(image, (x_offset, y_offset))

    # Draw red border around the collage
    draw = ImageDraw.Draw(collage)
    draw.rectangle([(0, 0), (collage_width - 1, collage_height - 1)], outline="red", width=border_width)

    # Save the collage
    collage.save(output_path)
    collage.show()

    print(f"Collage created with {num_images} images.")
    print(f"Layout: {cols}x{rows}")
    print(f"Collage size: {collage.size}")

# Example usage
folder_path = os.getcwd()  # Use the current working directory
create_collage(folder_path, 'flexible_collage.png', scale_factor=2, border_width=20)