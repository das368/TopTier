from dataclasses import dataclass, field

@dataclass
class Tier:
    name: str
    images: list = field(default_factory=list)