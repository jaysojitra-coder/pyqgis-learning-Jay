## 2. Hello PyQGIS 🐍🌍
** Script Name: delete_attribute.py**

### What is PyQGIS?

**PyQGIS** is the Python API for QGIS.
It allows you to control QGIS using Python instead of clicking buttons.

With PyQGIS you can:

* Automate GIS workflows
* Edit layers programmatically
* Create custom tools & plugins
* Process large datasets faster

---

### Requirements

* **QGIS Version:** 3.40 LTR
* Open QGIS → `Plugins → Python Console`
* Click **Show Editor** to write code

---

### Reference Video 🎥

**Hello PyQGIS – Attribute Editing**
YouTube: [https://youtu.be/7xNNpGoYK9Q](https://youtu.be/7xNNpGoYK9Q)
Playlist: PLppGmFLhQ1HKKnk3riKNyOxb-3MTI-7zE

---

### Example Task

Delete the **2nd attribute column** (`SDE_SFGIS_`) from a vector layer.

⚠️ Make sure the layer is **selected** before running code.

---

### Important Notes

* Attribute indexes start at **0**
* You must **start editing** before making changes
* Use `commitChanges()` to save
* Use `rollback()` to cancel changes

---

### Key Takeaways ✅

* PyQGIS can do everything the GUI can
* Python makes GIS work repeatable and fast
* Notes help you remember *why* code works
