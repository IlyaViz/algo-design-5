from typing import Callable
from .local_improvement_strategy_base import LocalImprovementStrategyBase


class InsertImprovementStrategy(LocalImprovementStrategyBase):
    def improve(individual: list, target_function: Callable) -> list:
        length = len(individual)

        init_target_function = target_function(individual)

        for gen_number in range(length):
            city = individual.pop(gen_number)

            for insert_position in range(length-1):
                individual.insert(insert_position, city)

                if target_function(individual) < init_target_function:
                    return

                individual.pop(insert_position)

            individual.insert(gen_number, city)
