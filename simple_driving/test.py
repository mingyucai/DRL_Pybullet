import pybullet as p
import time
import  pybullet_data
physicsClient = p.connect(p.GUI)
p.resetDebugVisualizerCamera(cameraDistance=1.0, cameraYaw=-90, cameraPitch=-45, cameraTargetPosition = [-0.1, -0.0, 0.65])
# p.resetSimulation()
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -10)
# p.setTimeStep(1./120.)
# useRealTimeSim = 1
# p.setRealTimeSimulation(useRealTimeSim)

planeID = p.loadURDF('plane.urdf')
GoalID = p.loadURDF("resources/simplegoal.urdf",
                   [1, 1, 0],
                   physicsClientId=physicsClient)

startPos = [0, 0, 0.2]
startOrientation = p.getQuaternionFromEuler([0, 0, 0])
carID = p.loadURDF("resources/simplecar.urdf", startPos, startOrientation)
for i in range(1000):
    pos, ori = p.getBasePositionAndOrientation(carID)
    p.applyExternalForce(carID, 0, [50, 0, 0], pos, p.WORLD_FRAME)
    p.stepSimulation()
    time.sleep(1./240.)
carPos, carOrn = p.getBasePositionAndOrientation(carID)
print(carPos, carOrn)
p.disconnect()
