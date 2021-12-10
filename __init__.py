#
#
#
#

bl_info = {
    "name": "Rig Tools",
    "description": "Other toolsa.",
    "author": "Volodya Renderberg",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3d tools panel",
    "warning": "", # used for warning icon and text in addons panel
    "doc_url":"",
    "category": "Rigging"}

if "bpy" in locals():
    import importlib
    importlib.reload(ui)
else:
    from . import ui

import bpy


##### REGISTER #####

def register():
    ui.register()

def unregister():
    ui.unregister()

if __name__ == "__main__":
    register()

