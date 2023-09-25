'''trying to create the signal with the gaussian noise'''

import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.animation as animation

t = np.linspace(1, 100, 1000)
x = 10*np.sin(t/(2*np.pi))
plt.subplot(3,1,1)   #dividing the plot into one third part of the graph
plt.plot(t, x)
plt.title('Sinusoidal Signal') 
plt.ylabel('Value (V)')
plt.xlabel('Time (s)')
#plt.show()

'''now  add the gaussian noise'''
tar_noise=10
mean_noise=0
noise=np.random.normal(mean_noise, np.sqrt(tar_noise),len(x**2))

sig_avg= np.mean(x)
print(sig_avg)


y=x+noise
plt.subplot(3,1,3)
plt.plot(t, y)
plt.title('Signal with noise')
plt.ylabel('Value (V)')
plt.xlabel('Time (s)')
plt.show()
