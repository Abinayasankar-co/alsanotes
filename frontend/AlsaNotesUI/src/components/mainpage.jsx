import React from "react";
import { useLoader } from "@react-three/fiber";
import { TextureLoader } from "three";


export default function Box() {
  // Pass the texture path as a string directly to useLoader
  const colorMap = useLoader(TextureLoader, "/textures/map.jpg");

  return (
    <mesh rotateOnAxis={[Math.PI / 2, 0, Math.PI / 9]}>
      <boxGeometry attributes={[3, 3, 3]} />
      <meshStandardMaterial map={colorMap} />
    </mesh>
  );
}
