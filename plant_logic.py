import time
import os

def plant_condition(file_path,x):
    try:
        with open(file_path,'r',encoding='utf-8') as f:
            print(color_list[x] + f.read() + color_list["RESET"])
    except FileNotFoundError:
        print("Error loading the file")
    

file_path = "{directory where the time_tracker.txt is saved}"
file_name = "time_tracker.txt"
pathh = os.path.join(file_path,file_name)

try:
    with open(pathh,"r") as f:
        current_time = time.time()
        recorder_time = float(f.read())

    time_diff = current_time-recorder_time
    hour_diff = time_diff//3600


    color_list = {
        "RESET": "\033[0m",       
        "MUSTARD": "\033[38;5;214m",     
        "BRIGHT_GREEN": "\033[92m", 
        "BROWN": "\033[38;5;94m", 
        "BOLD_RED": "\033[1;31m" 
    }

    if hour_diff<2.0:
        thrive = "{directory where the thriving.txt is saved}"
        plant_condition(thrive,"BRIGHT_GREEN")
    elif 2.0<=hour_diff<=24.0:
        droop = "{directory where the droopy.txt is saved}"
        plant_condition(droop,"MUSTARD")
    else:
        dead = "{directory where the dead.txt is saved}"
        plant_condition(dead,"BOLD_RED")
        
except FileNotFoundError:
    print("Time_Tracker File not created!!")
    