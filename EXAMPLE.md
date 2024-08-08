### Collage Application Explanation

The collage application is a Python program designed to create visually appealing image collages from a collection of images stored in a specified folder. It utilizes the Pillow library for image processing and supports various image formats, including HEIC, which it can convert to JPEG for compatibility.

#### Key Features

1. **Image Collection**:
   - The app scans a designated folder for image files, filtering by common formats such as PNG, JPG, JPEG, GIF, BMP, and HEIC.
   - Converts HEIC images to JPG for compatibility using the `convert_heic_to_jpg` function.

2. **Dynamic Layout**:
   - The collage layout adapts based on the number of images, arranging them in either a 2x2 or 3x3 grid to maximize space and visual appeal.
   - For 4 or fewer images, it uses a 2x2 layout.
   - For 5 to 6 images, it uses a 3x2 layout.
   - For more than 6 images, it uses a 3x3 layout.

3. **Customizable Size and Borders**:
   - Users can specify the base size of images, scaling factors, and frame widths, allowing for personalized collage dimensions.
   - **Base Image Size**: Sets the initial size for each image in the collage before scaling.
   - **Scale Factor**: Multiplies the base image size to determine the final size of each image in the collage.
   - **Frame Width**: Determines the width of the decorative frame around the collage and the spacing between images.

4. **Calculating Collage Width and Height**:
   - The width and height of the collage are calculated to include the space occupied by the images and the frame around the edges.
   - **Collage Width**: 
     $$
     \text{collage\_width} = \text{cols} \times \text{image\_size} + 2 \times \text{frame\_width}
     $$
     - This ensures that the collage width includes the total width of all columns of images plus the frame on both sides.
   - **Collage Height**:
     $$
     \text{collage\_height} = \text{rows} \times \text{image\_size}[1] + 2 \times \text{frame\_width}
     $$
     - This ensures that the collage height includes the total height of all rows of images plus the frame on the top and bottom.

5. **Creating the Collage Canvas**:
   - A new blank image for the collage is created with a white background, using the calculated width and height.

6. **Pasting Images into the Collage**:
   - Images are opened, resized, and pasted into the correct positions on the collage canvas.
   - The position of each image is calculated based on its row and column in the grid layout.

7. **Adding Decorative Frame**:
   - Optionally, a decorative flower frame can be added around the collage by pasting flower images along the edges.

8. **Saving and Displaying the Collage**:
   - The final collage image is saved to the specified output path and displayed to the user.

9. **Output Information**:
   - The application prints information about the created collage, including the number of images, layout, and size.

### Summary
This collage application simplifies the process of creating collages, making it accessible for users looking to compile and showcase their images in a creative format. It dynamically arranges images in a grid layout, supports various image formats, and allows for customization of image sizes and borders. The final collage is saved and displayed, providing immediate visual feedback.

