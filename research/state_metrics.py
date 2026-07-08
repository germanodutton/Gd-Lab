class StateMetrics:
    """
    NC-007A

    Calcula métricas globais dos estados
    históricos do sistema.
    """

    def calcular_idade_media(self, estados_historicos):
        """
        Calcula a idade média das 60 dezenas
        para cada concurso.
        """

        evolucao = []

        for concurso in sorted(estados_historicos.keys()):

            estado = estados_historicos[concurso]

            idades = list(
                estado["idades"].values()
            )

            media = round(
                sum(idades) / len(idades),
                2
            )

            evolucao.append({

                "concurso": concurso,

                "idade_media": media

            })

        return evolucao