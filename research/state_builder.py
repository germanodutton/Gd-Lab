class StateBuilder:
    """
    NC-005

    Reconstrói o estado atual do sistema.
    Versão 1.0
    """

    def calcular_idades(self, trajetorias, concurso_atual):
        """
        Calcula a idade de cada dezena.

        Idade = concursos decorridos desde
        a última ocorrência.
        """

        idades = {}

        for dezena, concursos in trajetorias.items():

            if len(concursos) == 0:

                idades[dezena] = None

            else:

                ultima_ocorrencia = concursos[-1]

                idade = concurso_atual - ultima_ocorrencia

                idades[dezena] = idade

        return idades

    def construir(self, trajetorias, concurso_atual):
        """
        Constrói o estado atual do sistema.
        """

        estado = {

            "concurso": concurso_atual,

            "idades": self.calcular_idades(
                trajetorias,
                concurso_atual
            )

        }

        return estado