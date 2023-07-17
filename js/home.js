import * as timeManager from './timeManager.js';
import data_camera from '../json/coordinates_rota_trans.json' assert { type: 'json' };
import * as hp from './hotspots.js';
import * as sc from './scene.js';

//----------------------------------------------------------------------------------------------------------------------------------------------
//Create Scenes with Hotspots
//First you need too create all the HP (HotSpot) because you need them in createScene()

// represente the number of panorama that we have
var nb_pano = data_camera.neighbor_pitch_yaw.length;
// represente the number of neighbor for each panorama that we have
var nb_neighbor = data_camera.neighbor_pitch_yaw[0].length;

//to use the data of our pitch and yaw : 

//data_camera.neighbor_pitch_yaw represente the all array 
//data_camera.neighbor_pitch_yaw[0] represente the datas of the first panorama
//data_camera.neighbor_pitch_yaw[0][0] represente the first hotspot of the first panorama
//data_camera.neighbor_pitch_yaw[0][0][0] represente the pitch of the first hotspot of the first panorama 

//----------------------------------------------------------------------------------------------------------------------------------------------


// creation of every hp based on neighbor
let hp_tab = [];

for (let i = 0; i < nb_pano; i++) {
  for (let j = 0; j < nb_neighbor; j++){  

    let pitch = data_camera.neighbor_pitch_yaw[i][j][0];
    let yaw = data_camera.neighbor_pitch_yaw[i][j][1];
    var neighbor = data_camera.neighbors[i][j];
    var scene_number = "scene" + neighbor;
    var hotSpot = hp.createHotSpots(pitch,yaw,"scene",scene_number,pitch,yaw);
    hp_tab.push(hotSpot);

  }
}

// creation of every scene with coresponding hp
let scene_tab = [];
var neighbor_id = 0;
for (let i = 0; i < nb_pano; i++) {
  var panorama = "../img/" + data_camera.shots[i] +".jpg"
  let neighbor_tab = []
  for (let j = 0; j < nb_neighbor; j++){
    var neighbor_in_scene = hp_tab[neighbor_id];
    neighbor_tab.push(neighbor_in_scene);
    neighbor_id = neighbor_id +1;
  }
  var scene = sc.createScene(panorama,neighbor_tab);
  scene_tab.push(scene);
}


//--------------------------------------------------------------------------------------------------------------------------------------------
// Configuration Pannellum 
  var configHome = {
    type: "equirectangular",
    autoLoad:true,
    yaw:0,
    pitch:0,
    hfov:200, /*zoom molette*/
    compass:false,
    scenes: {}
    
  };  

// Viewver creation 
var viewer = pannellum.viewer('panorama',configHome);

// add each scene to the viewver
for (let i = 0; i < scene_tab.length; i++)
{
  var scene_name = "scene" + i;
  viewer.addScene(scene_name,scene_tab[i]);
}

//scene you want to load first
viewer.loadScene('scene15');










