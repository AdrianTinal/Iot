﻿# evaluacion
﻿# evaluacion
Descripción del Proyecto
Este proyecto tiene como objetivo medir la temperatura ambiente utilizando el sensor interno de la Raspberry Pi Pico W y enviar los datos a ThingSpeak, una plataforma en la nube para almacenamiento y visualización de datos en tiempo real.

La Raspberry se conecta a una red Wi-Fi, toma lecturas de temperatura a intervalos de tiempo definidos y las envía a ThingSpeak, donde los datos pueden ser analizados y graficados. Esta implementación es una aplicación práctica del Internet de las Cosas (IoT), permitiendo el monitoreo remoto de temperatura sin necesidad de intervención manual.
Instrucciones de Instalación
1. Requisitos Previos
Antes de comenzar, asegúrate de contar con lo siguiente:

Hardware:

Raspberry Pi Pico W
Cable micro USB
Conexión a Internet (Wi-Fi)
oftware:

MicroPython instalado en la Raspberry Pi Pico W
Thonny IDE (o cualquier otro entorno compatible con MicroPython)
Librerías network, urequests, utime, y machine (ya incluidas en MicroPython)
Cuenta en ThingSpeak con una clave de API
2. Configuración del Entorno
1️instalar MicroPython en la Raspberry Pi Pico W:

Descarga MicroPython desde el sitio oficial.
Usa Thonny IDE para cargar MicroPython en la Raspberry.
2️ Configurar la Raspberry Pi Pico W en Thonny:

Conecta la Raspberry a tu PC con un cable micro USB.
Abre Thonny IDE, selecciona en "Interprete": MicroPython (Raspberry Pi Pico).
Prueba con el siguiente código para verificar la conexión:
python
Copiar
Editar
import os
print(os.uname())
Si todo está bien, verás la información del sistema.
3️ Obtener una Clave de API en ThingSpeak:

Crea una cuenta en ThingSpeak.
Crea un nuevo canal y habilita al menos un "Field" (campo).
Copia la clave de API para usarla en el código.
3. Instalación del Código en la Raspberry Pi Pico W
1️ Descarga el código documentado y guárdalo en la Raspberry como main.py.
2️ Modifica las credenciales Wi-Fi y la clave de API:
Abre el archivo main.py y edita estas líneas con tu información:
SSID = "Tu_RED_WIFI"
PASSWORD = "Tu_CONTRASEÑA"
THINGSPEAK_API_KEY = "Tu_API_KEY"
3️ Guarda los cambios y ejecuta el código:

Presiona el botón "Ejecutar" en Thonny IDE para iniciar el monitoreo.

Instrucciones de Uso
Encender la Raspberry Pi Pico W

Conéctala a una fuente de alimentación USB.
Verificar la conexión a Wi-Fi

Si la conexión es exitosa, se mostrará en la consola la IP asignada.
Monitoreo de Temperatura

Cada 180 segundos, la Raspberry tomará una nueva lectura de temperatura y la enviará a ThingSpeak.
Visualización de Datos

Entra a tu canal de ThingSpeak y observa el gráfico de temperatura en tiempo real.
Posibles Ajustes

Puedes modificar el intervalo de medición cambiando utime.sleep(180) en el código.
Si el sensor da valores inesperados, revisa la fórmula de conversión en la función leer_temperatura().
