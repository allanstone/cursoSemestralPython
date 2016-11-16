import pylab as pb
import numpy as np

x = np.linspace(-15,15,100)
y = np.sin(x)/x

pb.plot(x,y)
pb.plot(x,y,'co')
pb.plot(x,2*y,x,3*y)

pb.show()