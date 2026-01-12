"""
Distance Calculation Using QgsDistanceArea (PyQGIS)

This script calculates the ellipsoidal distance between two geographic
coordinates (latitude/longitude) using the WGS84 ellipsoid.

Author: Jay Sojitra
"""

from qgis.core import QgsDistanceArea, QgsPointXY

# ----------------------------------------------------
# Coordinates (Latitude, Longitude)
# ----------------------------------------------------
san_francisco = (37.7749, -122.4194)
new_york = (40.6610, -73.9440)

# ----------------------------------------------------
# Create QgsDistanceArea object
# ----------------------------------------------------
distance_calc = QgsDistanceArea()

# Set ellipsoid for accurate earth-based calculations
distance_calc.setEllipsoid('WGS84')

# ----------------------------------------------------
# Unpack coordinates
# QgsPointXY expects (X, Y) -> (Longitude, Latitude)
# ----------------------------------------------------
lat1, lon1 = san_francisco
lat2, lon2 = new_york

point1 = QgsPointXY(lon1, lat1)
point2 = QgsPointXY(lon2, lat2)

# ----------------------------------------------------
# Measure distance (result in meters)
# ----------------------------------------------------
distance_meters = distance_calc.measureLine([point1, point2])

# Convert meters to kilometers
distance_km = distance_meters / 1000

# ----------------------------------------------------
# Output
# ----------------------------------------------------
print(f"Distance between San Francisco and New York: {distance_km:.2f} km")

'''
output:
Distance between San Francisco and New York: 4145.45 km
'''