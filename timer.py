import time

# Install Python For Linux If your OS is windows change this line please
# input hour
timer = float(input("how can today? "))
if timer < 5 and timer > 0:
    seconds = 0
    miniutes = 0
    for i in range(0, timer): # loop for calculate time
        while seconds == time * 3600: # calculate time for send notification
            seconds = seconds + 1
            print(seconds)
            time.sleep(1) # Delay
            if seconds == 60: # calculate miniutes
                miniutes = miniutes + 1
                if miniutes == 25: # Send Notf
                    print("Time to have some tea or coffee and rest for a few minutes. Dont be tired")
else:
    exit("Err: hour is not authentic")
