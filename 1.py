from numpy import *
import matplotlib.pyplot as plt
from matplotlib import animation
 
fig,ax=plt.subplots()   #相当于fig=plt.figure(),ax=plt.subplot();ax=plt.subplot也可以是ax=fig.add_subplot()
x=arange(0,2*pi,0.01)
line,=ax.plot(x,sin(x))
 
def update(i):
    line.set_ydata(sin(x+i/10))
    return line,
def init():
    line.set_ydata(sin(x))
    return line,
 
ani=animation.FuncAnimation(fig=fig,func=update,frames=100,init_func=init,interval=20,blit=False)
plt.show()