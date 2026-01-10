## 2. Hello PyQGIS 🐍🌍

### What is PyQGIS?

* **PyQGIS** is the Python API for QGIS.
* Almost everything you can do in QGIS GUI can be done using Python.
* Used for **automation, custom tools, plugins, and batch GIS tasks**.

---

### Task Example: Delete an Attribute Column Using Python

**Goal:** Delete the 2nd column (`SDE_SFGIS_`) from `shoreline.shp` using PyQGIS.

> ⚠️ Make sure the `shoreline` layer is selected before running the script.

---

### PyQGIS Code

```python
layer = iface.activeLayer()  # Select layer 
layer.startEditing()         # start Editing (mean click the edit button)
layer.deleteAttribute(1)     # Deledt the attribute by which index
layer.commitChanges()        # Then do the cmmmit then change ( As Git )

layer .rollback()      # rollback the Like Undo ( is not deleted uness you commit 
```

---

### Code Explained (One-Line Notes)

* `iface.activeLayer()` → Gets the currently selected layer in QGIS
* `startEditing()` → Puts the layer into edit mode
* `deleteAttribute(1)` → Deletes the 2nd column (index starts at 0)
* `commitChanges()` → Saves edits and exits edit mode

---

### Alternative (With Confirmation Dialog)

```python
layer = iface.activeLayer()
iface.vectorLayerTools().startEditing(layer)
layer.deleteAttribute(1)
iface.vectorLayerTools().stopEditing(layer)
```

* Uses **QgsVectorLayerTools**
* Shows a **confirmation popup** before saving edits

---

### Key Takeaways

* PyQGIS allows **programmatic editing** of GIS data
* Attribute indexes start from **0**
* Always **start editing before changes** and **commit after**
* Python = faster, repeatable GIS workflows 🚀
