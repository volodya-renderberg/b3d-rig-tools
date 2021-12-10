# import webbrowser

import bpy

# from . import funcs as fn
# from . import settings


class RIGTOOLS_PT_main_panel(bpy.types.Panel):
    bl_label = 'Rig tools:'
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Rig tools'

    def draw(self, context):        
        layout = self.layout
        
        col = layout.column(align = True)
        row = col.row(align = True)
        row.label(text='Tools')

        


def register():
    bpy.utils.register_class(RIGTOOLS_PT_main_panel)

    
def unregister():
    bpy.utils.unregister_class(RIGTOOLS_PT_main_panel)
