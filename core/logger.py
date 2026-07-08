from datetime import datetime


class Logger:

    def info(self, mensagem):
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[INFO] {agora} - {mensagem}")

    def warning(self, mensagem):
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[WARNING] {agora} - {mensagem}")

    def error(self, mensagem):
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[ERROR] {agora} - {mensagem}")
