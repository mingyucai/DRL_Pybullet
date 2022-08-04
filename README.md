# DRL_Pybullet
Deep_Reinforcement_Learning_Pybullet

## Simple Driving
The simple driving environment was copied from [this repo](https://github.com/GerardMaggiolino/Gym-Medium-Post) and modified.
Modifications include a few updates for modern APIs and placing the RGB image camera above in a birds-eye view rather than POV.

To set up simple driving, run the following from within your virtualenv:
```
pip install -e ./SimpleDriving/
```

To test if your environment works, run the following:
```
python simple_driving_rand_actions.py
```

You should see low-resolution 2d birds-eye rendering of the vehicle on a plane.
