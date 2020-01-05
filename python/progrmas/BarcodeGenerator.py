import barcode
br = barcode.get_barcode_class('ean13')
Br = br('1234567891012')
qr = Br.save('barean13')


import barcode
from barcode.writer import ImageWriter
br = barcode.get_barcode_class('code39')
Br = br('abcdef',writer = ImageWriter())
qr = Br.save('barcode39')
