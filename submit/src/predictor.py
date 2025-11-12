import os
from typing import List, Dict

import numpy as np
from ultralytics import YOLO
from ultralytics.utils.ops import xyxy2ltwh

from config import Config


class Predictor(object):
    cfg = Config()

    @classmethod
    def get_model(cls, model_path: str) -> bool:
        cls.model = YOLO(os.path.join(model_path, "best.pt"))

        cls.model.export(
            format="engine",
            imgsz=cls.cfg.imgsz,
            nms=True,
            conf=cls.cfg.conf,
            iou=cls.cfg.iou,
            half=True,
            device=cls.cfg.device,
        )

        cls.model = YOLO(os.path.join(model_path, "best.engine"))

        height, width = (
            cls.cfg.imgsz
            if isinstance(cls.cfg.imgsz, tuple)
            else (cls.cfg.imgsz, cls.cfg.imgsz)
        )

        for _ in range(9):
            cls.model.predict(
                source=np.zeros((height, width, 3), dtype=np.uint8),
                device=cls.cfg.device,
                verbose=False,
            )

        return True

    @classmethod
    def predict(cls, input: np.ndarray) -> List[Dict]:
        results = cls.model.predict(
            source=input,
            device=cls.cfg.device,
            max_det=5,
            verbose=False,
        )

        data = results[0].boxes.data

        if len(data) == 0:
            return []

        data = data.cpu().numpy()

        boxes = data[:, :4]
        conf_scores = data[:, 4]
        class_ids = data[:, 5].astype(np.int32)

        boxes = xyxy2ltwh(boxes)

        outputs = [
            {
                "category_id": int(class_id + 1),
                "bbox": box.tolist(),
                "score": float(conf_score),
            }
            for class_id, box, conf_score in zip(class_ids, boxes, conf_scores)
        ]

        return outputs
