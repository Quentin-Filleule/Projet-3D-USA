import math
import json
import matplotlib.pyplot as plt


# Estimate distance between 2 points
def distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1) + (z2 - z1)*(z2 - z1))


# Estimate k nearest_neighbors for a point
def k_nearest_neighbors(points, k):
    neighbors = {}
    for i, point in enumerate(points):
        distances = []
        for j, other_point in enumerate(points):
            if i != j:
                distances.append((distance(point, other_point), j))
        distances.sort()
        neighbors[i] = [j for _, j in distances[:k]]
    return neighbors



#Estimate pitch and yaw based on pixel coordinates
def pixel_to_pitch_yaw(x, y):
    
    yaw = x * 180
    pitch = math.asin(y) * 180 / math.pi

    return pitch, yaw


############################################################################################################################################

tab_trans = []

# load reconstruction.json
with open('../json/reconstruction.json') as file:
    data = json.load(file)

# Extract datas from shots
shots_data = []
for object in data:
    if 'shots' in object:
        shots = object['shots']
    for shot_filename, shot_data in shots.items():
        rotation = shot_data.get('rotation')
        translation = shot_data.get('translation')
        if rotation is not None and translation is not None:
            shot_name = shot_filename.split('.')[0]
            shots_data.append(shot_name)
            tab_trans.append(translation)

k = 2
# For each panorama, estimate the k=2 closest panoramas
neighbors = k_nearest_neighbors(tab_trans, k)
for i, point in enumerate(tab_trans):
    print(f"the {k} nearest neighbors of {shots_data[i]} are : {', '.join(str(shots_data[j]) for j in neighbors[i])}")


# load json destination
with open('../json/coordinates_rota_trans.json') as dest_file:
    dest_data = json.load(dest_file)


dest_data['neighbors'] = neighbors
# Add all the datas to this file
with open('../json/coordinates_rota_trans.json', 'w') as dest_file:
    json.dump(dest_data, dest_file, indent=4)

#Display result on graph to check errors
center_X = []
center_Y = []
center_Z = []

for i in range(len(tab_trans)):

    temp = tab_trans[i]

    center_X.append(temp[0])
    center_Y.append(temp[1])
    center_Z.append(temp[2])


# Trace 3D figure
fig = plt.figure()
ax = fig.add_subplot(projection='3d') # Use 3D display
ax.scatter(center_X, center_Y, center_Z, marker='d')  # Trace points
plt.title("Points 3D")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.tight_layout()

# Create a new png images to preview the result
plt.savefig("mygraph.png")
