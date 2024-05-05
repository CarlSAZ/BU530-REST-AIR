'''commandbridge - handles interface to ROS through direct messaging

This API is a intermediary between external HTTP interfaces and the ROS 
operating system. This is handled by utilizing the ROS bridge library. This flask api 
will open up the TCP socket in order to communicate with the running ROS. In this way the
TCP information is not exposed to the general user or application maker.'''
from apiflask import APIBlueprint, HTTPBasicAuth, Schema

# TODO: Find a better way than circular importing...
from rest_air import rdb, auth
from flask import current_app
from queue import  PriorityQueue
import queue
import time
commandview = APIBlueprint('command',__name__,url_prefix='/command')

command_queue = PriorityQueue(maxsize=20)

class BaseCommand(object):
    op = "status"
    
class PublishRequest(object):
    op = "publish"
    topic = "foo"
    msg = object()

class Time(object):
    sec = 0
    nsec = 0

class Header(Schema):
    seq = 0
    stamp = Time()
    frame_id = 0


class AirshipParams(object):
    header = Header()
    height_target_m = 0.0
    altitude_control_flag = True
    yaw_target_deg = 0.0
    yaw_control_flag = False

@commandview.route('/killswitch',methods=['POST'])
@commandview.auth_required(auth)
def send_killswitch_sig():
    '''Immediately sends a kill signal.
    
    This is the exception where the command is not queued, but
    sent immediately. This is a failsafe in case immediate shutdown is required.'''
    # TODO: Implement kill signal
    return {'message':'sent killswitch signal. '}

@commandview.post('/hoverheight/<float:height>')
@commandview.auth_required(auth)
def send_hover_height(height:float):
    command = AirshipParams()
    command.height_target_m = height
    command.header.stamp.sec = int(time.time())
    command.header.stamp.nsec = int(time.time_ns() - command.header.stamp.sec)
    try:
        command_queue.put_nowait((50,command))
    except queue.Full:
        return {'message':'Command Queue Full, try again later.'}, 507
    
    return {'message':'Sent Hover height'}, 200

@commandview.post('/forwardspeed/<float:speed>')
@commandview.auth_required(auth)
def send_forward_speed(speed:float):
    # TODO: Replace with correct message
    command = AirshipParams()
    command.height_target_m = speed
    command.header.stamp.sec = int(time.time())
    command.header.stamp.nsec = int(time.time_ns() - command.header.stamp.sec)
    try:
        command_queue.put_nowait((50,command))
    except queue.Full:
        return {'message':'Command Queue Full, try again later.'}, 507
    
    return {'message':'Sent Hover height'}, 200