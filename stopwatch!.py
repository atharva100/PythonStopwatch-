# STOPWATCH 


import time
time.time()  # time func inside the time module

def time_calc(sec):   # we defined a func to calculate time elapsed
    print("time elapsed is : " + str(round(sec,3)) + " seconds ")

input("press enter to start : ")
start_time = time.time()          # start_time is an inbuilt func which starts timer

input("press enter to stop : ")
stop_time = time.time()           #stop_time is an inbuilt func which stops timer

time_lapsed = stop_time - start_time

time_calc(time_lapsed) # function call

print("have a nice day ! :)")




