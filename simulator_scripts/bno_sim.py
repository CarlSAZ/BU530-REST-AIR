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
                            "LABELS","imu_id", "2", "accel", "x")
    pipe.execute_command(command,"sensor:imu:accel_y",
                            "LABELS","imu_id", "2", "accel", "y")
    pipe.execute_command(command,"sensor:imu:accel_z",
                            "LABELS","imu_id", "2", "accel", "z")
    
    pipe.execute_command(command,"sensor:imu:gyro_x",
                            "LABELS","imu_id", "2", "gyro","x")
    pipe.execute_command(command,"sensor:imu:gyro_y",
                            "LABELS","imu_id", "2", "gyro","y")
    pipe.execute_command(command,"sensor:imu:gyro_z",
                            "LABELS","imu_id", "2", "gyro","z")
    
    pipe.execute_command(command,"sensor:imu:quat_r",
                            "LABELS","imu_id", "2", "quat","r")
    pipe.execute_command(command,"sensor:imu:quat_i",
                            "LABELS","imu_id", "2", "quat","i")
    pipe.execute_command(command,"sensor:imu:quat_j",
                            "LABELS","imu_id", "2", "quat","j")
    pipe.execute_command(command,"sensor:imu:quat_k",
                            "LABELS","imu_id", "2", "quat","k")

    pipe.execute_command(command,"sensor:imu:magn_x",
                            "LABELS","imu_id", "2", "magn","x")
    pipe.execute_command(command,"sensor:imu:magn_y",
                            "LABELS","imu_id", "2", "magn","y")
    pipe.execute_command(command,"sensor:imu:magn_z",
                            "LABELS","imu_id", "2", "magn","z")
    print(pipe.execute())
    print("Adjusted keys?")
    return


if __name__ == "__main__":
    with redis.Redis(host='localhost',port=6379 ,db=1) as r:
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
            value = ts.get("sensor:imu:mag_z")
            print("Got mag_z: " + repr(value))
            print(r.exists("sensor"))
            value = ts.mget(["imu_id=2"])
            print(type(value))
            print(value[0]['sensor:imu:accel_x'])
            tmp = ChainMap(*value)
            
            print(tmp[0][2])
            print(tmp)

