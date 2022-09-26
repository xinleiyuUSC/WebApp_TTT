from flask import jsonify
global program_status

def start():
    program_status = "ON"
    print("Program start")
    return jsonify ("program start")

def set_up(height,time, in_height, in_time):
    print("\n\nyour paremeter set as "+ height + time+"......")
    return jsonify("Your program is set as " + height + time)


def stop():
    program_status = "OFF"
    print("Program stopped")

def status(): 
    print(program_status)