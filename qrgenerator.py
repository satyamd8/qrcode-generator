import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from tkinter import Tk, Label, Entry, Button, messagebox, PhotoImage
from PIL import Image, ImageTk

def createQR(urlInput, output="qrcode.png"):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=15,
            border=8,
        )
        qr.add_data(urlInput)
        qr.make(fit=True)

        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer(),
            color_mask=RadialGradiantColorMask(edge_color=(123, 43, 132), center_color=(67, 71, 96))
        )
        img.save(output)
        return output
    except Exception as e:
        raise ValueError(f"Error generating QR Code: {e}")

def generate_qr():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return

    try:
        output_path = createQR(url)
        display_qr(output_path)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def display_qr(image_path):
    img = Image.open(image_path)
    img = img.resize((300, 300))  # Resize for display
    qr_img = ImageTk.PhotoImage(img)
    qr_label.config(image=qr_img)
    qr_label.image = qr_img  # Keep a reference to prevent garbage collection

# Create the GUI
root = Tk()
root.title("QR Code Generator")
root.geometry("400x500")

icon = PhotoImage(file='image.png')
root.iconphoto(True, icon)

Label(root, text="Enter URL:", font=("Calibri", 14)).pack(pady=10)
url_entry = Entry(root, font=("Arial", 12), width=30)
url_entry.pack(pady=5)

Button(root, text="Generate QR Code", font=("Calibri", 12, "bold"), command=generate_qr).pack(pady=20)

qr_label = Label(root, text="QR Code will appear here", font=("Arial", 12))
qr_label.pack(pady=20)


root.mainloop()
