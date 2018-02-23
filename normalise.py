import time 
from time import asctime, gmtime

def normalise(input_time):
    time_struct = gmtime(input_time)
    day = 24*60*60
    hour = 60*60
    minute = 60
    second = 1
    Y = asctime(time_struct)
    
    while Y[0:3]!= "Sun":
       input_time -= day
       Y = asctime(gmtime(input_time))

    new_y = Y[:11]+"00"+Y[13]+"00"+Y[16]+"00" +Y[19:]

    new_time = time.strptime(new_y,"%a %b %d %H:%M:%S %Y")
    
    input_time = time.mktime(new_time)

    return  input_time




input_time = time.time()
normalise(input_time)
