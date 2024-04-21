'''A simulator for the BNO IMU data

Auto generates data into the redis database similar to an actual IMU'''
import redis
import time
import datetime



if __name__ == "__main__":
    with redis.Redis(host='localhost',port=6379 ,db=1) as r:
        ts = r.ts()
        
        while(True):
            date = datetime.datetime.now()
            timestamp = int(date.timestamp()*1000)

            pipe = r.pipeline()
            pipe.execute_command("ts.add","sensor:bno:accel_x",timestamp,0.1)
            pipe.execute_command("ts.add","sensor:bno:accel_y",timestamp,0.2)
            pipe.execute_command("ts.add","sensor:bno:accel_z",timestamp,0.3)

            pipe.execute_command("ts.add","sensor:bno:gyro_x",timestamp,0.3)
            pipe.execute_command("ts.add","sensor:bno:gyro_y",timestamp,0.3)
            pipe.execute_command("ts.add","sensor:bno:gyro_z",timestamp,0.3)

            
            pipe.execute_command("ts.add","sensor:bno:quat_i",timestamp,0.3)
            pipe.execute_command("ts.add","sensor:bno:quat_j",timestamp,0.3)
            pipe.execute_command("ts.add","sensor:bno:quat_k",timestamp,0.3)
            pipe.execute_command("ts.add","sensor:bno:quat_real",timestamp,0.3)
            
            pipe.execute_command("ts.add","sensor:bno:mag_x",timestamp,0.3)
            pipe.execute_command("ts.add","sensor:bno:mag_y",timestamp,0.3)
            pipe.execute_command("ts.add","sensor:bno:mag_z",timestamp,0.3)

            pipe.execute()
            print("Added sensor values")
            time.sleep(1)
            value = ts.get("sensor:bno:accel_x")
            print("Got accel_x: " + repr(value))
            value = ts.get("sensor:bno:mag_z")
            print("Got mag_z: " + repr(value))
