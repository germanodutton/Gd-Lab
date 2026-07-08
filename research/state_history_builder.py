class StateHistoryBuilder:
    """
    NC-006

    Reconstrói o estado completo do sistema
    para todos os concursos do histórico.

    Cada estado representa a idade das
    60 dezenas naquele instante.
    """

    def construir(self, dados):
        """
        Reconstrói todos os estados históricos.

        Retorna um dicionário no formato:

        {
            concurso: {
                "concurso": numero,
                "idades": {
                    1: idade,
                    2: idade,
                    ...
                    60: idade
                }
            }
        }
        """

        estados = {}

        # Todas as dezenas começam com idade zero
        idades = {
            dezena: 0
            for dezena in range(1, 61)
        }

        # Descobre automaticamente as colunas das dezenas
        colunas_dezenas = [
            coluna
            for coluna in dados.columns
            if coluna != "Concurso"
        ]

        # Percorre todos os concursos
        for _, linha in dados.iterrows():

            concurso = int(linha["Concurso"])

            # Todas envelhecem um concurso
            for dezena in idades:
                idades[dezena] += 1

            # Zera a idade das dezenas sorteadas
            for coluna in colunas_dezenas:

                valor = linha[coluna]

                if valor is None:
                    continue

                try:

                    dezena = int(valor)

                    if 1 <= dezena <= 60:
                        idades[dezena] = 0

                except (ValueError, TypeError):
                    continue

            # Guarda uma cópia do estado atual
            estados[concurso] = {
                "concurso": concurso,
                "idades": idades.copy()
            }

        return estados