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
import sys

argv = sys.argv
argv = argv[argv.index("--") + 1:]

hd = float(argv[0]) / 0.57
t = float(argv[1]) / 0.76
l = float(argv[2]) / 0.59
c = float(argv[3]) / 0.36
s = float(argv[4]) / 0.95
a = float(argv[5]) / 0.28
fa = float(argv[6]) / 0.25
hp = float(argv[7]) / 0.86
h = float(argv[8]) / 1.765

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
exportPath = r"..\projectexports\generatedbody.glb"
bpy.ops.export_scene.gltf(filepath=exportPath, use_selection=False)
