from flask import jsonify
program_status = "OFF"

def start():
    global program_status
    program_status = "ON"
    print("Program start")
    return jsonify ("program start")

def set_up(time, in_height, in_time):
    print("\n\nyour paremeter set as " + time+"......")
    return jsonify("Your program is set as "  + time)


def stop():
    global program_status
    program_status = "OFF"
    print("Program stopped")
    return jsonify("Your program is stopped")

#add duration and activate count etc. 
def status(): 
    print(program_status)
    return jsonify(program_status)