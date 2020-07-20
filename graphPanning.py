#Author - Ajay Amarnath
#Email - amarnathajay@gmail.com

#import numpy
import matplotlib.pylab as plotter
from mpl_toolkits.axes_grid1 import host_subplot
import matplotlib.animation as animation

fig = plotter.figure()
fig.suptitle("Data example for a panning graph", fontsize = 12)
animatedGraph = fig.add_subplot(1, 1, 1)
animatedGraph.set_title('Magnitude vs heading')
animatedGraph.set_xlim(0, 20)
animatedGraph.grid(True)
animatedGraph.set_xlabel("Hdng (deg)")
animatedGraph.set_ylabel("Magnitude")

xmin = 0.0
xmax = 20.0
x = []
y = []
i = 0

p011, = animatedGraph.plot(x,y,'b-', label="Magnitude")



dataStream = open("data.txt", "r").read()
extractedData = dataStream.split('\n')
xData = []
yData = []
for eachLine in extractedData:
    if len(eachLine) > 1:
        xFile,yFile = eachLine.split(' ')
        xData.append(int(xFile))
        yData.append(float(yFile))
        #print(xFile, yFile)

def update(self):
    global x
    global y
    global xData
    global yData
    global i

    x.append(float(xData[i]))
    y.append(float(yData[i]))

    print(x[i], y[i])

    p011.set_data(x, y)

    if x[i] >= xmax - 1.00:
        p011.axes.set_xlim(x[i]-xmax+1.0,x[i]+1.0)
    
    i += 1

    return p011

#for eachNum in xData:
#    print(xData[eachNum], yData[eachNum])

simulation = animation.FuncAnimation(fig, update, blit=False, frames=359, interval=20, repeat=False)

# Uncomment the next line if you want to save the animation
#simulation.save(filename='sim.mp4',fps=30,dpi=300)

plotter.show()



