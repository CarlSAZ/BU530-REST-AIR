'''This is a basic template for an API App that works with pytest'''
from apiflask import Schema
import apiflask.fields as field
import redis
import redis.commands
import redis.commands.timeseries
from collections import ChainMap

returned_labels = ["sensor", "type", "unit", "component"]

class imu_ts(Schema):
    timestamp = field.Integer()
    value = field.Float()

sensor_tuple = [field.Dict(),field.Integer(),field.Float()]

class imu_output(Schema):
    accel_x = field.Tuple(sensor_tuple,attribute="sensor:imu:accel_x")
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
    return ChainMap(*tsdb.mget(["imu_id=2"],select_labels=returned_labels))
