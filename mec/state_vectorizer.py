class StateVectorizer:
    """
    MEC-002A

    Converte todos os estados históricos
    em vetores matemáticos.

    Cada vetor possui 60 posições,
    correspondentes às idades das dezenas.
    """

    def construir(self, estados_historicos):

        vetores = {}

        for concurso, estado in estados_historicos.items():

            vetor = []

            for dezena in range(1, 61):

                vetor.append(
                    estado["idades"][dezena]
                )

            vetores[concurso] = vetor

        return vetores