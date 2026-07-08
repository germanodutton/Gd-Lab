class TrajectoryStatistics:
    """
    Calcula estatísticas básicas das trajetórias.
    """

    def calcular(self, trajetorias):

        estatisticas = {}

        for dezena, concursos in trajetorias.items():

            estatisticas[dezena] = {
                "ocorrencias": len(concursos),
                "primeiro_concurso": concursos[0],
                "ultimo_concurso": concursos[-1]
            }

        return estatisticas