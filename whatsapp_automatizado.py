import pywhatkit as kit
import time
import pandas as pd

# Carrega os contatos do arquivo Excel
df = pd.read_excel('tus_contactos.xlsx')  

# Mensaje que deseas enviar
msj = df.iloc[0,2] # <- se for uma mensagem unica no arquivo


mensaje = "Hola {nombre}, " + msj #<- pode sustituir msj por uma mensage so

# Obtener la hora y minutos actuales
hora_actual = time.localtime()
hora = hora_actual.tm_hour
minutos = hora_actual.tm_min + 1  # Agregar 1 minuto a la hora actual

# Enviar mensajes a cada contacto
for index, row in df.iterrows():
    nombre = row['Nombre']  #<- Nome da columna na no arquivo Excel
    numero = row['Numero']  #<- Nome da columna na no arquivo Excel
   # msj = row['Mensaje'] #<- So se vc quere enviar uma mensaje personalizado para cada
   # mensaje = f"Hola {nombre}, {msj}" #<-So se vc quere enviar uma mensaje personalizado para cada
    kit.sendwhatmsg(f"+{numero}", mensaje.format(nombre=nombre), hora, minutos)
    minutos += 1

print("Mensajes enviados correctamente.")
