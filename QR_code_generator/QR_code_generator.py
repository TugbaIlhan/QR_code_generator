import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_connection = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("quiz_game/qrimg.png")

generate_qrcode("https://www.codewithtomi.com")    