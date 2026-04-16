# Consistency-Fed-Terminal-Plant
A funny command line interface programming companion that feeds on user's productivity and dies from user's inconsistency
The Consistency-Fed Terminal Plant is designed for developers. It lives in your shell and survives entirely on your IDE activity.

**Thriving** :- If you have saved code within 2 hours of your current time, the plant is active.

**Wilting** :- If you haven't coded in a few hours, it starts to droop and nag you to code as you open your terminal.

**Dead** :- After 24 hours inactivity, it dies and guilt trip you.

## Working

**recorder.py** :- It is the background script that uses **watchdog** library. When its running, It monitors your project directory and update a timestamp in **time_tracker.txt** based on the time you have recently edited a file. It is integrated with Task scheduler on Windows so that it automatically kept running in the background.

**plant_logic.py** :- This script simulates the plant behaviour after calculating the time difference. It is hooked into user's Powershell **$PROFILE**, so that whenever user open the powershell it reminds its condition to the User by ASCII Art. 
*Note* :- User can use his own ASCII art style from any website. Just edit the ASCII art in the respective .txt files.

## How to use

Edit the directory paths with your own directory where your programming projects are placed and where you want the **time_tracker.txt** to be saved.
Use Task scheduler (if you are in Windows) to make the **recorder.py** run in background after starting. For Linux and MacOS investigate how you can automatically run a python script in background.
For hooking the **plant_logic.py** into Powershell, Open Powershell and write **notepad $PROFILE** and then in the .txt file write the execution command of the python file.. **python {directory of plant_logic.py}\plant_logic.py**

And its Good to go.

Thank You and Happy Programming
