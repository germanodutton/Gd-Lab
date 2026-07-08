class MECReport:
    """
    MEC-002E

    Gera um relatório resumido
    da cartografia do espaço de estados.
    """

    def gerar(
        self,
        vetores,
        distancias,
        vizinhos,
        mapa
    ):

        relatorio = {

            "total_estados": len(vetores),

            "total_vetores": len(vetores),

            "total_matrizes": len(distancias),

            "total_vizinhos": len(vizinhos),

            "total_vertices": len(mapa),

            "grau_medio": round(
                sum(
                    item["degree"]
                    for item in mapa.values()
                ) / len(mapa),
                2
            )

        }

        return relatorio