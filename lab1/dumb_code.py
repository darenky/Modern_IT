
def time(speed, distance):
    
    if speed == 0:
        raise ValueError("Can't divide by 0")
    
    if speed < 0 or distance < 0:
        raise ValueError("In my task, speed or distance can't be negative.")
    
    time = distance / speed

    return time

   