from dataclasses import dataclass, field

@dataclass
class TierList:
    name: str
    tiers: list = field(default_factory=list)
    image_items: list = field(default_factory=list)