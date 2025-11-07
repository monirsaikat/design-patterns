# 🧰 Factory Method Pattern (Python)

## 💡 Definition
The **Factory Method** pattern defines a base interface for creating objects  
but lets subclasses decide which concrete class to instantiate.

## 🧠 Key Idea
The parent class defines the *factory method*, and child classes override it.  
This removes direct dependencies and supports easy extension.

## 🧩 Example
`NotifierCreator.create_notifier()` → overridden by  
`EmailNotifierCreator` or `SMSNotifierCreator` to return their own notifiers.

## ⚙️ Real Use
Use it when you want to delegate object creation to subclasses  
and follow the **Open/Closed Principle** (extend without modifying existing code).


## Resources | Notes:
> Factory method is generally used when you have some generic processing in a class, but want to vary which kind of fruit you actually use. So:
```java
// Source - https://stackoverflow.com/a/13030163
// Posted by Anders Johansen, modified by community. See post 'Timeline' for change history
// Retrieved 2025-11-07, License - CC BY-SA 4.0

abstract class FruitPicker {

  protected abstract Fruit makeFruit();

  public void pickFruit() {
    private final Fruit f = makeFruit(); // The fruit we will work on..
    <bla bla bla>
  }
}
```