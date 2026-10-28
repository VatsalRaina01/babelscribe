from dataclasses import dataclass
from typing import Optional

@dataclass
class ModelConfig:
    name: str
    language: str
    dataset: str
    tier: str = "FINETUNES"
    description: Optional[str] = None

MODELS = [
    ModelConfig(
        name="vietnamese-vivos",
        language="vi",
        dataset="vivos",
        tier="FINETUNES",
        description="Vietnamese ASR model trained on VIVOS"
    )
]
