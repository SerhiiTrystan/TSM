import bpy

# Utility function to get UV Maps for selected objects
def get_uv_maps(context):
    uv_maps = set()
    for obj in context.selected_objects:
        if obj.type == 'MESH':
            for uv in obj.data.uv_layers:
                uv_maps.add(uv.name)
    return [(name, name, "") for name in sorted(uv_maps)]

# Utility function to get materials (visible objects or all in scene)
def get_materials(context):
    show_all = context.scene.show_all_materials
    materials = set()
    
    if show_all:
        # Get all materials in the scene
        for mat in bpy.data.materials:
            materials.add(mat.name)
    else:
        # Get materials from visible objects
        for obj in context.scene.objects:
            if obj.type == 'MESH' and not obj.hide_viewport:
                for slot in obj.material_slots:
                    if slot.material:
                        materials.add(slot.material.name)
    
    return [(name, name, "") for name in sorted(materials)]