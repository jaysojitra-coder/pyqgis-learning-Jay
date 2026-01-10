# Week 1 – Understanding Classes (PyQGIS Foundation)

This week, I am learning **Classes and Objects**, which are very important before starting PyQGIS.

QGIS and Qt are written in **C++**, and when we use PyQGIS, we are actually using **Python bindings** to access those C++ classes.

---

## Why Do We Use Classes?

* Makes code **modular and reusable**
* Avoids **duplicate code**
* Helps organize large programs
* Hides implementation details from the user
* QGIS uses many built-in C++ classes that we access using Python

---

## What Is a Class?

* A class is a **template or blueprint**
* It defines **properties (variables)** and **functions (methods)**
* A class itself does not do anything until we create an object from it

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

Example:

* The class defines what a car is
* The object represents a real car

---

## Instance and Constructor

* An **instance** is an object created from a class
* The constructor initializes the object
* In Python, the constructor is called `__init__()`
* `self` refers to the current object

Key points:

* `__init__()` runs automatically when the object is created
* `self` is required to access object data

---

## Class vs Object

* **Class** → blueprint
* **Object** → actual thing created from the class
* You cannot use a class directly — you must use an object

---

## Why This Matters for PyQGIS

* Every QGIS layer, feature, geometry, and tool is a **class**
* PyQGIS uses Python to control C++ QGIS classes
* Understanding classes makes PyQGIS much easier

---

## Reference Video 🎥

**Understanding Classes (PyQGIS Series)**
YouTube: [https://youtu.be/sUBnrV9McXk](https://youtu.be/sUBnrV9McXk)
Playlist: PLppGmFLhQ1HKKnk3riKNyOxb-3MTI-7zE

---

## One-Line Summary

> Classes are blueprints, objects are instances, and PyQGIS works by using Python to access C++ QGIS classes.


# Working(continuos)