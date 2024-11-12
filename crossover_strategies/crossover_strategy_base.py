from abc import ABC, abstractmethod


class CrossoverStrategyBase(ABC):
    @staticmethod
    @abstractmethod
    def crossover(parent1: list, parent2: list) -> list:
        pass