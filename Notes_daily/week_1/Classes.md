# Week 1 – Understanding Classes (PyQGIS Foundation)

This week focuses on **Classes and Objects**, which are essential before starting **PyQGIS**.

QGIS and Qt are written in **C++**, and when we use PyQGIS, we are actually using **Python bindings** to access those C++ classes.

---

## Why Do We Use Classes?

* Make code **modular and reusable**
* Avoid **duplicate code**
* Help organize large programs
* Hide implementation details from the user
* QGIS uses many built-in C++ classes that we access using Python

---

## What Is a Class?

* A class is a **template or blueprint**
* It defines:

  * **Properties (attributes / variables)**
  * **Functions (methods)**
* A class itself does nothing until we create an object from it

### Simple Example

Think of a **Car** class:

* The class is the blueprint
* Color and type are properties
* Start and stop are functions

---

## What Is an Object?

* An object is a **real instance of a class**
* To use a class, we must create an object from it
* Each object has its **own values and state**

**Example:**

* The class defines what a car is
* The object represents a real car

---

## Instance and Constructor

* An **instance** is an object created from a class
* The constructor initializes the object
* In Python, the constructor is called `__init__()`
* `self` refers to the **current object**

### Key Points

* `__init__()` runs automatically when an object is created
* `self` is required to access object data and methods

---

## Class vs Object

* **Class** → Blueprint
* **Object** → Actual instance created from the class
* You cannot use a class directly — you must use an object

---

## Methods

* Methods are **functions inside a class**
* Called using an **object**
* Automatically receive the current object using `self`

### Example

```python
def start(self):
    print("Car Started")
```

Calling the method from an object:

```python
my_car.start()
```

---

## Attributes

### Instance Attributes

* Belong to a **specific object**
* Defined inside the `__init__()` constructor
* Each object can have different values

### Class Attributes

* Belong to the **class itself**
* Shared by all objects
* Defined outside the `__init__()` constructor
* Can be accessed using the class name

```python
model = "Civic"
```

---

## Inheritance

* Classes can be **derived from another class**
* The derived (child) class **inherits all features** of the base (parent) class
* Used to extend or modify existing functionality

### Example

```python
class Sedan(Car):
    pass
```

---

## Inheritance in PyQGIS

* All PyQGIS classes are derived from the base class **QObject**

* Examples of QGIS class inheritance:

* `QgsMapLayer` → Base class for all map layers

* `QgsVectorLayer` → Derived from `QgsMapLayer`

* `QgsRasterLayer` → Derived from `QgsMapLayer`

* `QgsPointCloudLayer` → Derived from `QgsMapLayer`

* `QgsAuxiliaryLayer` → Derived from `QgsVectorLayer`

---

## Why This Matters for PyQGIS

* Every QGIS layer, feature, geometry, and tool is a **class**
* PyQGIS uses Python to control C++ QGIS classes
* Understanding classes makes PyQGIS **much easier and clearer**

---

## Reference Video 🎥

**Understanding Classes (PyQGIS Series)**
YouTube: [https://youtu.be/sUBnrV9McXk](https://youtu.be/sUBnrV9McXk)
Playlist: PLppGmFLhQ1HKKnk3riKNyOxb-3MTI-7zE

---

## One-Line Summary

> Classes are blueprints, objects are instances, and PyQGIS works by using Python to access C++ QGIS classes.