# Issuing commands to Airship via API

The command pages are an interface with the ROS backend. This seperates out the external interface from the robot's subsystems, and protects the robot from direct connections.

In this way, the commands can be better screened and sanitized prior to handing over to the robotic interface. Additionally, the HTTP authentication can be used to ensure only 
a valid user is capable of sending commands.

All commands are implemented as POST routines. A user will post the command to this API, and it will get added to a queue with a priority based on the user priviledge and command type. A subroutine running in the background will be popping commands off the queue and converting them to ROS message formats. These will then get sent to the running ROS application through a socket layer.

## Command List

