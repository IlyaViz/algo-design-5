from abc import ABC, abstractmethod
from typing import Callable


class LocalImprovementStrategyBase(ABC):
    @staticmethod
    @abstractmethod
    def improve(individual: list, target_function: Callable) -> list:
        pass