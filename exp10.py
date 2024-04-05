from PIL import Image

# Load the image
image = Image.open("path_to_image.jpg")

# Display the image
image.show()

# Plot the image in console window
image_array = image.load()
for y in range(image.height):
    for x in range(image.width):
        pixel = image_array[x, y]
        # Print the pixel value or perform any other operation

# Display the image size
width, height = image.size
print("Image size: {} x {}".format(width, height))

# Reduce the image size to half
half_width = width // 2
half_height = height // 2
half_size_image = image.resize((half_width, half_height))
half_size_image.show()

# Rotate the image 145 degrees
rotated_image = image.rotate(145)
rotated_image.show()

# Resize the image
resized_image = image.resize((width + 50, height + 70))
resized_image.show()

# Flip the image
flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
flipped_image.show()

# Crop the image
left = 100
top = 100
right = 300
bottom = 300
cropped_image = image.crop((left, top, right, bottom))
cropped_image.show()

# Convert the image to grayscale
grayscale_image = image.convert("L")
grayscale_image.show()

# Convert the image to black and white
bw_image = image.convert("1")
bw_image.show()

# Apply blur effect on the image
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.show()