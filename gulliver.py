def contar(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            contador = {}

            for caracter in contenido:
                if caracter in contador:
                    contador[caracter] +=1
                else:
                    contador [caracter] +=1
            caracteres_order = sorted(contador.items(),key=lambda x:x[1],reverse = true)
            return caracteres_order
    except FileNotFoundError:
        return "Error del archivo"

    archivo = "Gullivers_Travels.txt"
    resultado = contar(archivo)
    print(resultado)