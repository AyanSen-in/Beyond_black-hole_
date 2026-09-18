# import qrcode as qr

# from PIL import Image 

# image= qr.make(" https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")
# image.save("ayan_youtube.png")

# qr = qr.QRCode(version =1, 
#                 error_correction= qr.constants.ERROR_CORRECT_H,
#                 box_size = 10, border =4,)

# qr.add_data("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")
# qr.add=input("enter your input ")
# qr.make(fit=True)
# image= qr.make_image(fill_colour="RED", black_color="black")
# image.save(f"{qr.add}.png")


# qr.add_data =input(" please ") 
# print (qr.add_data)




# # borderless_qrcode.py

# import segno

# qrcode = segno.make_qr(" Enter what you can do in qr: ")
# qrcode.save(
#     "borderless_qrcode.png",
#     scale=10,
#     border=0,
# )




# import qrcode

# # 1. Get input from the user
# data = input("Enter text or URL to convert to QR code: ")

# # 2. Create the QR code object
# # version=1 creates the smallest 21x21 matrix; auto-adjusts if data is too long
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )

# # 3. Add data and finalize
# qr.add_data(data)
# qr.make(fit=True)

# # 4. Create the image and save it
# img = qr.make_image(fill_color="black", back_color="white")
# img.save("qr_code.png")

# print("QR code saved as qr_code.png")   





# import qrcode
# data = input('QR Code using make() function')

# img = qrcode.make(data)
# img.save('MyQRCode1.png')
















"""
QR Code Generator
-----------------
Run:  python3 qr_generator.py
Then type any text / URL and press Enter.
The QR code is saved as qr_output.png in the same folder.
Scan it with your phone camera to open the link / read the text.
"""

import qrcode
import sys
import os

def make_qr(text: str, filename: str = "qr_output.png") -> str:
    qr = qrcode.QRCode(
        version=None,          # auto-size
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30 % ERROR corrected 
        box_size=5,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    return os.path.abspath(filename)


def main():
    print("#" * 50)
    print("        QR Code Generator")
    print("*~*" *25)

    # Accept text as CLI arg or interactive prompt
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = input("Enter text or URL to encode: ").strip()

    if not text:
        print("Error: no input provided.")
        sys.exit(1)

    path = make_qr(text)
    print(f"\n✅  QR code saved → {path}")
    # print("    Scan it with your phone camera!\n")

    # Also print a mini ASCII preview in the terminal
    qr = qrcode.QRCode(border=1)
    qr.add_data(text)
    qr.make(fit=True)
    print("── Terminal preview ──")
    qr.print_ascii(invert=True)


if __name__ == "__main__":
    main()





























# # animated_qrcode.py

# import segno
# from urllib.request import urlopen

# slts_qrcode = segno.make_qr("https://www.youtube.com/watch?v=hTWKbfoikeg")
# nirvana_url = urlopen("https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif")
# slts_qrcode.to_artistic(
#     background=nirvana_url,
#     target="animated_qrcode.gif",
#     scale=5,
# )























# from tkinter import *
# from tkinter import messagebox
# import os
# import qrcode

# # import pyqrcode
# import smtplib
# # import imghdr
# from email.message import EmailMessage


# my_mail = "ENTER YOUR EMAIL ID"
# password = "SET PASSWORD"
# # create a GUI window with Tkinter
# window = Tk()
# window.title("QR Code Generator APP")
# global email_add


# # a function to generate all widgets
# def generate():
#     if len(Subject.get()) != 0:
#         global qr, photo
#         qr = pyqrcode.create(Subject.get())
#         photo = BitmapImage(data=qr.xbm(scale=8))
#     else:
#         messagebox.showerror("Error", "Enter subject first")
#     try:
#         showcode()
#     except:
#         pass


# # a function to show the qr code on the screen
# def showcode():
#     imageLabel.config(image=photo)
#     subLabel.config(text="QR of " + Subject.get())


# # A function to save the qr code as a png file
# def save():
#     dir = os.getcwd()
#     if not os.path.exists(os.getcwd()):
#         os.makedirs(dir)
#     try:
#         if len(name.get()) != 0:
#             qr.png(os.path.join(dir, name.get() + ".png"), scale=8)
#             messagebox.showinfo("Status", "QR code saved successfully")
#         else:
#             messagebox.showerror("Error", "Enter file name first")
#     except:
#         messagebox.showerror("Error", "Generate the QR code first")


# def send():
#     try:
#         if len(mail.get()) != 0 and os.path.exists(name.get()+".png"):
#             newMessage = EmailMessage()
#             newMessage['Subject'] = "QR CODE IS READY!!"
#             newMessage['From'] = my_mail
#             newMessage['To'] = mail.get()
#             with open(f'{name.get()}.png', 'rb') as f:
#                 image_data = f.read()
#                 image_type = imghdr.what(f.name)
#                 image_name = f.name
#             newMessage.add_attachment(
#                 image_data, maintype='image', subtype=image_type, filename=image_name)
#             with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#                 smtp.login(my_mail, password)
#                 smtp.send_message(newMessage)

#             messagebox.showinfo("Status", "Mail has been sent successfully")
#         else:
#             messagebox.showerror(
#                 "Error", "Invalid Email or QR Code not generated")
#     except:
#         messagebox.showerror("Error", "Invalid Email")


# # specifying all details for the widgets
# Sub = Label(window, text="Enter URL/Subject")
# Sub.grid(row=0, column=0, sticky=N + S + W + E)

# FName = Label(window, text="Enter filename to save as")
# FName.grid(row=1, column=0, sticky=N + S + W + E)

# Mail = Label(window, text="Enter email address")
# Mail.grid(row=2, column=0, sticky=N + S + W + E)

# Subject = StringVar()
# SubEntry = Entry(window, textvariable=Subject)
# SubEntry.grid(row=0, column=1, sticky=N + S + W + E)

# name = StringVar()
# nameEntry = Entry(window, textvariable=name)
# nameEntry.grid(row=1, column=1, sticky=N + S + W + E)

# mail = StringVar()
# mailEntry = Entry(window, textvariable=mail)
# mailEntry.grid(row=2, column=1, sticky=N + S + W + E)

# button = Button(window, text="Generate QR Code", width=15, command=generate)
# button.grid(row=0, column=3, sticky=N + S + W + E)

# imageLabel = Label(window)
# imageLabel.grid(row=4, column=1, sticky=N + S + W + E)

# subLabel = Label(window, text="")
# subLabel.grid(row=3, column=1, sticky=N + S + W + E)

# saveB = Button(window, text="Save as PNG File", width=15, command=save)
# saveB.grid(row=1, column=3, sticky=N + S + W + E)

# sendB = Button(window, text="Send QR code", width=15, command=send)
# sendB.grid(row=2, column=3, sticky=N + S + W + E)

# Rows = 5
# Columns = 5

# for row in range(Rows + 1):
#     window.grid_rowconfigure(row, weight=1)

# for col in range(Columns + 1):
#     window.grid_columnconfigure(col, weight=1)

# # let the program run forever until manually closed by the user
# window.mainloop()