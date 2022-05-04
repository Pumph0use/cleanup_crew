import os

from dotenv import load_dotenv

load_dotenv()
RABBITMQ_USERNAME = os.getenv('RABBITMQ_USERNAME', None)
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD', None)
RABBITMQ_HOSTNAME = os.getenv('RABBITMQ_HOSTNAME', None)
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT', None)

BROKER_URL = f'amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOSTNAME}:{RABBITMQ_PORT}//'

REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)
REDIS_HOSTNAME = os.getenv('REDIS_HOSTNAME', None)
REDIS_PORT = os.getenv('REDIS_PORT', None)
REDIS_BACKEND_DB = os.getenv('REDIS_BACKEND_DB', None)

BACKEND_URL = f'redis://:{REDIS_PASSWORD}@{REDIS_HOSTNAME}:{REDIS_PORT}/{REDIS_BACKEND_DB}'
