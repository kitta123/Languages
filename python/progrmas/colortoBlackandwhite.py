''' Convert Photo into Color to Black and White '''

from PIL import Image

open_image = Image.open("python.png")
convert_to_bw = open_image.covert("I")
convert_to_bw.show()
