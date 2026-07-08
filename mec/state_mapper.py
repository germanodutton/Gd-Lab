class StateMapper:
    """
    MEC-002D

    Constrói um mapa estrutural
    baseado na vizinhança entre estados.
    """

    def construir(self, vizinhos):
        """
        Constrói o grafo estrutural.

        Parameters
        ----------
        vizinhos : dict

        Returns
        -------
        dict
        """

        mapa = {}

        for concurso, lista in vizinhos.items():

            mapa[concurso] = {

                "neighbors": [
                    outro
                    for outro, _ in lista
                ],

                "degree": len(lista)

            }

        return mapa