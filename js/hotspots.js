//Function to creat hotspots
export function createHotSpots(pitch, yaw, type, sceneId, targetPitch, targetYaw) {
  var hotSpots = 
    {
      pitch: pitch,
      yaw: yaw,
      type: type,
      sceneId: sceneId,
      targetPitch: targetPitch,
      targetYaw: targetYaw,
    }
    // Ajoutez d'autres points chauds ici
  

  return hotSpots;
}

