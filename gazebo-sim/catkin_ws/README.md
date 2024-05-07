# How to Run Gazebo Simulation

These instructions will cover how to run and drive a simulation of the Miami University ECE car in Gazebo using ROS.

## Prerequisites:
### To run simulation (in person or remotely) from previously configured lab computer:
1. Login to robot0 user
   - To log in remotely, use remote desktop connection (on windows), or linux virtual machine (tested on windows, found to be inefficient)

### Configure new computer to run simulation:
1. Download gazebo. Our code is tested with version 11.11.0
2. Download ROS. Our code is tested with noetic (required)
   - If using Ubuntu, must use version 20.04
3. Navigate to location for projoect and run this set of commands:
    ```
    mkdir catkin_ws
    cd catkin_ws
    mkdir src
    ```
4. Install ackermann steering plugin
    ```
    git clone (use git link for this repository)
    sudo apt install ros-roetic-ackermann-msgs
    cd ~/catkin_ws
    rosdep install –from-paths src --ignore-src -r -y
    catkin_make
    ```

## Running the Simulation:
1. Ensure packages are available:
    ```
    cd ~/catkin_ws/src
    rospack find ackermann_vehicle_gazebo # this will throw an error every time you open a new terminal
    ```
    If this command causes an error:
    ```
    source /home/{your_username}/{path to catkin folder}/catkin_ws/devel/setup.bash
    ```

2. Launch the plugin:
    ```
    roslaunch ackermann_vehicle_gazebo ackermann_vehicle_noetic.launch
    ```

3. Setting up listener to steer the car:
   Open a new terminal to run the following:
    ```
    cd catkin_ws/src/ackermann_vehicle/ackermann_vehicle_navigation/scripts/
    ./cmd_vel_to_ackermann_drive.py
    ```
      This terminal is now listening for inputs
   
4a. Steering the car manually:
    Open another new terminal to run directions, adjust linear and angular inputs as required:
    ```
    rostopic pub -r 10 /cmd_vel geometry_msgs/Twist '{linear: {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.2}}'
    ```

4b. Running specified path:
   - Open a new terminal and run a path publisher python file from the `ackermann_vehicle_navigation/scripts` folder
   - Open a new terminal and run a path follower python file from the `ackermann_vehicle_navigation/scripts` folder
   - note: these new terminals will require repeating step one to ensure packages can be found by the files
