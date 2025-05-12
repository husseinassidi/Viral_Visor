import { Canvas, useFrame } from "@react-three/fiber";
import { useRef } from "react";

import "./three_balls_loading.css";

const Sphere = ({ position, size, color }) => {
  const ref = useRef();

  useFrame((state, delta) => {
    if (ref.current) {
      ref.current.rotation.x += delta; // Rotate around x-axis
      ref.current.rotation.y += delta * 2; // Rotate around x-axis
      ref.current.rotation.z += -delta * 3; // Rotate around x-axis
      ref.current.position.z = Math.sin(state.clock.elapsedTime) * 2;
    }
  });
  return (
    <mesh position={position} ref={ref}>
      <sphereGeometry args={size} />
      <meshStandardMaterial color={color} />
    </mesh>
  );
};

const LoadingAnimation = () => {
  return (
    <div className="Loading_popUp">
      <Canvas>
        <directionalLight position={[0, 1, 2]} />
        <Sphere position={[2.5, 0, 0]} size={[1, 64, 64]} color={"red"} />
        <Sphere position={[0, 0, 0]} size={[1, 64, 64]} color={"cyan"} />
        <Sphere position={[-2.5, 0, 0]} size={[1, 64, 64]} color={"red"} />
      </Canvas>
    </div>
  );
};

export default LoadingAnimation;

