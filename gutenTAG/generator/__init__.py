from __future__ import annotations

from typing import Optional, Dict, List, Union
import numpy as np
import matplotlib.pyplot as plt
import json, os

from gutenTAG.base_oscillations import BaseOscillation, BaseOscillationInterface
from gutenTAG.anomalies import Anomaly, AnomalyPlatform, Position


class GutenTAG:
    def __init__(self, base_oscillation: BaseOscillationInterface, anomalies: List[Anomaly], plot: bool = False):
        self.base_oscillation = base_oscillation
        self.anomalies = anomalies
        self.timeseries: Optional[np.ndarray] = None

        self._generate_base_oscillation()
        if plot:
            self._plot()

    def _generate_base_oscillation(self):
        self.timeseries = self.base_oscillation.inject_anomalies(self.anomalies).generate()

    def _plot(self):
        plt.plot(self.timeseries)
        plt.show()

    @staticmethod
    def from_json(path: os.PathLike) -> List[GutenTAG]:
        with open(path, "r") as f:
            config = json.load(f)
        return GutenTAG.from_dict(config)

    @staticmethod
    def from_dict(config: Dict) -> List[GutenTAG]:
        result = []
        for ts in config.get("timeseries", []):
            base_oscillation_configs = ts.get("base-oscillation", {})
            key = base_oscillation_configs.get("kind", "sinus")
            base_oscillation = BaseOscillation.from_key(key, **base_oscillation_configs)
            anomalies = []
            for anomaly_config in ts.get("anomalies", []):
                anomaly = Anomaly(Position(anomaly_config.get("position", "middle")), anomaly_config.get("length", 200))

                for anomaly_kind in anomaly_config.get("kinds", []):
                    name = anomaly_kind.get("name", "platform")
                    if name == "platform":
                        anomaly.set_platform(AnomalyPlatform(anomaly_kind.get("value", 0.0)))
                anomalies.append(anomaly)
            result.append(GutenTAG(base_oscillation, anomalies, True))
        return result


if __name__ == "__main__":
    GutenTAG.from_json("./generation_config.json")
