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


@sio.event
def tree(sid, data):
    print(data)
    global tree
    tree.color = Color(data["color"])

tree = RGBXmasTree()

if __name__ == "__main__":
    tree.brightness = 0.1
    tree.color = (1,1,1)
    eventlet.wsgi.server(eventlet.listen(('',5000)), app)
    tree.off()
    tree.close()
