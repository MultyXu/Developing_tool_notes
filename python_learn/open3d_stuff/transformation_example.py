import open3d as o3d
import numpy as np
import copy

mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()
mesh_tx = copy.deepcopy(mesh).translate((1.3, 0, 0))
mesh_ty = copy.deepcopy(mesh).translate((0, 1.3, 0))
print(f'Center of mesh: {mesh.get_center()}')
print(f'Center of mesh tx: {mesh_tx.get_center()}')
print(f'Center of mesh ty: {mesh_ty.get_center()}')
# o3d.visualization.draw_geometries([mesh, mesh_tx, mesh_ty])

# rotate the mesh around the z-axis
mesh_trans = copy.deepcopy(mesh)
T = np.eye(4)
T[:3, :3] = mesh.get_rotation_matrix_from_xyz((np.pi / 4, np.pi / 4, 0))
T[0, 3] = 1.5 # move 1 meter in x direction
mesh_trans.transform(T)
o3d.visualization.draw_geometries([mesh, mesh_trans])