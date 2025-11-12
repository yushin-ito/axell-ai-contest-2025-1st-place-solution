from dataclasses import dataclass


@dataclass
class Config:
    device: int = 0
    imgsz: int | tuple[int, int] = (576, 768)
    conf: float = 0.09
    iou: float = 0.33
