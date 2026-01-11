# Behavioural Design Patterns

Behavioural design patterns are a category of design patterns that focus on communication between objects. They help in defining how objects interact and distribute responsibilities, making the system more flexible and easier to maintain.

## Key Characteristics
- Focus on object collaboration.
- Improve communication between objects.
- Promote loose coupling.

## Common Behavioural Design Patterns

1. **Chain of Responsibility**  
    Pass requests along a chain of handlers. Each handler decides whether to process the request or pass it to the next handler.

2. **Command**  
    Encapsulate a request as an object, allowing you to parameterize objects with different requests, delay execution, or support undoable operations.

3. **Interpreter**  
    Define a grammar for a language and provide an interpreter to process sentences in the language.

4. **Iterator**  
    Provide a way to access elements of a collection sequentially without exposing its underlying representation.

5. **Mediator**  
    Reduce direct communication between objects by introducing a mediator object that handles interactions.

6. **Memento**  
    Capture and restore an object's state without exposing its internal structure.

7. **Observer**  
    Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified.

8. **State**  
    Allow an object to alter its behavior when its internal state changes.

9. **Strategy**  
    Define a family of algorithms, encapsulate each one, and make them interchangeable.

10. **Template Method**  
     Define the skeleton of an algorithm in a method, deferring some steps to subclasses.

11. **Visitor**  
     Separate an algorithm from the object structure it operates on, allowing new operations to be added without modifying the objects.

## Benefits
- Enhances flexibility and scalability.
- Simplifies complex workflows.
- Promotes code reuse and maintainability.

## Use Cases
- Applications requiring dynamic behavior changes.
- Systems with complex workflows or multiple interacting objects.
- Scenarios where loose coupling is essential.

## Resources
- [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns)
- [Refactoring.Guru - Behavioural Patterns](https://refactoring.guru/design-patterns)

Explore these patterns to improve the design and maintainability of your software projects!