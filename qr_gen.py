import qrcode
from datetime import datetime
import os

# Folder that saves the qr codes
output_folder = "generated_codes"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    
    full_path = os.path.join(output_folder, filename)
    img.save(full_path)
    print(f"QR Code saved as {full_path}")

if __name__ == "__main__":
    data = input("Enter the text or URL for QR code: ")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"qr_{timestamp}.png"
    
    generate_qr(data, filename)