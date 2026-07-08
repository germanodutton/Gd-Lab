"""
NC-008
Transition Analyzer

Reconstrói a matriz de transição entre estados históricos.
"""

from collections import defaultdict


class TransitionAnalyzer:
    """
    Analisa as transições entre estados históricos.
    """

    def calcular(self, estados_historicos):
        """
        Calcula a matriz de transição.
        """

        concursos = sorted(estados_historicos.keys())

        matriz = defaultdict(lambda: defaultdict(int))

        total_transicoes = 0

        for i in range(len(concursos) - 1):

            concurso_origem = concursos[i]
            concurso_destino = concursos[i + 1]

            estado_origem = estados_historicos[concurso_origem]
            estado_destino = estados_historicos[concurso_destino]

            origem = self._assinatura(estado_origem)
            destino = self._assinatura(estado_destino)

            matriz[origem][destino] += 1
            total_transicoes += 1

        probabilidades = self._probabilidades(matriz)

        return {
            "transition_matrix": dict(matriz),
            "transition_probability": probabilidades,
            "transition_statistics": {
                "total_estados": len(matriz),
                "total_transicoes": total_transicoes,
            },
        }

    def _assinatura(self, estado):
        """
        Cria uma assinatura única do estado.
        """

        idades = estado["idades"]

        return tuple(
            idades[dezena]
            for dezena in range(1, 61)
        )

    def _probabilidades(self, matriz):

        probabilidades = {}

        for origem, destinos in matriz.items():

            total = sum(destinos.values())

            probabilidades[origem] = {}

            for destino, quantidade in destinos.items():

                probabilidades[origem][destino] = quantidade / total

        return probabilidades