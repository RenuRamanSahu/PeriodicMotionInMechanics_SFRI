import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation



scale = 0.75
fig, ax = plt.subplots(figsize = (3.6,3.6))
L = 1*scale
g = 9.8
T = 2*np.pi*np.sqrt(L/g)
print(T)
time = np.linspace(0, 4*T, 361)
dT = time[1]-time[0]
frameInterval = int(dT*1e3)

theta = 2*np.pi*time/T
Alpha_amplitude =      0.2*L/L                                #10*np.pi/180#angularAmplitude
alpha = Alpha_amplitude*np.sin(theta)
y = -L*np.cos(alpha)
x = -L*np.sin(alpha)
# x = np.cos(theta)
# y = np.sin(theta)
constantValueArray = L*0.25*np.ones(361)

ax.plot(x, y, color = 'b', lw = 0.5)
ax.plot(0,0, 'o',color = 'b', lw = 3)
Lmax = 1.5
Lmin = 0.2
# ax.plot(x, constantValueArray, color = 'g', lw = 3)
ax.plot([0, x[0]], [0, y[0]], color = 'black', lw = 0.5)
ax.set_xlabel('x (m)', fontsize = 12)
ax.set_ylabel('y (m)', fontsize = 12)
ax.set_xlim(-0.75, 0.75)
L_lim_range = Lmax
ax.set_ylim(-0.9*L_lim_range, 0.1*L_lim_range)
ax.set_yticks([-1.25, -1, -0.75, -0.5, -0.25, 0])
ax.tick_params(axis = 'both', direction = 'in')
ax.set_aspect(1) 

ax.grid(which = 'major', axis = 'both', lw = 0.1)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)

dot, = ax.plot(x[0], y[0], 'o', color = 'r', lw = 10)
# projection_x, = ax.plot(x[0], constantValueArray[0], 's', color = 'r')
# projection_line, = ax.plot([x[0], x[0]], [constantValueArray[0], y[0]], color = 'r', lw = 0.5)
rotor, = ax.plot([0, x[0]], [0, y[0]], color = 'black', lw = 0.5)


def init():
    # ax.set_xlim(-Lmax, Lmax)
    # ax.set_ylim(-1.25*Lmax, Lmax)
    # ax.set_xticks([-L, 0, L])
    # ax.set_yticks([-L, 0, L])
    return dot,# projection_x

def update(frame):
    # for each frame, update the data stored on each artist.
    dot.set_xdata([x[frame]])
    dot.set_ydata([y[frame]])
    
    # projection_x.set_data([x[frame]], [constantValueArray[frame]])
    
    # projection_line.set_data([x[frame], x[frame]], [constantValueArray[frame], y[frame]])
    rotor.set_data([0, x[frame]], [0, y[frame]])
    return dot, #projection_x
plt.tight_layout()
ani = animation.FuncAnimation(fig=fig, init_func=init, func=update, frames=361, interval=frameInterval)

##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################






plt.show()