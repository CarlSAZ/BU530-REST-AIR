'''A simulator for the imu IMU data

Auto generates data into the redis database similar to an actual IMU'''
import redis
import time
import datetime
from collections import ChainMap


def create_database(r:redis.Redis):
    if not r.exists("sensor:imu:accel_x"):
        command = "ts.create"
    else:
        command = "ts.alter"
    pipe = r.pipeline()
    pipe.execute_command(command,"sensor:imu:accel_x",
                            "LABELS","sensor", "imu","type", "accel","unit","m/s/s","component", "x")
    pipe.execute_command(command,"sensor:imu:accel_y",
                            "LABELS","sensor", "imu","type", "accel","unit","m/s/s","component", "y")
    pipe.execute_command(command,"sensor:imu:accel_z",
                            "LABELS","sensor", "imu","type", "accel","unit","m/s/s","component", "z")
    
    pipe.execute_command(command,"sensor:imu:gyro_x",
                            "LABELS","sensor", "imu","type", "gyro","unit","rad","component","x")
    pipe.execute_command(command,"sensor:imu:gyro_y",
                            "LABELS","sensor", "imu","type", "gyro","unit","rad","component","y")
    pipe.execute_command(command,"sensor:imu:gyro_z",
                            "LABELS","sensor", "imu","type", "gyro","unit","rad","component","z")
    
    pipe.execute_command(command,"sensor:imu:quat_r",
                            "LABELS","sensor", "imu","type", "quat","unit","none","component","r")
    pipe.execute_command(command,"sensor:imu:quat_i",
                            "LABELS","sensor", "imu","type", "quat","unit","none","component","i")
    pipe.execute_command(command,"sensor:imu:quat_j",
                            "LABELS","sensor", "imu","type", "quat","unit","none","component","j")
    pipe.execute_command(command,"sensor:imu:quat_k",
                            "LABELS","sensor", "imu","type", "quat","unit","none","component","k")

    pipe.execute_command(command,"sensor:imu:magn_x",
                            "LABELS","sensor", "imu","type", "magn","unit","rad","component","x")
    pipe.execute_command(command,"sensor:imu:magn_y",
                            "LABELS","sensor", "imu","type", "magn","unit","rad","component","y")
    pipe.execute_command(command,"sensor:imu:magn_z",
                            "LABELS","sensor", "imu","type", "magn","unit","rad","component","z")
    print(pipe.execute())
    print("Adjusted keys?")
    return


if __name__ == "__main__":
    with redis.Redis(host='localhost',port=6379 ,db=0) as r:
        ts = r.ts()
        create_database(r)

        while(True):
            date = datetime.datetime.now()
            timestamp = int(date.timestamp()*1000)

            pipe = r.pipeline()
            pipe.execute_command("ts.add","sensor:imu:accel_x",timestamp,0.1,"LABELS imu_id 2 accel 1")
            pipe.execute_command("ts.add","sensor:imu:accel_y",timestamp,0.2,"LABELS imu_id 2 accel 2")
            pipe.execute_command("ts.add","sensor:imu:accel_z",timestamp,0.3,"LABELS imu_id 2 accel 3")

            pipe.execute_command("ts.add","sensor:imu:gyro_x",timestamp,0.3)
            pipe.execute_command("ts.add","sensor:imu:gyro_y",timestamp,0.3)
            pipe.execute_command("ts.add","sensor:imu:gyro_z",timestamp,0.3)

            
            pipe.execute_command("ts.add","sensor:imu:quat_i",timestamp,0.3)
            pipe.execute_command("ts.add","sensor:imu:quat_j",timestamp,0.3)
            pipe.execute_command("ts.add","sensor:imu:quat_k",timestamp,0.3)
            pipe.execute_command("ts.add","sensor:imu:quat_r",timestamp,0.3)
            
            pipe.execute_command("ts.add","sensor:imu:magn_x",timestamp,0.3)
            pipe.execute_command("ts.add","sensor:imu:magn_y",timestamp,0.3)
            pipe.execute_command("ts.add","sensor:imu:magn_z",timestamp,0.3)

            pipe.execute()
            print("Added sensor values")
            time.sleep(1)
            # Extra debugging to test commands
            value = ts.get("sensor:imu:accel_x")
            print("Got accel_x: " + repr(value))
            value = ts.get("sensor:imu:magn_z")
            print("Got mag_z: " + repr(value))
            print(r.exists("sensor"))
            value = ts.mget(["sensor=imu"])
            print(type(value))
            print(value[0]['sensor:imu:accel_x'])
            tmp = ChainMap(*ts.mget(["sensor=imu"]))
            
            print(tmp['sensor:imu:accel_x'][2])
            print(dict(tmp))

