import pika
import os
import time
import sys

RABBITMQ_URL = os.environ.get('RABBITMQ_URL', 'amqp://admin:admin@rabbitmq:5672')

def callback(ch, method, properties, body):
    print(f"Petición recibida: {body.decode()}")
    sys.stdout.flush()  # Forzar flush del buffer de salida

def main():
    # Implementar reintentos con espera
    max_attempts = 30
    for attempt in range(max_attempts):
        try:
            print(f"Intento de conexión {attempt+1}/{max_attempts}...")
            sys.stdout.flush()
            
            connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
            channel = connection.channel()
            channel.queue_declare(queue='logs')
            channel.basic_consume(queue='logs', on_message_callback=callback, auto_ack=True)
            
            print("Conectado a RabbitMQ. Esperando peticiones...")
            sys.stdout.flush()
            
            channel.start_consuming()
            break
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Error de conexión: {e}")
            sys.stdout.flush()
            if attempt < max_attempts - 1:
                wait_time = min(30, 2 * attempt)  # Incremento exponencial pero máximo 30s
                print(f"Reintentando en {wait_time} segundos...")
                sys.stdout.flush()
                time.sleep(wait_time)
            else:
                print("Se alcanzó el número máximo de intentos. Saliendo...")
                sys.stdout.flush()
                raise

if __name__ == "__main__":
    main()