from typing import Callable
from .local_improvement_strategy_base import LocalImprovementStrategyBase


class SwapImprovementStrategy(LocalImprovementStrategyBase):
    def improve(individual: list, target_function: Callable) -> list:
        length = len(individual)

        init_target_function = target_function(individual)

        for gen_number1 in range(length):
            for gen_number2 in range(gen_number1+1, length):
                individual[gen_number1], individual[gen_number2] = individual[gen_number2], individual[gen_number1]

                if target_function(individual) < init_target_function:
                    return

                individual[gen_number1], individual[gen_number2] = individual[gen_number2], individual[gen_number1]
        