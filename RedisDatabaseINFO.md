# Definitions for the Redis Server

This API interface expects to gather data directly from a redis database on the host robot.

The majority of the data that can be requested uses the redis timeseries module. These include sensor and state values (such as acceleration values over time).

## Redis Timeseries convention

A general rule made was to have the key values for the timeseries data be human readable. The key should clearly describe the data that it tracks, and should use colons to seperate the ideas. 

The timeseries data makes a distinction between sensor data and state data. Sensor data comes from a measurment device and represents an observed physical characteristic. State data is any variable created from processing of the system. State data is typically things like the current thruster state or the inertial navigation state vector.

Thus "sensor:imu:accel:x" describes sensor data from the inertial measurement unit for acceleration in the x direction.

"state:inu:pos:x" would describe the x position state from the INU.

## Sensor timeseries lists

|  key  |  description  |  units  |  Labels  |
| ------ | ----- | ---- | ---- |
| sensor:imu:accel_x |measured acceleration in x direction | m/s/s | sensor:imu type:acceleration unit:m/s/s component:x |

