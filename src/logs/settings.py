import logging
import builtins


# Configurar o logger como de costume
def log_config():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("src/logs/output.log"),  # Defina o nome do arquivo de log aqui
            logging.StreamHandler()  # Para continuar exibindo as mensagens no console
        ]
    )


# Substituir a função print por uma função que utiliza o logger
def custom_print(*args, **kwargs):
    logger = logging.getLogger(__name__)
    message = " ".join(map(str, args))
    logger.info(message)

def printing_log():
# Substituir a função print globalmente
    builtins.print = custom_print

