from abc import ABC, abstractmethod


class ConfigContext:
    def __init__(self):
        self.configurations = {}

    def set_config(self, key, value):
        self.configurations[key] = value

    def get_config(self, key):
        return self.configurations.get(key)


class ConfigExpression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass


class AssignmentExpression(ConfigExpression):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def interpret(self, context):
        context.set_config(self.key, self.value)


class BlockExpression(ConfigExpression):
    def __init__(self, expressions):
        self.expressions = expressions

    def interpret(self, context):
        for expression in self.expressions:
            expression.interpret(expression.key, expression.value)
