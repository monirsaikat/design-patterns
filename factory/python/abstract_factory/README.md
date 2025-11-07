# 🏢 Abstract Factory Pattern (Python)

## 💡 Definition
Creates **families of related objects** (multiple products) without specifying concrete classes.

## 🧠 Key Idea
Client asks one factory for matching products. Swap the factory to switch the whole family.

## 🧩 Example
`NotifierSuiteFactory` → creates `Notifier` + `AuditLogger`.  
`ProductionFactory` uses real notifier + file logger; `TestFactory` uses dummy + null logger.

## ⚙️ Real Use
When multiple objects must be used together (themes, platforms, vendors, envs).
