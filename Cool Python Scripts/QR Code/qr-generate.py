# Install qrcode for generating the qr code
# pip install qrcode

import qrcode

filename = 'QRtest.png'
data = 'pyGuru python'
img = qrcode.make(data)
img.save(filename)