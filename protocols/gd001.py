from database.loader import Loader
from research.research_engine import ResearchEngine


class GD001:

    def __init__(self):

        print(">>> GD001 criado")

        self.nome = "GD-001 - Reconstrução das Trajetórias"

        self.loader = Loader()
        self.engine = ResearchEngine()

    def executar(self):

        print("\n[GD-001] Iniciando protocolo...")

        arquivo = "mega_sena_asloterias_ate_concurso_3027_crescente.xlsx"

        try:

            dados = self.loader.load_excel(arquivo)

            print("[GD-001] Histórico carregado com sucesso.")
            print(f"[GD-001] Total de concursos: {len(dados)}")

            context = self.engine.executar(dados)

            trajetorias = context.trajetorias
            estatisticas = context.estatisticas
            intervalos = context.intervalos
            estado = context.estados
            estados_historicos = context.estados_historicos

            total_ocorrencias = sum(
                len(t)
                for t in trajetorias.values()
            )

            esperado = len(dados) * 6

            print(f"[GD-001] Total de trajetórias: {len(trajetorias)}")
            print(f"[GD-001] Total de ocorrências: {total_ocorrencias}")
            print(f"[GD-001] Esperado: {esperado}")

            if total_ocorrencias == esperado:
                print("[GD-001] Validação: OK")
            else:
                print("[GD-001] Validação: FALHOU")

            print("\n================ MEC REPORT 0002 ================")

            print(
                f"{'Dz':>2} "
                f"{'Ocorr':>6} "
                f"{'Média':>7} "
                f"{'Min':>5} "
                f"{'Max':>5} "
                f"{'Idade':>6}"
            )

            print("-" * 40)

            for dezena in range(1, 61):

                est = estatisticas[dezena]
                inter = intervalos[dezena]
                idade = estado["idades"][dezena]

                print(
                    f"{dezena:02d} "
                    f"{est['ocorrencias']:6d} "
                    f"{inter['media']:7.2f} "
                    f"{inter['menor']:5d} "
                    f"{inter['maior']:5d} "
                    f"{idade:6d}"
                )

            print("\n================ MEC REPORT 0003 ================")

            print(
                f"Estados históricos reconstruídos : "
                f"{len(estados_historicos)}"
            )

            print(
                f"Primeiro concurso : "
                f"{min(estados_historicos.keys())}"
            )

            print(
                f"Último concurso   : "
                f"{max(estados_historicos.keys())}"
            )

            print("\n================ MEC-002 REPORT ================")

            report = context.mec_report

            print(
                f"Estados........... {report['total_estados']}"
            )

            print(
                f"Vetores........... {report['total_vetores']}"
            )

            print(
                f"Distâncias........ {report['total_matrizes']}"
            )

            print(
                f"Vizinhanças....... {report['total_vizinhos']}"
            )

            print(
                f"Grafo............. {report['total_vertices']}"
            )

            print(
                f"Grau médio........ {report['grau_medio']}"
            )

            print("\nSTATUS : MEC-002 VALIDADO")

            return context

        except Exception as erro:

            print(f"[GD-001] Erro: {erro}")

            return None