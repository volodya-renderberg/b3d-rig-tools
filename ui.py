# import webbrowser

import bpy

from . import working as w
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
        #
        box=col.box()
        box.label(text="Single selected object")
        row = box.row(align = True)
        row.label(text='Position and Action:')
        row.operator("rigtools.push_position_and_action", text="Push")
        row.operator("rigtools.pull_position_and_action", text="Pull")
        row = box.row(align = True)
        row.label(text='Child Offs:')
        row.operator("rigtools.push_child_off_constraints", text="Push")
        row.operator("rigtools.pull_child_off_constraints", text="Pull")
        #
        col.separator(factor=1.0)
        box=col.box()
        box.label(text="Many objects")
        row = box.row(align = True)
        row.label(text='Position and Action:')

        
class RIGTOOLS_push_position_and_action(bpy.types.Operator):
    bl_idname = "rigtools.push_position_and_action"
    bl_label = "Push position and action"

    def execute(self, context):
        # (1)
        b,r=w.push_position_and_action(context)
        if not b:
            self.report({'WARNING'}, r)
        else:
            self.report({'INFO'}, r)
        return{'FINISHED'}


class RIGTOOLS_pull_position_and_action(bpy.types.Operator):
    bl_idname = "rigtools.pull_position_and_action"
    bl_label = "Pull position and action"

    def execute(self, context):
        # (1)
        b,r=w.pull_position_and_action(context)
        if not b:
            self.report({'WARNING'}, r)
        else:
            self.report({'INFO'}, r)
        return{'FINISHED'}


class RIGTOOLS_push_child_off_constraints(bpy.types.Operator):
    bl_idname = "rigtools.push_child_off_constraints"
    bl_label = "Push Child off constraints"

    def execute(self, context):
        # (1)
        b,r=w.push_child_offs(context)
        if not b:
            self.report({'WARNING'}, r)
        else:
            self.report({'INFO'}, r)
        return{'FINISHED'}


class RIGTOOLS_pull_child_off_constraints(bpy.types.Operator):
    bl_idname = "rigtools.pull_child_off_constraints"
    bl_label = "Pull Child off constraints"

    def execute(self, context):
        # (1)
        b,r=w.pull_child_offs(context)
        if not b:
            self.report({'WARNING'}, r)
        else:
            self.report({'INFO'}, r)
        return{'FINISHED'}


### TEMPLATE
class RIGTOOLS_template_operator(bpy.types.Operator):
    bl_idname = "rigtools.template_operator"
    bl_label = "Text"

    def execute(self, context):
        # (1)
        self.report({'INFO'}, "template_operator")
        return{'FINISHED'}

def register():
    bpy.utils.register_class(RIGTOOLS_PT_main_panel)
    bpy.utils.register_class(RIGTOOLS_push_position_and_action)
    bpy.utils.register_class(RIGTOOLS_pull_position_and_action)
    bpy.utils.register_class(RIGTOOLS_push_child_off_constraints)
    bpy.utils.register_class(RIGTOOLS_pull_child_off_constraints)

    
def unregister():
    bpy.utils.unregister_class(RIGTOOLS_PT_main_panel)
    bpy.utils.unregister_class(RIGTOOLS_push_position_and_action)
    bpy.utils.unregister_class(RIGTOOLS_pull_position_and_action)
    bpy.utils.unregister_class(RIGTOOLS_push_child_off_constraints)
    bpy.utils.unregister_class(RIGTOOLS_pull_child_off_constraints)
