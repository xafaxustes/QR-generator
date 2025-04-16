import qrcode
from vobject import vCard


# Solicitar datos del contacto
nombre = input("Introduce el nombre completo: ")
telefono = input("Introduce el número de teléfono: ")
correo = input("Introduce el correo electrónico: ")

# Crear la información del contacto
contacto = vCard()
contacto.add('fn').value = nombre
contacto.add('tel').value = telefono
contacto.add('email').value = correo

# Convertir la información del contacto a formato vCard
vcard_str = contacto.serialize()

# Generar el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(vcard_str)
qr.make(fit=True)

# Crear la imagen del código QR
img = qr.make_image(fill='black', back_color='white')

# Guardar la imagen del código QR con el nombre del contacto
nombre_archivo = f"{nombre.replace(' ', '_')}.png"
img.save(nombre_archivo)


print(f"Código QR generado y guardado como '{nombre_archivo}'")
