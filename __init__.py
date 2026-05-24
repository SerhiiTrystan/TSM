import bpy
from . import operators, ui_panels

#addon metadata:

bl_info = {
    "name": "TSM",
    "description": "Add-on for make your work easyest",
    "author": "Grok/Chat GPT/ TS",
    "version": (0, 0, 1),
    "blender": (5, 0, 1),
    "location": "View3D > N - panel > UV & Material Manager",
    "warning": "Manage UV maps and Materials for selected objects",
    "wiki_url": "github",
    "category": "Object"
}

class exchange_properties(bpy.types.PropertyGroup):
    exchange_path: bpy.props.StringProperty(
        name="Exchange Folder",
        subtype="DIR_PATH",
        default="D:/Exchange"
    )

#list of register classes
classes = (
    operators.uv_map_set_active_operator,
    operators.uv_map_create,
    operators.uv_map_delete_operator,
    operators.uv_map_rename,
    operators.material_delete,
    operators.material_select,
    operators.material_apply,
    operators.material_clear,
    operators.export_to_folder,
    operators.import_from_folder,
    operators.import_one_fbx,
    operators.clear_folder,
    operators.rename_selected_obj,
    ui_panels.uvpanel,
    ui_panels.material_panel,
    ui_panels.exchange_panel,
    ui_panels.popup_panel
)

#register function

def register():
    bpy.utils.register_class(exchange_properties)
    bpy.types.Scene.exchange_props = bpy.props.PointerProperty(type=exchange_properties)
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.uv_map_selector = bpy.props.EnumProperty(
        items=lambda self, context: [(name, name, "") for name in sorted(set(
            uv.name for obj in context.selected_objects if obj.type == 'MESH' for uv in obj.data.uv_layers
        ))],
        name="UV Maps",
        description="Select a UV Map from the list",
        update=lambda self, context: None  # Placeholder for dynamic updates
        )
        # Add custom property for material selection
    bpy.types.Scene.material_selector = bpy.props.EnumProperty(
        items=lambda self, context: [(mat.name, mat.name, "") for mat in bpy.data.materials],
        name="Materials",
        description="Select a Material from the list",
        update=lambda self, context: None
    )
        # Add toggle for material list scope
    bpy.types.Scene.show_all_materials = bpy.props.BoolProperty(
        name="Show All Materials",
        description="Toggle between showing materials on visible objects or all materials in the scene",
        default=False
    )
        # Add property for new UV Map name
    bpy.types.Scene.new_uv_map_name = bpy.props.StringProperty(
        name="UV Map Name",
        description="Name for creating or renaming a UV Map",
        default="UVMap_New"
    )

def unregister():

    del bpy.types.Scene.exchange_props
    bpy.utils.unregister_class(exchange_properties)
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.uv_map_selector
    del bpy.types.Scene.material_selector
    del bpy.types.Scene.show_all_materials
    del bpy.types.Scene.new_uv_map_name

# entry point
if __name__ == "__main__":
    register()
