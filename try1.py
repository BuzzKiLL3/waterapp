import React, { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";

export default function WaterTankApp() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [sensorId, setSensorId] = useState("");
  const [sensorValue, setSensorValue] = useState(50); // Placeholder percentage
  const [sensorInput, setSensorInput] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = () => {
    if (username && password) setIsLoggedIn(true);
  };

  const handleSensorSubmit = () => {
    if (sensorInput) setSensorId(sensorInput);
    // In real implementation: fetch live sensor data here
  };

  const tankHeight = 300;
  const fillHeight = (sensorValue / 100) * tankHeight;

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-200 to-indigo-300 p-4">
      {!isLoggedIn ? (
        <Card className="w-full max-w-md p-6 rounded-2xl shadow-xl">
          <CardContent className="space-y-4">
            <h2 className="text-2xl font-bold text-center">Login</h2>
            <Input
              placeholder="Username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <Input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <Button onClick={handleLogin} className="w-full">
              Sign In
            </Button>
          </CardContent>
        </Card>
      ) : !sensorId ? (
        <Card className="w-full max-w-md p-6 rounded-2xl shadow-xl">
          <CardContent className="space-y-4">
            <h2 className="text-2xl font-bold text-center">Enter Sensor ID</h2>
            <Input
              placeholder="Sensor ID"
              value={sensorInput}
              onChange={(e) => setSensorInput(e.target.value)}
            />
            <Button onClick={handleSensorSubmit} className="w-full">
              Connect
            </Button>
          </CardContent>
        </Card>
      ) : (
        <Card className="w-full max-w-2xl p-6 rounded-2xl shadow-xl bg-white">
          <CardContent className="flex flex-col items-center">
            <h2 className="text-xl font-bold mb-4">Water Tank Live Visualization</h2>
            <div className="relative w-32 h-[300px] border-4 border-blue-600 rounded-b-full overflow-hidden bg-blue-100">
              <motion.div
                className="absolute bottom-0 left-0 w-full bg-blue-500"
                initial={{ height: 0 }}
                animate={{ height: fillHeight }}
                transition={{ duration: 1 }}
              />
              <div className="absolute bottom-2 w-full text-center text-white font-bold text-lg">
                {sensorValue}%
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-600">Sensor ID: {sensorId}</p>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
