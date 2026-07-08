class StateNeighbors:
    """
    MEC-002C

    Determina os vizinhos estruturais
    mais próximos de cada estado.
    """

    def calcular(
        self,
        distancias,
        quantidade=5
    ):
        """
        Seleciona os N vizinhos
        mais próximos de cada estado.

        Parameters
        ----------
        distancias : dict

        quantidade : int

        Returns
        -------
        dict
        """

        vizinhos = {}

        for concurso, lista in distancias.items():

            vizinhos[concurso] = lista[:quantidade]

        return vizinhos
    