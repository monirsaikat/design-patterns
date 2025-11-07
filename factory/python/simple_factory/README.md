# 🏭 Simple Factory Pattern (Python)

## 💡 Definition
The **Simple Factory** pattern centralizes object creation inside one function or class.  
It decides which concrete class to instantiate based on an input parameter.

## 🧠 Key Idea
Clients don’t create objects directly — they ask the factory.  
The factory hides the creation logic and returns the correct product.

## 🧩 Example
`make_notifier(kind)` → returns either `EmailNotifier` or `SMSNotifier`.

## ⚙️ Real Use
Use it when you have multiple similar objects and want to centralize creation.

## Resources | Notes
> Factory is "fixed", in that you have just one implementation with no subclassing. In this case, you will have a class like this:
```java
// Source - https://stackoverflow.com/a/13030163
// Posted by Anders Johansen, modified by community. See post 'Timeline' for change history
// Retrieved 2025-11-07, License - CC BY-SA 4.0

class FruitFactory {

  public Apple makeApple() {
    // Code for creating an Apple here.
  }

  public Orange makeOrange() {
    // Code for creating an orange here.
  }

}
```