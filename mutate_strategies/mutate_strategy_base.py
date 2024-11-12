from abc import ABC, abstractmethod


class MutateStrategyBase(ABC):
    @staticmethod
    @abstractmethod
    def mutate(individual: list) -> list:
        pass