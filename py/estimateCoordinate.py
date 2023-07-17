import math
import json
#from scipy.spatial.transform import Rotation as R
import numpy as np
import matplotlib.pyplot as plt


# Estimate vector between 2 cameras and convert it to pitch and yaw for display in Pannellum
def point_camera(camera_pos, camera_target):
    x1, y1, z1 = camera_target
    x2, y2, z2 = camera_pos

    # Normal coordinates
    direction_x = x2 - x1
    direction_y = y2 - y1
    direction_z = z2 - z1

    # Rearange cameras coordinate because they are display along axis Z
    tampon = direction_z
    direction_z = direction_y
    direction_y = direction_x
    direction_x = tampon

    # Estimate pitch and yaw based on traslation coordinate
    pitch = math.atan2(direction_z, math.sqrt(direction_x**2 + direction_y**2))
    yaw = math.atan2(direction_y, direction_x)

    # convert into deggree ( unit used in Pannellum)
    pitch_deg = math.degrees(pitch)
    yaw_deg = math.degrees(yaw)

    return pitch_deg,yaw_deg

#########################################################################################################################################

# load reconstruction.json
with open('../json/coordinates_rota_trans.json') as file:
    data = json.load(file)

# Extract datas from shots
rotation_data = data['rotation']
translation_data = data['translation']
neighbors_data = data['neighbors']

i = 0
j = 0

neighbor_pitch_yaw = []
# Compute pitch and yaw for every images and put it into array to use it in json
for i in range((len(neighbors_data))): 

    img = str(i)
    compute_tab = []
    
    for j in range(len(neighbors_data[img])):

        tab = []
        camera_pos = translation_data[i]
        id_camera_dest = neighbors_data[img][j]
        camera_dest = translation_data[id_camera_dest]
        pitch,yaw = point_camera(camera_pos, camera_dest)
        tab.append(pitch)
        tab.append(yaw)
        
        compute_tab.append(tab)

    neighbor_pitch_yaw.append(compute_tab)
        

# load json destination
with open('../json/coordinates_rota_trans.json') as dest_file:
    dest_data = json.load(dest_file)


dest_data['neighbor_pitch_yaw'] = neighbor_pitch_yaw
# Add all the datas to this file
with open('../json/coordinates_rota_trans.json', 'w') as dest_file:
    json.dump(dest_data, dest_file, indent=4)





"""


def angle_axis_to_matrix(angle, axis):
    # Normalize the axis vector
    axis = axis / np.linalg.norm(axis)
    
    # Compute sine and cosine of the angle
    c = np.cos(angle)
    s = np.sin(angle)
    
    # Construct the skew-symmetric matrix
    kx, ky, kz = axis
    A = np.array([[0, -kz, ky],
                  [kz, 0, -kx],
                  [-ky, kx, 0]])
    
    # Compute the rotation matrix using Rodrigues' rotation formula
    R = np.eye(3) + s * A + (1 - c) * np.dot(A, A)
    
    return R

def matrix_to_euler_angles(axis):
    # Normalize the axis vector
    axis = axis / np.linalg.norm(axis)
    
    # Compute the angle using the arccosine function
    angle = np.arccos(np.clip(np.dot(axis, [1, 0, 0]), -1.0, 1.0))
    return angle

    

##############################################################################################################"

camera_center = []
matrix = []
angle = []

rec_file = "../json/reconstruction.json"

with open(rec_file, 'r') as f:
    data = json.load(f)[0]
rec = sfmio.reconstruction_from_json(data)

for shot in rec.shots.values():
   # shots.values() seems to get you what you need...
    r = shot.pose.rotation
    t = shot.pose.translation
    org = shot.pose.get_origin()
    
    #r_matrix = R.from_euler("xyz", r, degrees=False).as_matrix()
    t_matrix = t


    # Estimate the Euler angle of the matrix
    temp_angle = matrix_to_euler_angles(r)
    angle.append(temp_angle)

    # Estimate the 3x3 matrix from our angle-axis matrix
    temp_matrix = angle_axis_to_matrix(temp_angle,r)
    matrix.append(temp_matrix)

    # Transpose the previous matrix
    r_matrix_transpose = temp_matrix.transpose()

    # Negate this matrix
    minus_r_matrix_transpose = -1*r_matrix_transpose

    # multiply this matrix with the transpose ùmatrix
    centre = np.matmul(minus_r_matrix_transpose,t_matrix)

    camera_center.append(centre)
print(camera_center)

"""




   