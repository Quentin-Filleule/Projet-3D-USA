import * as timeManager from './timeManager.js';

var hotSpots1 = [
    {
      pitch: 8.270775531599261, // Angle vertical du point chaud (en degrés)
      yaw: 168.9643425492632, // Angle horizontal du point chaud (en degrés)
      type: "scene", // Type de point chaud ("info", "scene", "URL", etc.)
      sceneId: "scene2", // Identifiant de la scène à laquelle le point chaud est lié (pour le type "scene")
      targetPitch: 0,
      targetYaw: 0,

    },
    // Ajoutez d'autres points chauds ici
  ];

  var bat = {
    panorama: "../img/00001.jpg",
    hotSpots: hotSpots1 
  };

  var eau = {
    panorama: "../img/malibu200.jpg"
  };


  var configHome = {
    type: "equirectangular",
    autoLoad:true,
    yaw:0,
    pitch:0,
    hfov:200, /*zoom molette*/
    compass:false,
    scenes: {}
    
  };  

var viewer = pannellum.viewer('panorama',configHome);

viewer.addScene("scene1",bat);
viewer.addScene("scene2",eau);
console.log(configHome.scenes)
viewer.loadScene('scene1');



console.log(viewer.getScene)






