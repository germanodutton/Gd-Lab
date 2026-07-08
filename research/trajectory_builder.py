class TrajectoryBuilder:
    """
    Reconstrói as trajetórias das 60 dezenas da Mega-Sena.
    """

    def __init__(self):
        self.trajetorias = {
            dezena: []
            for dezena in range(1, 61)
        }

    def construir(self, dados):
        """
        Recebe o DataFrame da Mega-Sena e reconstrói
        as trajetórias de todas as dezenas.
        """

        colunas = [
            "bola 1",
            "bola 2",
            "bola 3",
            "bola 4",
            "bola 5",
            "bola 6"
        ]

        for _, linha in dados.iterrows():

            concurso = int(linha["Concurso"])

            for coluna in colunas:

                dezena = int(linha[coluna])

                self.trajetorias[dezena].append(concurso)

        return self.trajetorias