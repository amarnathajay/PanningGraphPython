import matplotlib.pyplot as plotter
import matplotlib.animation as animator
import time

fig = plotter.figure()
animatedGraph = fig.add_subplot(1, 1, 1)

def animate(i):
    dataStream = open("data.txt", "r").read()
    extractedData = dataStream.split('\n')
    xData = []
    yData = []
    for eachLine in extractedData:
        if len(eachLine) > 1:
            x,y = eachLine.split(' ')
            xData.append(float(x))
            yData.append(float(y))
    animatedGraph.clear()
    animatedGraph.plot(xData, yData)
anim = animator.FuncAnimation(fig, animate, interval = 10)
plotter.show()