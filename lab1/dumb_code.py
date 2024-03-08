
def time(speed, distance):
    
    if speed == 0:
        raise ValueError("Can't divide by 0")
    
    time = distance / speed

    return time

   