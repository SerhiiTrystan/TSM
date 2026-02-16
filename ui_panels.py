import bpy
from . import utils, operator

#panel for uv map managment

class uvpanel(bpy.types.Panel):
    bl_label = "TS UV"
    bl_idname = "PT_UVPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'TSM'

    def draw(self, context):
        layout = self.layout
        layout = label(text="UV Map Managment", icon='UV')
        #dinamic uv map list
        layout.prop(context.scene, "uv_map_selector", text="UV Maps")
        
        #buttons for UV map operations
        layout.operator("object.uv_map_set_active", text="Set Active UV Map")
        layout.operator("object.uv_map_delete", text="Delete Selected UV Map")
        
        #new uv map creation and renaming
        layout.prop(context.scene, "new_uv_map_name", text="UV Map Name")
        layout.operator("object.uv_map_create", text="Create New Uv Map")
        layout.operator("object.uv_map_rename", text="Rename Active UV Map")


class material_panel(bpy.types.Panel):
    bl_label = "TSMaterial"
    bl_idname = "PT_MaterialPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'TSM'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Material Managment", icon='MATERIAL')

        layout.prop(context.scene, "show_all_materials", text="Show All Scene Materials")

        layout.prop(context.scene, "material_selector", text="Materials")
        #buttons
        layout.operator("object.material_delete", text="Delete Selected Material")
        layout.operator("object.material_select_objects", text="Select Objects with Material")
        layout.operator("object.material_apply", text="Apply Material to Selected")
        layout.operator("object.material_clear", text="Clear Material")

#tsb
class exchange_panel(bpy.types.Panel):
    bl_label = "TSBridge"
    bl_idname = "exhange_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type "UI"
    bl_category = "TSM"

    def draw(self, context):
        layout = self.layout
        props = context.scene.exchange_props

        layout.prop(props, "exchange_path")
        layout.separator()
        layout.operator("exchange.export_fbx", icon="EXPORT")
        layout.operator("exchange.import_fbx", icon="IMPORT")
        layout.operator("exchange.clear_folder", icon="TRASH")

class add_tool_panel(bpy.types.Panel):
    bl_label = "TSBridge"
    bl_idname = "add_tools"
    bl_space_type = "VIEW_3D"
    bl_region_type "UI"
    bL_category = "TSM"

    def draw(self, context):
        layout = self.layout
        
