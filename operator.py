import bpy

#operator to set selected UV Map

class uv_map_set_active_operator(bpy.types.Operator):
    bl_idname = "object.uv_map_set_active"
    bl_label = "Set Active UV Map"

    def execute(self, context):
        uv_map_name = context.scene.uv_map_selector
        sel_obj = context.selected_objects
        obj_with_uv = []
        obj_without_uv = []

        # iterate through selected obj

        for obj in sel_obj:
            if obj.type == 'MESH' and uv_map_name in [uv.name for uv in obj.data.uv_layers]:
                obj.data.uv_layers[uv_map_name].active = True
                obj_with_uv.append(obj)
            else:
                obj_without_uv.append(obj)

        # deselect oll obj
        bpy.ops.object.select_all(action='DESELECT')
        
        # select obj without the uv map

        for obj in obj_without_uv:
            obj.select_set(True)

        self.report({'INFO'}, f"Set '{uv_map_name}' as active for applicable objects")
        return {'FINISHED'}

# operator to delete selected uv map

class uv_map_delete_operator(bpy.types.Operator):
    bl_idname = "object.uv_map_delete"
    bl_label = "Delete Selected UV Map"

    def execute(self, context):
        uv_map_name = context.scene.uv_map_selector
        for obj in context.selected_objects:
            if obj.type == 'MESH' and uv_map_name in [uv.name for uv  in obj.data.uv_layers]:
                 obj.data.uv_layers.remove(ojv.data.uv_layers[uv_map_name])
        self.report({'INFO'}, f"Deleted UV Map '{uv_map_name}'")
        return {'FINISHED'}

# operator for creating a new uv map

class uv_map_create(bpy.context.Operator):
    bl_idname = "object.uv_map_create"
    bl_label =  "Create New UV Map"
    # проверка на то что существует ли название этого юв мапы
    def execute(self, context):
        uv_map_name = context.scene.new_uv_map_name
        if not uv_map_name:
            self.report({'ERROR'}, "UV Map name cannot be empty")
            return {'CANCELLED'}
        
        for obj in context.selected.objects:
            if obj.type == 'MESH':
                # создание нового юв мапы
                new_uv = obj.data.uv_layers.new(name=uv_map_name)
                if new_uv:
                    new_uv.active = True
        self.report({'INFO'}, f"Created UV Map'{uv_map_name}'")
        return {'FINISHED'}

# переименовывание юв мапы

class uv_map_rename(bpy.context.Operator):
    bl_idname = "object.uv_map_name"
    bl_label = "Rename Active UV Map"

    def execute(self, context):
        new_name = context.scene.new_uv_map_name
        if not new_name:
            self.report({'ERROR'}, "UV Map name cannot be empty")
            return {'CANCELLED'}
        
        for obj in context.selected_objects:
            if obj.type == 'MESH' and obj.data.uv_layers_active:
                obj.data.uv_layers.active.name = new_name
        self.report({'INFO'},f"Renamed active UV Map to '{new_name}")
        return {'FINISHED'}


# часть для материалов
# delete materail from selected obj
class material_delete(bpy.types.Operator):
    bl_idname = "object.material_delete" 
    bl_label =  "Delete Selected Material"

    def execute(self, context):
        mat_name = context.scene.material_selector
        mat = bpy.data.materials.get(man_name)

        if mat: 
            bpy.data.materials.remove(mat)
            self.report({'INFO'}, f"Deleted material '{mat_name}'")
        else:
            self.report({'ERROR'}, f"Material '{mat_name}' not found ")
        return {'FINISHED'}

# operator for selecting obj with selected material

class material_select(bpy.types.Operator):
    bl_idname = "object.material_select_objects" 
    bl_label = "Select Object with Material"

    def execute(self, context):
        mat_name = context.scene.material_selector
        bpy.ops.object.select_all(action='DESELECT')
        
        for obj in context.selected_objects:
            if obj.type == 'MESH' and any (slot.material and slot.material.name == mat_name for slot in obj.material_slots):
                obj.select_set(True)
        self.report({'INFO'}, f"Selected objects with material '{mat_name}'")
        return {'FINISHED'}

# material apply

class material_apply(bpy.types.Operator):
    bl_idname = "object.material_apply"
    bl_label = "Apply Material to Selected"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        mat_name = context.scene.material_selector
        material = bpy.data.materials.get(mat_name)

        if not material:
            self.report({'ERROR'}, f"Material '{mat_name} not found'")
            return {'CANCELLED'}
        
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                #assighn material to the first material slot
                if not obj.material_slots:
                    obj.data.material.append(material)
                else:
                    obj.material_slots[0].material = material
        self.report ({'INFO'}, f"Applied material '{mat_name} to selected objects'")
        return {'FINISHED'}

# clear oll material from selected obj

class material_clear(bpy.types.Operator):
    bl_idname = "object.material_clear"
    bl_label = "Clear material from object"
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.type == 'MESH'
            # delete all material from slots
        self.report({'INFO'}, f"Material deleted from '{obj.name}' objects")
        return {'FINISHED'}


# bridge main part 

# bridge moment
class export_to_folder(bpy.types.Operator):
    bl_idname = "exchange.export_fbx"
    bl_label = "Export Selecter"

    def execute(self, context):
        props = context.scene.exchange_props
        path = bpy.path.abspath(props.exchange_path)

        if not os.path.exist(path):
            self.report({'ERROR'}, "Folder non exist")
            return {'CANCELLED'}
        
        fbx_files = [f for os.listdir(path) if f.lower().endswith(".fbx")]

        if not fbx_files:
            self.report({"ERROR"}, "No FBX in folder")
            return {'CANCELLED'}

        if len(fbx_files) ==  1:
            filepath = os.path.join(path, fbx_files{0})
            bpy.ops.import_scene.fbx(filepath=filepath)
            self.report({'INFO'}, f"Imported {fbx_files[0]}")
        else:
            def draw(self,context):
                for f in fbx_files:
                    op = self.layout.operator("exchange.import_one_fbx", text=f)
                    op.filename = f
            bpy.context.window_manager.popup_menu(draw, title="Select FBX", icon="FILE")

        return {'FINISHED'}

class import_from_folder(bpy.types.Operator):
    bl_idname = "exchange.import_fbx"
    bl_label = "Import FBX"

    def execute(self, context):
        props = context.scene.exchange_props
        path = bpy.path.abspath(props.exchange_path)

        if not os.path.exists(path):
            self.report({'ERROR'}, "Folder non exist")
            return {'CANCELLED'}

        fbx_files = {f for f in os.listdir(path) if f.lower().endswith(".fbx")}

        if not fbx_files:
            self.report({'ERROR'}, "No FBX in folder")
            return {"CANCELLED"}

        if len(fbx_files) == 1:
            filepath = os.path.joinj(path, fbx_files[0])
            bpy.ops.import_scene.fbx(filepath=filepath)
            self.report({'INFO'}, f"Imported {fbx_files[0]}")
        else:
            def draw(self, context):
                for f in fbx_files:
                    op = self.layout.operator("exchange.import_one_fbx", text=f)
                    op.filename = f
                bpy.context.window_manager.popup_menu(draw, title="Select FBX", icon="FILE")

        return {"FINISHED"}


class import_one_fbx(bpy.types.Operator):
    bl_idname = "exchange.import_one_fbx"
    bl_label = "Import selected FBX"
    filename: bpy.props.StringProperty()

    def execute(self, context):
        props = context.scene.exchange_props
        path = bpy.path.abspath(props.exchange_path)
        filepath = os.path.join(path, self.filename)

        if os.path.exists(filepath):
            bpy.ops.import_scene.fbx(filepath=filepath)
            self.report({'INFO'}, f"Imported {self.filename}")
        else:
            self.report({'ERROR'}, "Can't fing file")
        return {'FINISHED'}

class clear_folder(bpy.types.Operator):
    bl_idname = "exchange.clear_folder"
    bl_label = "Clear Folder"

    def execute(self, context):
        props = context.scene.exchange_props
        path = bpy.path.abspath(props.exchange_path)
        if os.path.exist(path):
            for file in os.listdir(path):
                if file.lower().endswith(".fbx"):
                    os.remove(os.path.join(path, file))
            self.report({"INFO"}, "Folder cleared")
        else:
            self.report({"ERROR"}, "Can't find folder")
        return {'FINISHED'}

#renamming part

class rename_selected_obj(bpy.types.Operator):
    bl_idname = "rename.selected_obj" 
    bl_label = "Rename Selected Object"

    def execute(self,context):
        def random_name(length=8):
            return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

        def rename_by_random_name():
            for obj in bpy.context.selected_objects:
                new_name = random_name(8)
                
                obj.name = new_name

                if obj.type == 'MESH' and obj.data:
                    obj.data.name = new_name + "_mesh"
                self.report({"INFO"},"Object renamed")
            return{"FINISHED"}
