class IntervalAnalyzer:
    """
    NC-003

    Responsável por transformar as trajetórias
    em intervalos entre ocorrências consecutivas.
    """

    def construir_intervalos(self, trajetoria):
        """
        Recebe uma trajetória e devolve
        os intervalos entre concursos consecutivos.

        Exemplo:

        [4, 18, 39, 62]

        retorna

        [14, 21, 23]
        """

        intervalos = []

        for i in range(1, len(trajetoria)):

            intervalo = trajetoria[i] - trajetoria[i - 1]

            intervalos.append(intervalo)

        return intervalos

    def calcular(self, trajetorias):
        """
        Calcula os intervalos
        de todas as 60 dezenas.
        """

        resultado = {}

        for dezena, trajetoria in trajetorias.items():

            intervalos = self.construir_intervalos(trajetoria)

            if len(intervalos) > 0:

                media = round(
                    sum(intervalos) / len(intervalos),
                    2
                )

                menor = min(intervalos)

                maior = max(intervalos)

            else:

                media = None
                menor = None
                maior = None

            resultado[dezena] = {

                "intervalos": intervalos,

                "quantidade": len(intervalos),

                "media": media,

                "menor": menor,

                "maior": maior
            }

        return resultado