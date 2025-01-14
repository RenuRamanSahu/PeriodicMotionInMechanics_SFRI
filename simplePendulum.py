import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation




fig, ax = plt.subplots(figsize = (4.8, 4.8))
R=1.
theta = np.linspace(0, 2*np.pi, 361)
Alpha_amplitude = 15*np.pi/180#angularAmplitude
alpha = Alpha_amplitude*np.sin(theta)
y = -R*np.cos(alpha)
x = -R*np.sin(alpha)


# x = np.cos(theta)
# y = np.sin(theta)
constantValueArray = 1.25*np.ones(361)

ax.plot(x, y, color = 'b', lw = 1.5)
ax.plot(0,0, 'o',color = 'b', lw = 3)

ax.plot(x, constantValueArray, color = 'g', lw = 3)
ax.plot( constantValueArray, y, color = 'g', lw = 3)
ax.plot([0, x[0]], [0, y[0]], color = 'black', lw = 0.5)
ax.set_xlabel('x', fontsize = 16)
ax.set_ylabel('y', fontsize = 16)
ax.set_xticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
ax.set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
ax.tick_params(axis = 'both', direction = 'in')
ax.grid(which = 'major', axis = 'both', lw = 0.1)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)



dot, = ax.plot(x[0], y[0], 'o', color = 'r', lw = 10)
projection_x, = ax.plot(x[0], constantValueArray[0], 's', color = 'r')
projection_y, = ax.plot( constantValueArray[0], y[0], 's', color = 'r')
projection_line, = ax.plot([x[0], x[0], constantValueArray[0]], [constantValueArray[0], y[0], y[0]], color = 'r', lw = 0.5)
rotor, = ax.plot([0, x[0]], [0, y[0]], color = 'black', lw = 0.5)


def init():
    ax.set_xticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
    ax.set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
    return dot, projection_x, projection_y

def update(frame):
    # for each frame, update the data stored on each artist.
    dot.set_xdata([x[frame]])
    dot.set_ydata([y[frame]])
    
    projection_x.set_data([x[frame]], [constantValueArray[frame]])
    projection_y.set_data([constantValueArray[frame]], [y[frame]])
    projection_line.set_data([x[frame], x[frame], constantValueArray[frame]], [constantValueArray[frame], y[frame],  y[frame]])
    rotor.set_data([0, x[frame]], [0, y[frame]])
    
    
    
    return (dot, projection_x, projection_y)

plt.tight_layout()


ani = animation.FuncAnimation(fig=fig, init_func=init, func=update, frames=361, interval=10)


plt.show()