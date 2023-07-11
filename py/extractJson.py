import json

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
            shot_info = {
                'shot_name': shot_name,
                'rotation': rotation,
                'translation': translation
            }
            shots_data.append(shot_info)

# load json destination
with open('../json/coordinates_rota_trans.json') as dest_file:
    dest_data = json.load(dest_file)


dest_data['shots'] = shots_data

# Add all the datas to this file
with open('../json/coordinates_rota_trans.json', 'w') as dest_file:
    json.dump(dest_data, dest_file, indent=4)
