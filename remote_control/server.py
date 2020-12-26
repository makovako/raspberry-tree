import socketio
import eventlet

from tree import RGBXmasTree
from colorzero import Color


static_files = {
    "/": "index.html",
    "/index.js": "index.js"
}

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files=static_files)

curr_brightness = 0.1


@sio.event
def tree(sid, data):
    print(data)
    global tree
    tree.color = Color(data["color"])

@sio.event
def color(sid, color):
    global tree
    tree.color = Color(color)

@sio.event
def plus(sid):
    global tree
    global curr_brightness
    if curr_brightness <= 0.9:
        curr_brightness = 0.1 + curr_brightness
        tree.brightness = curr_brightness
        print(tree.brightness)

@sio.event
def minus(sid):
    global tree
    global curr_brightness
    if curr_brightness >= 0.1:
        curr_brightness = curr_brightness - 0.1
        tree.brightness = curr_brightness
        print(tree.brightness)

@sio.event
def on(sid):
    global tree
    tree.on()

@sio.event
def off(sid):
    global tree
    tree.off()

@sio.event
def effect(sid, effect):
    global tree
    print(effect)

tree = RGBXmasTree()

if __name__ == "__main__":
    tree.brightness = curr_brightness
    tree.color = (1,1,1)
    eventlet.wsgi.server(eventlet.listen(('',5000)), app)
    tree.off()
    tree.close()
