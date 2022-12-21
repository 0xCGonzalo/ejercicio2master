#Lo primero es importar todas las librerias a utilizar
from pathlib import Path
import pyqrcode
import pyotp
import webbrowser

# Luego se definen los colores
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Aca configuro el banner del script para un correcto entendimiento
print("")
print (bcolors.WARNING +  "====== Gonzalo Carrasco ======" + bcolors.ENDC)
print("")
print(bcolors.OKGREEN + "Generador y Validador de OTP con QR Master (Ejercicio2)")
print("")
print("Una vez que se corre el script, se abrira el navegador por defecto. Debe escanearse la imagen generada con el nombre de 'qr_a_escanear_para_OTP.svg'." + bcolors.ENDC)
print("")

# Comenzando con la logica del script, primero que nada se genera una secret key para el usuario con pyotp
aSecreto = pyotp.random_base32()

# Despues se genera el URI TOTP utilizando la secret key del usuario
totp_uri = pyotp.totp.TOTP(aSecreto).provisioning_uri("cgonzalo@campusciberseguridad.com", issuer_name="Ejercicio2App")

# Luego se genera el codigo QR con qr_code
qr_code = pyqrcode.create(totp_uri)

# A continuacion se guarda el fichero QR, como SVG para ocupar menos espacio en disco
qr_code.svg("qr_a_escanear_para_OTP.svg", scale=8)

# Luego se define la ruta del fichero
print(bcolors.OKCYAN + "El codigo QR generado se encuentra en el directorio:" + bcolors.ENDC , Path.cwd())
print("")

# Se abre el archivo con el navegador por default
webbrowser.open("qr_a_escanear_para_OTP.svg")

# Despues se crea un objeto TOTP utilizando la secre key del usuario definida anteriormente
totp = pyotp.TOTP(aSecreto)

# Luego se crea un objeto TOTP con la secret key anterior
totp = pyotp.TOTP(aSecreto)

# Posterioremente se inicializa una variable para controlar el bucle de error cuando el otp no es correcto
otp_is_valid = False

# Se defin el bucle para cuando el OTP sea incorrecto
while not otp_is_valid:
    # Se le pide al usuario que ingrese el codigo OTP
    otp = input("Ingrese el codigo OTP: ")

    # Se valida el OTP ingresado
    otp_is_valid = totp.verify(otp)
    if otp_is_valid:
        print("El codigo OTP es valido")
    else:
        print("El codigo OTP es invalido, por favor ingreselo nuevamente")
                                                                           
