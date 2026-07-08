class MetricEvolution:
    """
    NC-004

    Reconstrói a evolução de métricas ao longo do tempo.

    Versão 1.0:
    Evolução da média acumulada.
    """

    def evolucao_media(self, valores):
        """
        Recebe uma lista de valores e retorna
        a evolução da média acumulada.

        Exemplo:

        Entrada:
        [1, 17, 2, 22]

        Saída:
        [1.0, 9.0, 6.67, 10.5]
        """

        medias = []

        soma = 0

        for i, valor in enumerate(valores):

            soma += valor

            media = soma / (i + 1)

            medias.append(round(media, 2))

        return medias

    def calcular(self, intervalos):
        """
        Calcula a evolução da média
        para todas as dezenas.
        """

        resultado = {}

        for dezena, info in intervalos.items():

            medias = self.evolucao_media(
                info["intervalos"]
            )

            resultado[dezena] = {
                "media_evolucao": medias
            }

        return resultado