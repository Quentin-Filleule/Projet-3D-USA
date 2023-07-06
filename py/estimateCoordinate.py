import math
import json
from opensfm import io as sfmio
from scipy.spatial.transform import Rotation as R
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d 



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


def convert_to_pitch_yaw(camera_x, camera_y, camera_z, target_x, target_y, target_z):
    # Calculate the vector from camera to target
    dx = target_x - camera_x
    dy = target_y - camera_y
    dz = target_z - camera_z

    # Calculate the distance from camera to target
    distance = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)

    # Calculate the yaw angle
    yaw = math.atan2(dy, dx)

    # Calculate the pitch angle
    pitch = math.asin(dz / distance)

    # Convert angles to degrees
    pitch_deg = math.degrees(pitch)
    yaw_deg = math.degrees(yaw)

    return pitch_deg, yaw_deg


#########################################################################################################################################

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


    
    temp_angle = matrix_to_euler_angles(r)
    angle.append(temp_angle)

    temp_matrix = angle_axis_to_matrix(temp_angle,r)
    matrix.append(temp_matrix)

    r_matrix_transpose = temp_matrix.transpose()

    minus_r_matrix_transpose = -1*r_matrix_transpose

    centre = np.matmul(minus_r_matrix_transpose,t_matrix)

    camera_center.append(centre)
print(camera_center)




center_X = []
center_Y = []
center_Z = []
for i in range(len(camera_center)):

    temp = camera_center[i]
    
    j=0
    center_X.append(temp[j])
    center_Y.append(temp[j+1])
    center_Z.append(temp[j+2])

# Tracé du résultat en 3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d') # Affichage en 3D
ax.scatter(center_X, center_Y, center_Z, marker='d')  # Tracé de la courbe 3D
plt.title("Points 3D")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.tight_layout()
plt.savefig("mygraph.png")


























"""
#separate rotation and traslation tab in 3
rotation_X = []
rotation_Y = []
rotation_Z = []
translation_X = []
translation_Y = []
translation_Z = []

i=0

for i in range(len(rotation_data)):

    temp = rotation_data[i]
    temp1 = translation_data[i]
    j=0
    rotation_X.append(temp[j])
    rotation_Y.append(temp[j+1])
    rotation_Z.append(temp[j+2])

    translation_X.append(temp1[j])
    translation_Y.append(temp1[j+1])
    translation_Z.append(temp1[j+2])

un = 2
deux = 1
pitch, yaw = convert_to_pitch_yaw(translation_X[un],translation_Y[un],translation_Z[un],translation_X[deux],translation_Y[deux],translation_Z[deux])
print("Pitch:", pitch)
print("Yaw:", yaw)



#use fonction to get pitch and yaw
pitch_Tab = []
yaw_Tab = []

i=0
for i in range(len(rotation_data)):

    pitch = calculate_pitch(rotation_X[i],rotation_Y[i],rotation_Z[i])
    yaw = calculate_yaw(rotation_X[i],rotation_Y[i])

    pitch_Tab.append(pitch)
    yaw_Tab.append(yaw)
"""






   