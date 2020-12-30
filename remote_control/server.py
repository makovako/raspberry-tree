import socketio
import eventlet
import asyncio
import uvicorn
import random

from tree import RGBXmasTree
from colorzero import Color, Hue


static_files = {
    "/": "index.html",
    "/index.js": "index.js"
}

sio = socketio.AsyncServer(async_mode="asgi")
app = socketio.ASGIApp(sio, static_files=static_files)

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

def gen_value(color, indexes):
    out = []
    for i in range(25):
        if i in indexes:
            out.append(Color(color))
        else:
            out.append((0,0,0))
    return out

async def run_effect(effect=None):
    global tree
    try:
        if "pulze" in effect["type"]:
            while True:
                color = random.choice(effect["colors"])
                bottom = [0,7,19,24,12,6,15,16]
                middle = [1,8,20,23,11,5,14,17]
                top = [2,9,21,22,10,4,13,18]
                star = [3]
                tree.value = gen_value(color, bottom)
                tree.value = gen_value(color, bottom+middle)
                tree.value = gen_value(color, bottom+middle+top)
                tree.value = gen_value(color, bottom+middle+top+star)
                tree.value = gen_value(color, bottom+middle+top)
                tree.value = gen_value(color, bottom+middle)
                tree.value = gen_value(color, bottom)
                tree.value = [(0,0,0)] * 25
                await asyncio.sleep(0.25)
                print(f"running {effect['type']}")
        elif "huecycle" in effect["type"]:
            color = Color("red")
            if "fade" in effect["type"]:
                tree.brightness = 0
            while True:
                dim = list(filter(lambda n: n <= curr_brightness, [0,0.1,0.2,0.3,0.5,0.6,0.7,0.8,0.9]))
                color += Hue(deg=5)
                tree.color = color
                if "fade" in effect["type"]:
                    for d in dim:
                        tree.brightness = d
                    for d in dim[::-1]:
                        tree.brightness = d
                if "black" in effect["type"]:
                    await asyncio.sleep(0.1)
                    tree.color = Color("black")
                    await asyncio.sleep(0.1)
                await asyncio.sleep(0.1)
                print(f"running {effect['type']}")
        elif "fading" in effect["type"]:
            tree.brightness = 0
            while True:
                dim = list(filter(lambda n: n <= curr_brightness, [0,0.1,0.2,0.3,0.5,0.6,0.7,0.8,0.9]))
                tree.color = Color(random.choice(effect["colors"]))
                for d in dim:
                    tree.brightness = d
                for d in dim[::-1]:
                    tree.brightness = d
                await asyncio.sleep(0.1)
                print(f"running {effect['type']}")

        else:
            tree.color = Color(random.choice(['red','green','blue']))
            while True:
                await asyncio.sleep(5)
                print("running unknown effect")
    except asyncio.CancelledError:
        tree.off()
        tree.brightness = curr_brightness
        tree.on()
    except KeyboardInterrupt:
        tree.off()
        tree.brightness = curr_brightness
        tree.on()


@sio.event
async def effect(sid, effect):
    global tree
    pending = asyncio.all_tasks()
    #print(pending)
    for task in pending:
        name = getattr(task, "name", None)
        if name == "effect-task":
            task.cancel()
            await task
    print(effect)
    if effect["type"] != "none":
        #loop = asyncio.get_event_loop()
        task = asyncio.create_task(run_effect(effect))
        task.name = "effect-task"
        await task

tree = RGBXmasTree()

if __name__ == "__main__":
    tree.brightness = curr_brightness
    tree.color = (1,1,1)
    #eventlet.asgi.server(eventlet.listen(('',5000)), app)
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
    tree.off()
    tree.close()
