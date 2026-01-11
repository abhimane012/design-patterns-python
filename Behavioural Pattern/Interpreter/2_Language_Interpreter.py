# Language Interpreter
from abc import ABC, abstractmethod


class Program:
    def __init__(self):
        self.variables = {}

    def set_variable(self, var, value):
        self.variables[var] = value

    def get_variable(self, var):
        return self.variables[var]


class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass


class VariableExpression(Expression):
    def __init__(self, variable):
        self.variable = variable

    def interpret(self, context):
        return context.get_variable(self.variable)


class AssignmentExpression(Expression):
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

    def interpret(self, context):
        context.set_variable(self.variable, self.value)


class AddExpression(Expression):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

    def interpret(self, context):
        value1 = self.expression1.interpret(context)
        value2 = self.expression2.interpret(context)
        return value1 + value2


if __name__ == "__main__":
    context = Program()

    AssignmentExpression("x", 10).interpret(context)
    AssignmentExpression("y", 10).interpret(context)

    add_expression = AddExpression(VariableExpression("x"), VariableExpression("y"))
    add_value = add_expression.interpret(context)
    AssignmentExpression("z", add_value).interpret(context)
    result = VariableExpression("z").interpret(context)
    print(context.__dict__)
