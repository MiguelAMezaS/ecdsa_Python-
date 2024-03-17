# ecdsa_Python-
## Si no se tiene instalada en python la libreria edcsa va a dar error al ejecutar el archivo "ecdsa_01.py"

-Utilizando la biblioteca ecdsa en Python para generar y utilizar claves de firma digital basadas en curvas elípticas (ECDSA, por sus siglas en inglés).
Supongamos que se tiene una clave privada y se quiere generar una firma digital utilizando ECDSA. Se puede utilizar una biblioteca o una implementación específica del algoritmo ECDSA en el lenguaje de programación de tu elección, en este ejemplo utilice python.

-Si solo se quisiera ver la validación de la firma si da como resultado "true" o "false", se debería dejar solamente la línea 35, los demás "print" se puede comentar o borrar.

-En la línea 26 también se puede comentar o borrar el withopen directamente solo en caso de querer saber la validación y nada más.

-En el "with open" se puede ver que esta la ruta donde quiero que se guarde el archivo txt a modo de ejemplo, esa ruta se puede modificar para guardar en la ubicación que se prefiera o borrarla y dejar solamente el archivo txt y el modo "w" o el modo que se requiera, en este caso de borrar la ruta el archivo generado generalmente se termina guardando en el "inicio" del explorador ya que no tiene una ubicación especifica, en otros casos se guarda en la misma ubicación que se encuentra el script.

-En claves_generadas.txt se puede ver lo que se generaria al ejecutar edcsa_01.py

En "message" también se puede modificar el mensaje por el que uno quiera.

A modo de aclaración: '08b' es una cadena de formato que se pasa como argumento a la función format(). Aquí, '08b' significa lo siguiente:

0: Rellena con ceros a la izquierda si el número binario tiene menos de 8 dígitos.
8: Especifica que el número binario debe tener una longitud de 8 dígitos.
b: Indica que el número debe ser representado en formato binario.

## If you do not have the edcsa library installed in Python, you will get an error when executing the file "ecdsa_01.py".

-Using the ecdsa library in Python to generate and use elliptic curve based digital signature keys (ECDSA).
Suppose you have a private key and want to generate a digital signature using ECDSA. You can use a library or a specific implementation of the ECDSA algorithm in the programming language of your choice, in this example use python.

-If you only want to see the validation of the signature if it results in "true" or "false", you should leave only line 35, the other "print" can be commented out or deleted.

-In line 26 you can also comment or delete the withopen directly only in case you want to know the validation and nothing else.

-In the "with open" you can see the path where I want to save the txt file as an example, this path can be modified to save in the location you prefer or delete it and leave only the txt file and the "w" mode or the mode that is required, in this case of deleting the path the generated file usually ends up saving in the "start" of the browser because it does not have a specific location, in other cases it is saved in the same location that is the script.

-In "generated_keys.txt" you can see what would be generated when executing edcsa_01.py.

In "message" you can also modify the message for the one you want.

For clarification: '08b' is a format string that is passed as an argument to the format() function. Here, '08b' means the following:

0: Fills with leading zeros if the binary number has less than 8 digits.
8: Specifies that the binary number must be 8 digits long.
b: Indicates that the number must be represented in binary format.

## Resultado en la terminal (Result at the terminal)

![Captura de pantalla 2024-03-16 022747](https://github.com/MiguelAMezaS/ecdsa_Python-/assets/95736906/7d3d6ed4-f4bc-42ec-8cad-3f902f906f78)

## Archivo txt generado en el editor de código (txt file generated in the code editor)
![Captura de pantalla 2024-03-16 022802](https://github.com/MiguelAMezaS/ecdsa_Python-/assets/95736906/a84aef4c-1c44-481a-9402-765d7a275e05)

## Ubicación donde se guardo correctamente el archivo (Location where the file was saved correctly)
![Captura de pantalla 2024-03-16 022857](https://github.com/MiguelAMezaS/ecdsa_Python-/assets/95736906/32d51b3e-fed7-44ce-a1cc-b27c8ab92943)

