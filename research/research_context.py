class ResearchContext:
    """
    Contexto compartilhado do GD-Lab.

    Armazena todos os resultados produzidos
    pelos Núcleos Científicos (NC)
    e pelos Módulos de Evolução Científica (MEC).
    """

    def __init__(self):

        # Histórico
        self.dados = None

        # NC-001
        self.trajetorias = None

        # NC-002
        self.estatisticas = None

        # NC-003
        self.intervalos = None

        # NC-004
        self.evolucao = None

        # NC-005
        self.estados = None

        # NC-006
        self.estados_historicos = None

        # NC-007
        self.idade_media = None

        # NC-008
        self.transition_matrix = None
        self.transition_probability = None
        self.transition_statistics = None

        # MEC-002
        self.vetores = None
        self.distancias = None
        self.vizinhos = None
        self.mapa = None
        self.mec_report = None

        # Área para futuras expansões
        self.extra = {}