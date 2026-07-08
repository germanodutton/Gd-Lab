from research.trajectory_builder import TrajectoryBuilder
from research.trajectory_statistics import TrajectoryStatistics
from research.interval_analyzer import IntervalAnalyzer
from research.metric_evolution import MetricEvolution
from research.state_builder import StateBuilder
from research.state_history_builder import StateHistoryBuilder
from research.state_metrics import StateMetrics
from research.transition_analyzer import TransitionAnalyzer
from research.research_context import ResearchContext
from mec.state_vectorizer import StateVectorizer
from mec.state_distance import StateDistance
from mec.state_neighbors import StateNeighbors
from mec.state_mapper import StateMapper
from mec.mec_report import MECReport

class ResearchEngine:
    """
    Motor científico do GD-Lab.

    Executa todos os Núcleos Científicos
    e devolve um ResearchContext completo.
    """

    def __init__(self):

        # NC-001
        self.builder = TrajectoryBuilder()

        # NC-002
        self.statistics = TrajectoryStatistics()

        # NC-003
        self.interval_analyzer = IntervalAnalyzer()

        # NC-004
        self.metric_evolution = MetricEvolution()

        # NC-005
        self.state_builder = StateBuilder()

        # NC-006
        self.state_history_builder = StateHistoryBuilder()

        # NC-007
        self.state_metrics = StateMetrics()

        # NC-008
        self.transition_analyzer = TransitionAnalyzer()

    def executar(self, dados):

        context = ResearchContext()

        context.dados = dados

        # NC-001
        trajetorias = self.builder.construir(dados)
        context.trajetorias = trajetorias

        # NC-002
        estatisticas = self.statistics.calcular(trajetorias)
        context.estatisticas = estatisticas

        # NC-003
        intervalos = self.interval_analyzer.calcular(trajetorias)
        context.intervalos = intervalos

        # NC-004
        evolucao = self.metric_evolution.calcular(intervalos)
        context.evolucao = evolucao

        # NC-005
        concurso_atual = int(dados["Concurso"].max())

        estado = self.state_builder.construir(
            trajetorias,
            concurso_atual
        )

        context.estados = estado

        # NC-006
        estados_historicos = self.state_history_builder.construir(
            dados
        )

        context.estados_historicos = estados_historicos

        # NC-007
        idade_media = self.state_metrics.calcular_idade_media(
            estados_historicos
        )

        context.idade_media = idade_media

        # NC-008
        transition = self.transition_analyzer.calcular(
            estados_historicos
        )

        context.extra.update(transition)

        return context