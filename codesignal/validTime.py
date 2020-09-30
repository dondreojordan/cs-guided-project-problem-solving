def validTime(time):
    h, m = time.split(':')
    return 0<=int(h)<24 and 0<=int(m)<60

time = "08:50"
print(validTime(time))