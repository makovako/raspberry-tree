# raspberry-tree

Example scripts end remote control for controlling Raspberry pi Christmas Tree.

[Source](https://github.com/ThePiHut/rgbxmastree)

## Example scripts

Make sure you have `python3-gpiozero` installed. Then you can run any script as normal python script and cancel with Ctrl+C.

## Remote control

Starts http server and serves website on port 5000 for controling the tree from any device.

How to run:

1. Go to remote\_control folder `cd remote_control`
2. Create virtual environment `python3 -m venv venv`
3. Activate it `source venv/bin/activate`
4. Install required packages `pip install -r requirements.txt`
5. Run server `python3 server.py`
6. Connect from the browser `http://pi_ip_address:5000` and control the tree
