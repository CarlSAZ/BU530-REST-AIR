'''This is a basic template for an API App that works with pytest'''
from apiflask import APIFlask, HTTPBasicAuth
import Sensors.bno_imu as bno_imu

auth = HTTPBasicAuth()
    

@auth.verify_password
def verify_password(username,password):
    '''TBD: Better define authentication'''
    if(username=='admin' and password=='tacocat'):
        return username

@app.get('/')
def index():
    return {'message': 'hello human! This is a flying airship!'}

@app.get('/sensors')
def list_sensors():
    return {''}

@app.get('/sensors/imu')
@app.output(bno_imu.imu_output)
@app.doc(summary='Return latest IMU')
def get_latest_imu():
    '''Returns the latest sensor data from the BNO imu
        - acceleration
        - gyro
        - quaternion
        - magnetic compass'''
    result = bno_imu.load_latest_imu(ts)
    print(result)
    return result

@app.get('/sensors/imu/timerange/<int:time1>-<int:time2>')
@app.output(bno_imu.imu_output)
def get_imu_timerange(time1,time2):
    '''Returns the sensor data from the BNO imu between time1 and time2
        - acceleration
        - gyro
        - quaternion
        - magnetic compass'''
    #result = bno_imu.get_imu_timerange(ts,time1,time2)
    return 'Timerange not implemented yet. Requested time [{time1} - {time2}]', 501


@app.route('/killswitch',methods=['GET','POST','PUT'])
@app.auth_required(auth)
def send_killswitch_sig():
    return {'message':'sent killswitch signal. '}