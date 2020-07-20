import random
import time

for x in range(360):
    data = open("data.txt", "a")
    line1 = str(x)
    line2 = str(random.uniform(1,10))
    data.write(line1 + ' ' + line2 + '\n')
    data.close()
    time.sleep(0.1)