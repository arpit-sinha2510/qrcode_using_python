import qrcode
from PIL import Image as img

qr=qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_H,box_size=10,border=4,) #QRCode used to remove errors
qr.add_data("https://web-resume-ecru.vercel.app/")
qr.make(fit=True)
img=qr.make_image(fill_color="navy",back_color="white")
img.save("scan_qr.png")
