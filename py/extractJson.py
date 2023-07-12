import json

# load reconstruction.json
with open('../json/reconstruction.json') as file:
    data = json.load(file)

# Extract datas from shots
shots_data = []
translation_tab = []
rotation_tab = []

for object in data:
    if 'shots' in object:
        shots = object['shots']
    for shot_filename, shot_data in shots.items():
        rotation = shot_data.get('rotation')
        translation = shot_data.get('translation')
        if rotation is not None and translation is not None:
            shot_name = shot_filename.split('.')[0]
            shots_data.append(shot_name)
            translation_tab.append(translation)
            rotation_tab.append(rotation)

# load json destination
with open('../json/coordinates_rota_trans.json') as dest_file:
    dest_data = json.load(dest_file)


dest_data['shots'] = shots_data
# Add all the datas to this file
with open('../json/coordinates_rota_trans.json', 'w') as dest_file:
    json.dump(dest_data, dest_file, indent=4)


dest_data['rotation'] = rotation_tab
# Add all the datas to this file
with open('../json/coordinates_rota_trans.json', 'w') as dest_file:
    json.dump(dest_data, dest_file, indent=4)

dest_data['translation'] = translation_tab
# Add all the datas to this file
with open('../json/coordinates_rota_trans.json', 'w') as dest_file:
    json.dump(dest_data, dest_file, indent=4)