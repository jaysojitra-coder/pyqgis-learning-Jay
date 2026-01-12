# QgsDistanceArea – Distance & Area Calculation (PyQGIS)

## Overview
`QgsDistanceArea` is a general-purpose class in PyQGIS used to calculate
distances and areas. It supports **ellipsoid-based calculations**, which
provide accurate real-world measurements on the Earth's surface.

Official Documentation (QGIS 3.40):  
https://qgis.org/pyqgis/3.40/core/QgsDistanceArea.html

---

## Why Use QgsDistanceArea?
- Accurate distance calculation on Earth
- Works with latitude/longitude coordinates
- Supports ellipsoidal algorithms (Vincenty formulas)
- Useful for GIS analysis, automation, and plugins

---

## Important Concept: Ellipsoid
When a valid ellipsoid is set, calculations are performed using
ellipsoidal math instead of flat (planar) geometry.

Common ellipsoid:
- **WGS84** (used by GPS and EPSG:4326)

## Reference Video 🎥 
Calculating Distance Using PyQGIS
By Ujaval Gandhi
Link👉 https://youtu.be/AXoCea7ryAA?list=PLppGmFLhQ1HKKnk3riKNyOxb-3MTI-7zE


```python
d.setEllipsoid('WGS84')


 
