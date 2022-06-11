import bpy

from .functions import generate_mech_mesh

# from .functions import

class COMBINEDMECHMESH_OT_generate_combined_mech_mesh(bpy.types.Operator):
    bl_idname = "COMBINEDMECHMESH.generate_combined_mech_mesh"
    bl_label = "Generate Combined Mech Mesh"
    bl_description = "generate mech mesh from active armature's children."
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if bpy.context.object is None:
            return False

        if bpy.context.object.type == "ARMATURE":
            return True
        return False

    def execute(self, context):

        generate_mech_mesh(bpy.context.object)
        
        return {'FINISHED'}



def generate_combined_mech_mesh_menu(self, context):
    self.layout.operator(COMBINEDMECHMESH_OT_generate_combined_mech_mesh.bl_idname, icon='OUTLINER_OB_ARMATURE')


classes = [COMBINEDMECHMESH_OT_generate_combined_mech_mesh]


def register():
    for target_class in classes:
        bpy.utils.register_class(target_class)

    bpy.types.VIEW3D_MT_object_convert.prepend(generate_combined_mech_mesh_menu)


def unregister():
    for target_class in classes:
        bpy.utils.unregister_class(target_class)
    
    bpy.types.VIEW3D_MT_object_convert.remove(generate_combined_mech_mesh_menu)
