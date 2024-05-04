'''This is a basic template for an API App that works with pytest'''
from apiflask import Schema
import apiflask.fields as field
import redis
import redis.commands
import redis.commands.timeseries
from collections import ChainMap

returned_labels = ["sensor", "type", "unit", "component"]

class imu_lables(Schema):
    component = field.Method()
    sensor = field.String()
    type = field.String()
    unit = field.String()
    timestamp = field.Integer()

sensor_tuple = [field.Dict(),field.Integer(),field.Float()]

class imu_output(Schema):
    accel_x = field.Tuple(sensor_tuple,attribute="sensor:imu:accel_x")
    accel_y = field.Tuple(sensor_tuple,attribute="sensor:imu:accel_y")
    accel_z = field.Tuple(sensor_tuple,attribute="sensor:imu:accel_z")
    gyro_x = field.Tuple(sensor_tuple,attribute="sensor:imu:gyro_x")
    gyro_y = field.Tuple(sensor_tuple,attribute="sensor:imu:gyro_y")
    gyro_z = field.Tuple(sensor_tuple,attribute="sensor:imu:gyro_z")
    quat_i = field.Tuple(sensor_tuple,attribute="sensor:imu:quat_i")
    quat_j = field.Tuple(sensor_tuple,attribute="sensor:imu:quat_j")
    quat_k = field.Tuple(sensor_tuple,attribute="sensor:imu:quat_k")
    quat_real = field.Tuple(sensor_tuple,attribute="sensor:imu:quat_r")
    mag_x = field.Tuple(sensor_tuple,attribute="sensor:imu:magn_x")
    mag_y = field.Tuple(sensor_tuple,attribute="sensor:imu:magn_y")
    mag_z = field.Tuple(sensor_tuple,attribute="sensor:imu:magn_z")
    

def load_latest_imu(tsdb:redis.commands.timeseries.TimeSeries):
    return ChainMap(*tsdb.mget(["sensor=imu"],select_labels=returned_labels))
