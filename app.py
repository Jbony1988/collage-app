from PIL import Image
import os

def create_collage(image_paths, output_path, collage_size=(200, 200), layout=None):
    # Define the custom layout
    if layout is None:
        layout = [
            [(400, 400)],
            [(400, 400)],
        ]

    # Calculate the total width and height of the collage
    collage_width = sum(size[0] for row in layout for size in row)
    collage_height = max(sum(size[1] for size in row) for row in layout)

    # Create a new image for the collage
    collage = Image.new('RGBA', (collage_width, collage_height), (255, 255, 255, 255))

    # Filter and sort existing images
    existing_images = [path for path in image_paths if os.path.isfile(path)]
    existing_images.sort()

    # Iterate over the custom layout
    x_offset = 0
    image_index = 0
    for row in layout:
        y_offset = 0
        for size in row:
            if image_index < len(existing_images):
                # Open the image and resize it
                image_path = existing_images[image_index]
                image = Image.open(image_path)
                image = image.resize(size, resample=Image.BICUBIC)
                image = image.convert('RGBA')

                # Paste the image into the collage
                collage.paste(image, (x_offset, y_offset), image)
                image_index += 1
            else:
                # If we've run out of images, fill the space with a blank image
                blank = Image.new('RGBA', size, (255, 255, 255, 0))
                collage.paste(blank, (x_offset, y_offset), blank)

            # Update the y-offset for the next image in the row
            y_offset += size[1]
        
        # Update the x-offset for the next row
        x_offset += sum(size[0] for size in row)

    # Save the collage
    collage.save(output_path)
    collage.show()

# Example usage
image_paths = ['thayna-01.jpeg', 'thayna-02.jpeg']
create_collage(image_paths, 'collage_with_overlays.png')