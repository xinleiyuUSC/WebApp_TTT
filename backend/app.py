from flask import Flask, render_template
from flask import jsonify
from flask import request
import pose 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['GET'])
def start_program():
    return pose.start()

@app.route('/stop', methods=['GET'])
def stop_program():
    return pose.stop()

@app.route('/set', methods=['GET'])
def set_program():
    para1 = request.args.get('height')
    para2 = request.args.get('time')
    para3 = request.args.get('inHeight')
    para4 = request.args.get('inTime')
    return pose.set_up(para1, para2, para3, para4)

@app.route('/status', methods=['GET'])
def status_program():
    return pose.status()


if __name__ == "__main__":
    app.run(debug=True)