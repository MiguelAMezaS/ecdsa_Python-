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

## Resultado en la terminal

![Captura de pantalla 2024-03-16 022747](https://github.com/MiguelAMezaS/ecdsa_Python-/assets/95736906/7d3d6ed4-f4bc-42ec-8cad-3f902f906f78)
