import filters
import image_io

image_matrix = image_io.read_file("images/shrek1.jpg")
grayscale_matrix = filters.grayscale(image_matrix)
image_io.write_to_file("/home/oluwatosin/csci_100/lab_9/outputs/shrek1_image.png", grayscale_matrix)

image_matrix2 = image_io.read_file("images/shrek2.jpg")
reds_matrix = filters.red_stripes(image_matrix2)
image_io.write_to_file("/home/oluwatosin/csci_100/lab_9/outputs/shrek2_image.png", reds_matrix)

image_matrix3 = image_io.read_file("images/shrek3.jpg")
invert = filters.invert_colors(image_matrix3)
image_io.write_to_file("/home/oluwatosin/csci_100/lab_9/outputs/shrek3_image.png", invert)

image_matrix4 = image_io.read_file("images/shrek4.jpg")
flip = filters.flip(image_matrix4)
image_io.write_to_file("/home/oluwatosin/csci_100/lab_9/outputs/shrek4_image.png", flip)

image_matrix5 = image_io.read_file("images/shrek5.jpg")
sepia = filters.sepia(image_matrix5)
image_io.write_to_file("/home/oluwatosin/csci_100/lab_9/outputs/shrek5_image.png", sepia)

image_matrix6= image_io.read_file("images/shrek6.jpg")
threshold = filters.threshold(image_matrix6)
image_io.write_to_file("/home/oluwatosin/csci_100/lab_9/outputs/shrek6_image.png", threshold)

image_matrix7= image_io.read_file("images/shrek7.jpg")
blur = filters.blur(image_matrix7)
image_io.write_to_file("/home/oluwatosin/csci_100/lab_9/outputs/shrek7_image.png", blur)