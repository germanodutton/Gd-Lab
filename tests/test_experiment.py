
"""
GD-Lab Scientific AI
===================

Primeiro teste da classe Experiment.

Autor:
Antonio Germano da Costa Moreira Dutton
"""

from core.experiment import Experiment


def main():

	experiment = Experiment(
		title="Primeiro Experimento do GD-Lab",
		description="Validação da classe Experiment."
	)

	print("\n=== EXPERIMENTO CRIADO ===\n")

	print(experiment)

	print("\n=== DICIONÁRIO ===\n")

	print(experiment.to_dict())


if __name__ == "__main__":
	main()
