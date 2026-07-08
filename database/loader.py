from pathlib import Path

import pandas as pd


class Loader:
    """
    Responsável pelo carregamento dos dados do GD-Lab.
    """

    def __init__(self):

        # Pasta onde está este arquivo (database)
        self.base_path = Path(__file__).resolve().parent

    def file_exists(self, filename):

        return self.get_file_path(filename).exists()

    def get_file_path(self, filename):

        return self.base_path / filename

    def load_csv(self, filename):

        file_path = self.get_file_path(filename)

        if not file_path.exists():
            raise FileNotFoundError(
                f"Arquivo não encontrado: {file_path}"
            )

        return pd.read_csv(file_path)

    def load_excel(self, filename):

        file_path = self.get_file_path(filename)

        if not file_path.exists():
            raise FileNotFoundError(
                f"Arquivo não encontrado: {file_path}"
            )

        dados = pd.read_excel(
            file_path,
            header=6,
            engine="openpyxl"
        )

        dados = dados.sort_values("Concurso")
        dados = dados.reset_index(drop=True)

        return dados
        print("Loader importado com sucesso")