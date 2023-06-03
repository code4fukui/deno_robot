from flask import Flask, render_template, request, abort
import ipaddress
import datetime
import pyautogui
import json
 
app = Flask(__name__)

@app.route("/")
def index():
	templateData = {
		"position": pyautogui.position(),
	}
	return render_template("index.html", **templateData)

@app.route("/keyPress/<key>")
def keyPress(key):
	pyautogui.press(key)
	templateData = {}
	return render_template("ok.html", **templateData)

@app.route("/keyDown/<key>")
def keyDown(key):
	pyautogui.keyDown(key)
	templateData = {}
	return render_template("ok.html", **templateData)

@app.route("/keyUp/<key>")
def keyUp(key):
	pyautogui.keyUp(key)
	templateData = {}
	return render_template("ok.html", **templateData)

@app.route("/keyType/<s>")
def keyType(s):
	pyautogui.write(s)
	templateData = {}
	return render_template("ok.html", **templateData)

@app.route("/mousePosition")
def mousePosition():
	p = pyautogui.position()
	templateData = {
		"x": p.x,
		"y": p.y,
	}
	return render_template("point.html", **templateData)

@app.route("/screenSize")
def screenSize():
	p = pyautogui.size()
	templateData = {
		"x": p.width,
		"y": p.height,
	}
	return render_template("point.html", **templateData)

@app.route("/mouseMove/<x>,<y>")
def mouseMove(x, y):
	x = int(x)
	y = int(y)
	pyautogui.moveTo(x, y)
	templateData = {}
	return render_template("ok.html", **templateData)

@app.route("/mouseClick")
def mouseClick():
	pyautogui.click()
	templateData = {}
	return render_template("ok.html", **templateData)

@app.route("/mouseClickRight")
def mouseClickRight():
	pyautogui.rightClick()
	templateData = {}
	return render_template("ok.html", **templateData)

allow_networks = json.load(open("allow_networks.json", "r"))
print("allow_networks", allow_networks)

@app.before_request
def before_request():
	remote_addr = ipaddress.ip_address(request.remote_addr)
	for allow_network in allow_networks:
		ip_network = ipaddress.ip_network(allow_network)
		if remote_addr in ip_network:
			return
	return abort(403, "access denied from your IP address")

if __name__ == "__main__":
	#app.run(host="0.0.0.0", port=80, debug=True)
	app.run(host="::", port=80, debug=True) # both IPv4 and IPv6
