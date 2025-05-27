import numpy as np
import open3d as o3d
from glob import glob
import os
from tqdm import tqdm
from matplotlib import pyplot as plt
from scipy.spatial.transform import Rotation as R

def build_full_scene_pcd(depth, image, hfov):
    height, width = depth.shape

    cx = (width - 1.) / 2.
    cy = (height - 1.) / 2.
    fx = (width / 2.) / np.tan(np.deg2rad(hfov / 2.))
    # fy = (height / 2.) / np.tan(np.deg2rad(self.args.hfov / 2.))

    x = np.arange(0, width, 1.0)
    y = np.arange(0, height, 1.0)
    u, v = np.meshgrid(x, y)
    
    # Apply the mask, and unprojection is done only on the valid points
    valid_mask = depth > 0
    masked_depth = depth[valid_mask]
    u = u[valid_mask]
    v = v[valid_mask]

    # Convert to 3D coordinates
    x = (u - cx) * masked_depth / fx
    y = (v - cy) * masked_depth / fx
    z = masked_depth

    # Stack x, y, z coordinates into a 3D point cloud
    points = np.stack((x, y, z), axis=-1)
    points = points.reshape(-1, 3)
    
    # temp transform to x forward
    T = np.array([[0, 0, 1],
                  [-1, 0 , 0],
                  [0, -1, 0]])
    points = (T @ points.T).T
    # temp transform to x forward
    
    # Perturb the points a bit to avoid colinearity
    points += np.random.normal(0, 4e-3, points.shape)

    color_mask = np.repeat(valid_mask[:, :, np.newaxis], 3, axis=2)
    image_flat = image[color_mask].reshape(-1, 3)  # Flatten the image array for easier indexing
    colors = image_flat / 255.0  # Normalize the colors

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    pcd.colors = o3d.utility.Vector3dVector(colors)
    
    camera_object_pcd = pcd.voxel_down_sample(0.05)

    return camera_object_pcd

# dir = 'QaLdnwvtxbs_53'
# dir = 'offline_data_1'
dir = 'offline_data 2'
# dir = 'python_learn/offline_data'
# dir = 'python_learn/QaLdnwvtxbs_53'
all_rgb = glob(os.path.join(dir, 'rgb', '*.png'))
all_depth = glob(os.path.join(dir, 'depth', '*.npy'))
all_pose = np.load(os.path.join(dir, 'pose.npy'))
all_rgb.sort()
all_depth.sort()

# NUM_FRAMES = len(all_rgb)
NUM_FRAMES = 1

for i in tqdm(range(NUM_FRAMES)):
    rgb = o3d.io.read_image(all_rgb[i])
    depth = np.load(all_depth[i])
    # print(depth.shape)
    depth = depth.astype(np.float32)
    # depth /= max(depth.max(), 1e-6)
    depth /= 1000
    # depth = np.expand_dims(depth, axis=-1)
    # print(depth.shape)
    # plt.imshow(depth[:, :, 0])
    # plt.show()
    
    # filtering
    # depth = depth[:, :, 0] * 1
    # mask2 = depth > 3
    # depth[mask2] = 0.
    # depth = depth * 5

    pcd = build_full_scene_pcd(depth, np.asarray(rgb), 69)
    # print(np.array(pcd.points).shape)
    camera_matrix_T = all_pose[i].reshape(4, 4)
    # print("pose:", camera_matrix_T[:3, 3])
    r = R.from_matrix(camera_matrix_T[:3, :3])
    # print("euler:", r.as_euler('xyz', degrees=True))
    pcd.transform(camera_matrix_T)
    if i == 0:
        full_pcd = pcd
    else:
        full_pcd += pcd

# create height cut
# full_pcd = full_pcd.select_by_index(np.where(np.asarray(full_pcd.points)[:, 2] < 0.7)[0]) 
# full_pcd = full_pcd.paint_uniform_color([0.5, 0.5, 0.5])
# full_pcd = full_pcd.voxel_down_sample(0.03)
# camera view point 

# # Create a visualizer
# vis = o3d.visualization.Visualizer()
# vis.create_window()

# # Add the point cloud
# vis.add_geometry(full_pcd)

# # Get the view control
# view_ctl = vis.get_view_control()
# camera_params = view_ctl.convert_to_pinhole_camera_parameters()

# # Set the specified camera position
# # camera_params.extrinsic[:3, 0] = [0.72361005835869074, 0.60859090686769046, 0.32558499891747827]  # Front vector
# # camera_params.extrinsic[:3, 1] = [-0.52446660005754031, 0.7914818686428079, -0.31383313565296639]  # Up vector
# # camera_params.extrinsic[:3, 3] = [-1.8285146131229937, -0.14885291838881823, -1.1543190712718705]  # Lookat position

# # Create a new intrinsic matrix with the orthogonal effect
# new_intrinsic_matrix = np.array([
#     [100, 0, 400],
#     [0, 100, 400],
#     [0, 0, 1]
# ])

# # Set the new intrinsic matrix
# camera_params.intrinsic.intrinsic_matrix = new_intrinsic_matrix

# # Apply the modified camera parameters
# view_ctl.convert_from_pinhole_camera_parameters(camera_params)

# # Render
# vis.run()
# vis.destroy_window()


camera_param = {
			"boundingbox_max" : [ 10.099617275558431, 6.0505387186625565, 3.0085105098126088 ],
			"boundingbox_min" : [ -1.1839770227755073, -4.3052503027571074, -1.2626544490782075 ],
			"field_of_view" : 60.0,
			"front" : [ -0.83268152796408268, -0.51566160346944223, 0.20182810432326917 ],
			"lookat" : [ 1.2321365330497136, 0.27675874715552889, 0.26716443822834512 ],
			"up" : [ 0.21892863661803183, 0.028219518020234556, 0.97533271803588928 ],
			"zoom" : 0.27600000000000019
		}

o3d.visualization.draw_geometries([full_pcd], 
                                  zoom=camera_param['zoom'],
                                  front=camera_param['front'],
                                  lookat=camera_param['lookat'],
                                  up=camera_param['up'],)