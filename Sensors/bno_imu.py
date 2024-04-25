'''This is a basic template for an API App that works with pytest'''
from apiflask import Schema
import apiflask.fields as field
import redis
import redis.commands
import redis.commands.timeseries

class imu_ts(Schema):
    timestamp = field.Integer()
    value = field.Float()

sensor_tuple = (field.Integer(),field.Float())

class imu_output(Schema):
    accel_x = field.Tuple(sensor_tuple)
    accel_y = field.Tuple(sensor_tuple)
    accel_z = field.Tuple(sensor_tuple)
    gyro_x = field.Tuple(sensor_tuple)
    gyro_y = field.Tuple(sensor_tuple)
    gyro_z = field.Tuple(sensor_tuple)
    quat_i = field.Tuple(sensor_tuple)
    quat_j = field.Tuple(sensor_tuple)
    quat_k = field.Tuple(sensor_tuple)
    quat_real = field.Tuple(sensor_tuple)
    mag_x = field.Tuple(sensor_tuple)
    mag_y = field.Tuple(sensor_tuple)
    mag_z = field.Tuple(sensor_tuple)
    

def load_latest_imu(tsdb:redis.commands.timeseries.TimeSeries):
    
    return {
        "accel_x": tsdb.get("sensor:bno:accel_x"),
        "accel_y": tsdb.get("sensor:bno:accel_y"),
        "accel_z": tsdb.get("sensor:bno:accel_z"),
        "gyro_x": tsdb.get("sensor:bno:gyro_x"),
        "gyro_y": tsdb.get("sensor:bno:gyro_y"),
        "gyro_z": tsdb.get("sensor:bno:gyro_z"),
        "quat_i": tsdb.get("sensor:bno:quat_i"),
        "quat_j": tsdb.get("sensor:bno:quat_j"),
        "quat_k": tsdb.get("sensor:bno:quat_k"),
        "quat_real": tsdb.get("sensor:bno:quat_real"),
        "mag_x": tsdb.get("sensor:bno:mag_x"),
        "mag_y": tsdb.get("sensor:bno:mag_y"),
        "mag_z": tsdb.get("sensor:bno:mag_z"),
    }