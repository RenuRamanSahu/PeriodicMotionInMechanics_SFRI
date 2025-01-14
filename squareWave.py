import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation



scale = 1.2
fig, ax = plt.subplots(figsize = (scale*8, scale*4.5))

theta = np.linspace(0, 2*np.pi, 361)
x = np.cos(theta)
y =(np.sin(theta))+(1./3.0)*np.sin(3*theta)+(1./5.0)*np.sin(5*theta) + (1./7.0)*np.sin(7*theta)+ (1./9.0)*np.sin(9*theta)

constantValueArray = 1.25*np.ones(361)

ax.plot(x, y, color = 'b', lw = 3)
ax.plot(0,0, 'o',color = 'b', lw = 3)

ax.plot(x, constantValueArray, color = 'g', lw = 3)
ax.plot( constantValueArray, y, color = 'g', lw = 3)
ax.plot([0, x[0]], [0, y[0]], color = 'black', lw = 0.5)
ax.set_xlabel('x', fontsize = 16)
ax.set_ylabel('y', fontsize = 16)
ax.set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
ax.set_xticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3])
ax.tick_params(axis = 'both', direction = 'in')
ax.grid(which = 'major', axis = 'both', lw = 0.1)
ax.set_aspect(1)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)



dot, = ax.plot(x[0], y[0], 's', color = 'r', lw = 4)
projection_x, = ax.plot(x[0], constantValueArray[0], 'o', color = 'r')
projection_y, = ax.plot( constantValueArray[0], y[0], 'o', color = 'r')
projection_line, = ax.plot([x[0], x[0], constantValueArray[0]], [constantValueArray[0], y[0], y[0]], color = 'r', lw = 0.5)
rotor, = ax.plot([0, x[0]], [0, y[0]], color = 'black', lw = 0.5)


ax1 = ax.inset_axes([0.4, 0.1, 0.55, 0.8])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([])
t = [0]
yt = [y[0]]
sine, = ax1.plot(t, yt,'.', color = 'r')

t0 = time.time()
def init():
    ax.set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
    ax.set_xticks([-1.5, -1, -0.5, 0, 0.5, 1,  2,  3, 4, 5, 6])
    ax1.set_xticks([])
    ax1.set_ylim(-1.2, 1.2)


    return dot, projection_x, projection_y

def update(frame):
    # for each frame, update the data stored on each artist.
    dot.set_xdata([x[frame]])
    dot.set_ydata([y[frame]])
    
    projection_x.set_data([x[frame]], [constantValueArray[frame]])
    projection_y.set_data([constantValueArray[frame]], [y[frame]])
    projection_line.set_data([x[frame], x[frame], constantValueArray[frame]], [constantValueArray[frame], y[frame],  y[frame]])
    rotor.set_data([0, x[frame]], [0, y[frame]])
    
    t = sine.get_xdata()
    t_val = time.time()-t0
    t = np.append([-t_val], t)
    yt = sine.get_ydata()
    yt = np.append(  [y[frame]], yt)
    ax1.set_xlim(-t_val-1, -t_val+15)
    sine.set_data(t, yt)
    
    
    
    return (dot, projection_x, projection_y)



ani = animation.FuncAnimation(fig=fig, init_func=init, func=update, frames=361, interval=10)


plt.show()