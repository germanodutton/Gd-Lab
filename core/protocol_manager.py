
class ProtocolManager:

	def __init__(self):
		self.protocolos = []

	def registrar(self, protocolo):
		self.protocolos.append(protocolo)

	def executar(self):

		if not self.protocolos:
			print("Nenhum protocolo registrado.")
			return

		print("\nProtocolos registrados:")

		for protocolo in self.protocolos:
			print(f" - {protocolo.nome}")

			if hasattr(protocolo, "executar"):
				protocolo.executar()
