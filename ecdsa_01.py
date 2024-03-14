from ecdsa import SigningKey, VerifyingKey

# Generar una clave privada
private_key = SigningKey.generate()

# Obtener la clave pública correspondiente
public_key = private_key.get_verifying_key()

#private_key_bytes contiene la clave privada en bytes, luego se usa una comprensión de lista para convertir cada byte en su representación binaria utilizando format(byte, '08b'). 
#Luego, concatenamos todas las representaciones binarias de los bytes utilizando join().
private_key_bytes = private_key.to_string()
private_key_binary = ''.join(format(byte, '08b') for byte in private_key_bytes)

# Mensaje que se desea firmar
message = b'este es un mensaje para firmar'
decoded_message = message.decode() #Al decodificar la cadena de bytes utilizando el metodo decode(), obtendrás una cadena de caracteres que se puede imprimir sin la "b" al principio.

# Firmar el mensaje utilizando la clave privada
signature = private_key.sign(message)

# Verificar la firma utilizando la clave pública
is_valid = public_key.verify(signature, message)

#se crea un archivo llamado "claves_generadas.txt" utilizando la función open() con el modo de escritura ("w"). 
#Luego, se utiliza el método write() para escribir el contenido en el archivo
with open("C:/Users/Miguel/OneDrive/Escritorio/ecdsa_Python-/claves_generadas.txt", "w") as archivo:
    archivo.write("Firma válida: " + str(is_valid) + "\n")
    archivo.write(decoded_message + "\n")
    archivo.write("Clave privada generada: " + private_key.to_string().hex() + "\n")
    archivo.write("Clave privada en bytes: " + str(private_key.to_string()) + "\n")
    archivo.write(private_key_binary)

print("Contenido exportado correctamente en el archivo claves_generadas.txt")

print("Firma válida:", is_valid)
print(decoded_message)
print("Clave privada generada:", private_key.to_string().hex())
print("clave privada en bytes:", private_key.to_string())
print("Clave privada generada en 0 y 1:"+ private_key_binary)