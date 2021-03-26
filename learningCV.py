import cv2

img = 'pixel/20201115-DSC07384.jpg'
# img2 = 'pixel/20160910-DSC06091_before.jpg'
img_grey = cv2.imread(img,0)
# img_grey2 = cv2.imread(img2,0)
# img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

contrast = img_grey.std()
# contrast2 = img_grey2.std()

print(contrast)

# from exif import Image

# with open(img2, "rb") as palm_1_file:
#     palm_1_image = Image(palm_1_file)
#     print(palm_1_image)
    
# images = [palm_1_image]

# for index, image in enumerate(images):
#     if image.has_exif:
#         status = f"contains EXIF (version {image.exif_version}) information."
#     else:
#         status = "does not contain any EXIF information."
#     print(f"Image {index} {status}")

