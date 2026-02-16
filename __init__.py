import bpy
from . import operators, ui_panels

#addon metadata:

bl_info = {
    "name": "TSM",
    "description": "Add-on for make your work easyest",
    "author": "Grok/Chat GPT/ TS",
    "version": (0, 0, 1),
    "blender": (5, 0, 1),
    "Glocation": "View3D > N - panel > UV & Material Manager",
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

)

#register function

def register():
    bpy.utils.register_class(ExchangeProperties)
    bpy.types.Scene.exchange_props = bpy.props.PointerProperty(type=ExchangeProperties)
for cls in classes:
    bpy.utils.register_class()

def unregister():

    del bpy.types.Scene.exchange_props
    bpy.utils.unregister_class(ExchangeProperties)
# entry point
if __name__ == "__main__":
    register()