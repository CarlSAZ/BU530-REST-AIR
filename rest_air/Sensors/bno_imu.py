'''This is a basic template for an API App that works with pytest'''
from collections import ChainMap
import apiflask.fields as field
import redis
import redis.commands
import redis.commands.timeseries
from apiflask import  Schema, APIBlueprint, HTTPBasicAuth
from rest_air import auth, rdb

imupage= APIBlueprint('imu',__name__,url_prefix='/sensors/imu')

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

@imupage.get('')
@imupage.output(imu_output)
@imupage.doc(summary='Return latest IMU')
def get_latest_imu():
    '''Returns the latest sensor data from the BNO imu
        - acceleration
        - gyro
        - quaternion
        - magnetic compass'''
    result = load_latest_imu(rdb.ts())
    print(result)
    return result

@imupage.get('/<int:time1>-<int:time2>')
def get_imu_timerange(time1,time2):
    '''Returns the sensor data from the BNO imu between time1 and time2
        - acceleration
        - gyro
        - quaternion
        - magnetic compass'''
    #result = bno_imu.get_imu_timerange(ts,time1,time2)
    return f"Timerange not implemented yet. Requested time [{time1} - {time2}]", 501