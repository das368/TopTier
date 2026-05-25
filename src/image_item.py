from dataclasses import dataclass

@dataclass
class ImageItem:
    id: str
    path: str
    original_name: str