import math


class StateDistance:
    """
    MEC-002B

    Calcula distâncias entre estados históricos.
    """

    def distancia_euclidiana(self, vetor_a, vetor_b):
        """
        Calcula a distância euclidiana entre dois vetores.
        """

        soma = 0.0

        for a, b in zip(vetor_a, vetor_b):

            soma += (a - b) ** 2

        return math.sqrt(soma)

    def calcular(self, vetores):
        """
        Calcula a distância entre todos os estados.

        Retorna:

        {
            concurso: [
                (outro_concurso, distancia),
                ...
            ]
        }
        """

        concursos = sorted(vetores.keys())

        distancias = {}

        for concurso in concursos:

            vetor = vetores[concurso]

            lista = []

            for outro in concursos:

                if concurso == outro:
                    continue

                distancia = self.distancia_euclidiana(
                    vetor,
                    vetores[outro]
                )

                lista.append(
                    (
                        outro,
                        round(distancia, 4)
                    )
                )

            lista.sort(
                key=lambda x: x[1]
            )

            distancias[concurso] = lista

        return distancias