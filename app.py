'''This is a basic template for an API App that works with pytest'''
import redis
from apiflask import APIFlask, HTTPBasicAuth
import Sensors.bno_imu as bno_imu

app = APIFlask(__name__)
auth = HTTPBasicAuth()

rdb = redis.Redis(host='localhost',port=6379 ,db=1)
ts = rdb.ts()

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


@app.route('/killswitch',methods=['GET','POST','PUT'])
@app.auth_required(auth)
def send_killswitch_sig():
    return {'message':'sent killswitch signal. '}

if __name__ == "__main__":
    temp = ts.get("sensor:bno:mag_x")
    print(repr(temp))
    temp = ts.info("sensor:bno:mag_x")
    print(bno_imu.load_latest_imu(ts))
    pass
