"""
GD-Lab Scientific AI
===================

Core Module
-----------

Experiment

Representa um experimento científico executado dentro do GD-Lab.

Autor:
Antonio Germano da Costa Moreira Dutton
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class ExperimentStatus(Enum):
    """
    Estados possíveis de um experimento.
    """

    CREATED = "CREATED"
    CONFIGURED = "CONFIGURED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    ARCHIVED = "ARCHIVED"


@dataclass(slots=True)
class Experiment:
    """
    Representa um experimento científico do GD-Lab.

    Esta classe armazena apenas as informações essenciais
    para identificação, rastreabilidade e estado do experimento.
    """

    title: str
    description: str = ""
    author: str = "Antonio Germano da Costa Moreira Dutton"
    version: str = "0.1.0"

    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=datetime.now)
    status: ExperimentStatus = field(default=ExperimentStatus.CREATED)
    notes: str = ""

    def set_status(self, status: ExperimentStatus) -> None:
        """
        Atualiza o estado do experimento.
        """
        self.status = status

    def to_dict(self) -> dict:
        """
        Retorna uma representação serializável do experimento.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "author": self.author,
            "version": self.version,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "notes": self.notes,
        }

    def __str__(self) -> str:
        """
        Retorna uma representação legível do experimento.
        """
        return (
            "Experiment\n"
            "------------------------------\n"
            f"ID         : {self.id}\n"
            f"Title      : {self.title}\n"
            f"Status     : {self.status.value}\n"
            f"Version    : {self.version}\n"
            f"Author     : {self.author}\n"
            f"Created At : {self.created_at}"
        )