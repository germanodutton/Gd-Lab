from core.logger import Logger
from core.protocol_manager import ProtocolManager
from protocols.gd001 import GD001


class Application:

    def __init__(self):
        self.logger = Logger()
        self.protocol_manager = ProtocolManager()

    def run(self):

        print("=" * 45)
        print("GD-Lab Scientific AI")
        print("Version 0.1")
        print("=" * 45)

        self.logger.info("Inicializando aplicação.")

        self.protocol_manager.registrar(GD001())
        self.protocol_manager.executar()

        print("Application started successfully.")

        self.logger.info("Sistema carregado com sucesso.")

        print("=" * 45)