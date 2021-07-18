bl_info = {
    "name": "Body Editor Addon",
    "author": "Viviana Pentangelo",
    "version": (1, 0),
    "blender": (2, 90, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Edit your body mesh",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

import bpy
import bmesh


class BodyEditorPanel(bpy.types.Panel):
    bl_label = "Body Editor"
    bl_idname = "body_editor"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Body Editor Tool"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("wm.bodyedit",
                     icon='OUTLINER_OB_ARMATURE')


# Operator
class WM_OT_bodyEdit(bpy.types.Operator):
    bl_label = "Edit Body"
    bl_idname = "wm.bodyedit"

    head = bpy.props.FloatProperty(name="Head:", default=1, min=0.1)
    torso = bpy.props.FloatProperty(name="Torso:", default=1, min=0.1)
    hips = bpy.props.FloatProperty(name="Hips:", default=1, min=0.1)
    leg = bpy.props.FloatProperty(name="Leg:", default=1, min=0.1)
    calves = bpy.props.FloatProperty(name="Calves:", default=1, min=0.1)
    shoulders = bpy.props.FloatProperty(name="Shoulders:", default=1, min=0.1)
    arms = bpy.props.FloatProperty(name="Arms:", default=1, min=0.1)
    forearms = bpy.props.FloatProperty(name="Forearms:", default=1, min=0.1)
    height = bpy.props.FloatProperty(name="Height:", default=1, min=0.1)

    def execute(self, context):
        hd = self.head
        t = self.torso
        l = self.leg
        c = self.calves
        s = self.shoulders
        a = self.arms
        fa = self.forearms
        hp = self.hips
        h = self.height

        ob = bpy.context.object
        me = ob.data
        is_editmode = me.is_editmode

        bpy.ops.object.mode_set(mode='EDIT')

        # HEAD
        ob.vertex_groups.active = ob.vertex_groups["Head"]
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.vertex_group_select()
        vgVerts = [v for v in ob.data.vertices if v.select]

        bpy.ops.transform.resize(
            value=(hd, hd, hd),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            mirror=True,
            use_proportional_edit=True,
            proportional_edit_falloff='SMOOTH',
            proportional_size=0.18,
            use_proportional_connected=False,
            use_proportional_projected=False
        )

        # TORSO
        ob.vertex_groups.active = ob.vertex_groups["Torso"]
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.vertex_group_select()
        vgVerts = [v for v in ob.data.vertices if v.select]

        bpy.ops.transform.resize(
            value=(t, t, 1),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            mirror=True,
            use_proportional_edit=True,
            proportional_edit_falloff='SMOOTH',
            proportional_size=0.18,
            use_proportional_connected=False,
            use_proportional_projected=False
        )

        # LEGS
        ob.vertex_groups.active = ob.vertex_groups["Leg"]
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.vertex_group_select()
        vgVerts = [v for v in ob.data.vertices if v.select]

        bpy.ops.transform.resize(
            value=(l, l, l),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            mirror=True,
            use_proportional_edit=True,
            proportional_edit_falloff='SMOOTH',
            proportional_size=0.163508,
            use_proportional_connected=False,
            use_proportional_projected=False
        )

        # CALVES
        ob.vertex_groups.active = ob.vertex_groups["Calves"]
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.vertex_group_select()
        vgVerts = [v for v in ob.data.vertices if v.select]

        bpy.ops.transform.resize(
            value=(c, c, c),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            mirror=True,
            use_proportional_edit=True,
            proportional_edit_falloff='SMOOTH',
            proportional_size=0.15,
            use_proportional_connected=False,
            use_proportional_projected=False
        )

        # SHOULDERS
        ob.vertex_groups.active = ob.vertex_groups["Shoulder"]
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.vertex_group_select()
        vgVerts = [v for v in ob.data.vertices if v.select]

        bpy.ops.transform.resize(
            value=(s, s, s),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            mirror=True,
            use_proportional_edit=True,
            proportional_edit_falloff='SMOOTH',
            proportional_size=0.20,
            use_proportional_connected=False,
            use_proportional_projected=False
        )

        # HIPS
        ob.vertex_groups.active = ob.vertex_groups["Hips"]
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.vertex_group_select()
        vgVerts = [v for v in ob.data.vertices if v.select]

        bpy.ops.transform.resize(
            value=(hp, hp, hp),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            mirror=True,
            use_proportional_edit=True,
            proportional_edit_falloff='SMOOTH',
            proportional_size=0.24,
            use_proportional_connected=False,
            use_proportional_projected=False
        )

        # ARMS
        ob.vertex_groups.active = ob.vertex_groups["Arm"]
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.vertex_group_select()
        vgVerts = [v for v in ob.data.vertices if v.select]

        bpy.ops.transform.resize(
            value=(a, a, a),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            mirror=True,
            use_proportional_edit=True,
            proportional_edit_falloff='SMOOTH',
            proportional_size=0.1,
            use_proportional_connected=False,
            use_proportional_projected=False
        )

        # FOREARMS
        ob.vertex_groups.active = ob.vertex_groups["Forearm"]
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.vertex_group_select()
        vgVerts = [v for v in ob.data.vertices if v.select]

        bpy.ops.transform.resize(
            value=(fa, fa, fa),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            mirror=True,
            use_proportional_edit=True,
            proportional_edit_falloff='SMOOTH',
            proportional_size=0.1,
            use_proportional_connected=False,
            use_proportional_projected=False
        )

        bpy.ops.object.editmode_toggle()

        # HEIGHT
        bpy.ops.transform.resize(
            value=(h, h, h),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            mirror=True,
            use_proportional_edit=False,
        )

        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

        # EXPORT
        exportPath = r"C:\Users\39347\Documents\GitHub\3D-Human-Body-Generator\projectexports\generatedbody.fbx"
        bpy.ops.export_scene.fbx(filepath=exportPath, use_selection=False)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


def register():
    bpy.utils.register_class(BodyEditorPanel)
    bpy.utils.register_class(WM_OT_bodyEdit)


def unregister():
    bpy.utils.unregister_class(BodyEditorPanel)
    bpy.utils.unregister_class(WM_OT_bodyEdit)


if __name__ == "__main__":
    register()