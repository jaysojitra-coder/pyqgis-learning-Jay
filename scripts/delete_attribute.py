# Week 1 Hello PyQGIS Script
# Delete the 2nd attribute column from the active layer in QGIS

layer = iface.activeLayer()

if not layer:
    raise Exception("No active layer selected")

# Start editing mode
layer.startEditing()

# Delete the 2nd attribute (index starts at 0)
layer.deleteAttribute(1)

# Commit changes (save permanently)
layer.commitChanges()

print("Attribute deleted successfully")
