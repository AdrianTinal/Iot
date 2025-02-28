import network       # Librería para manejar la conexión Wi-Fi
import urequests     # Librería para hacer solicitudes HTTP
import utime         # Librería para manejar tiempos y pausas
from machine import ADC  # Importa el módulo ADC para leer valores analógicos

# Configuración de Wi-Fi
SSID = "Alumno"       # Nombre de la red Wi-Fi (SSID)
PASSWORD = "Mebe2ege"      # Contraseña de la red Wi-Fi

# Configuración de ThingSpeak
THINGSPEAK_API_KEY = "5LMNK8CLHEDGGTHS"  # Clave de API para enviar datos
THINGSPEAK_URL = "https://api.thingspeak.com/update"  # URL de actualización

# Configuración del sensor de temperatura interno del RP2040
sensor_temp = ADC(4)  # El sensor de temperatura interno está en el canal ADC 4
VOLTAGE_REFERENCE = 3.3  # Voltaje de referencia del ADC (3.3V)
CONVERSION_FACTOR = VOLTAGE_REFERENCE / 65535  # Factor de conversión ADC → Voltaje

def conectar_wifi():
    """
    Establece la conexión a una red Wi-Fi.
    """
    wlan = network.WLAN(network.STA_IF)  # Activa la interfaz Wi-Fi
    wlan.active(True)  # Habilita la conexión
    wlan.connect(SSID, PASSWORD)  # Intenta conectarse a la red Wi-Fi

    print("Conectando a Wi-Fi...", end="")
    while not wlan.isconnected():  # Espera hasta que se establezca la conexión
        print(".", end="")
        utime.sleep(1)  # Espera 1 segundo entre intentos
    print("\nConectado:", wlan.ifconfig())  # Muestra la configuración de red obtenida

def leer_temperatura():
    """
    Lee la temperatura interna del RP2040 y la convierte a grados Celsius.
    
    Retorna:
        float: Temperatura en grados Celsius.
    """
    valor_adc = sensor_temp.read_u16()  # Obtiene el valor crudo del ADC (16 bits)
    voltaje = valor_adc * CONVERSION_FACTOR  # Convierte el valor a voltaje
    temperatura = 27 - (voltaje - 0.706) / 0.001721  # Aplica la fórmula para RP2040
    return temperatura  # Retorna la temperatura calculada

def enviar_a_thingspeak(temperatura):
    """
    Envía la temperatura a la plataforma ThingSpeak mediante una solicitud HTTP GET.
    
    Args:
        temperatura (float): Valor de la temperatura a enviar.
    """
    try:
        # Construcción de la URL con la temperatura como parámetro (field1)
        url = f"{THINGSPEAK_URL}?api_key={THINGSPEAK_API_KEY}&field1={temperatura}"
        respuesta = urequests.get(url)  # Realiza la solicitud GET
        print("Datos enviados:", respuesta.text)  # Muestra la respuesta del servidor
        respuesta.close()  # Cierra la conexión
    except Exception as e:
        print("Error al enviar datos:", e)  # Manejo de errores en caso de fallo

# --- Programa principal ---
conectar_wifi()  # Conectar a la red Wi-Fi antes de iniciar la lectura de temperatura

while True:
    temp = leer_temperatura()  # Leer la temperatura actual
    print(f"Temperatura interna: {temp:.2f}°C")  # Mostrar la temperatura en consola
    enviar_a_thingspeak(temp)  # Enviar la temperatura a ThingSpeak
    utime.sleep(180)  # Esperar 3 minutos antes de la próxima medición
