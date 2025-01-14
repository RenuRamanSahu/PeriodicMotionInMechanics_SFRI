import numpy as np
import matplotlib.pyplot as plt



from matplotlib.widgets import Button, Slider 


# The parametrized function to be plotted
def f(t, amplitude, frequency, phi):
    return amplitude * np.cos(2 * np.pi * frequency * t + phi)

t = np.linspace(0, 1, 1000)

# Define initial parameters
init_amplitude = 2
init_frequency = 1.0/(0.1*np.pi)
init_phase = np.pi

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots(figsize = (10, 6))
line, = ax.plot(t, f(t, init_amplitude, init_frequency, init_phase),color = 'r', lw=3)
ax.set_ylim(-5, 5)
ax.set_xlabel('Time [s]')
title_txt_pre = r"$x(t)$ = $A$ cos ( $\omega$ t + $\phi$) = "
title_txt = title_txt_pre+" {A:.2f} cos( {omega:.2f} t + {phi:.2f}) ".format(A=init_amplitude, omega=2*np.pi*init_frequency, phi=init_phase)
ax.set_title(title_txt)

# adjust the main plot to make room for the sliders
fig.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the frequency.
axfreq = fig.add_axes([0.25, 0.125, 0.65, 0.03])
freq_slider = Slider(
    ax=axfreq,
    label=r'Frequency, $\nu = \dfrac{1}{T} = \dfrac{\omega}{2\pi}$ [Hz]',
    valmin=0.1,
    valmax=10,
    valinit=init_frequency,
)

# Make a horizontal slider to control the frequency.
axPhase = fig.add_axes([0.25, 0.025, 0.65, 0.03])
phase_slider = Slider(
    ax=axPhase,
    label=r'Phase, $\phi$ [Radians]',
    valmin=0.0,
    valmax=10,
    valinit=init_phase,
)


# Make a vertically oriented slider to control the amplitude
axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
amp_slider = Slider(
    ax=axamp,
    label="Amplitude, ${A}$",
    valmin=0.1,
    valmax=4,
    valinit=init_amplitude,
    orientation="vertical"
)


# The function to be called anytime a slider's value changes
def update(val):
    line.set_ydata(f(t, amp_slider.val, freq_slider.val, phase_slider.val))
    omega = 2*np.pi*freq_slider.val
    A  = amp_slider.val
    phi =  phase_slider.val
    title_txt_pre = r"$x(t)$ = $A$ cos ( $\omega$ t + $\phi$) = "
    title_txt = title_txt_pre+" {A:.2f} cos( {omega:.2f} t + {phi:.2f}) ".format(A=A, omega=omega, phi=phi)
    ax.set_title(title_txt)
    fig.canvas.draw_idle()


# register the update function with each slider
freq_slider.on_changed(update)
amp_slider.on_changed(update)
phase_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = fig.add_axes([0.8, 0.9, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    freq_slider.reset()
    amp_slider.reset()
button.on_clicked(reset)

# manager = plt.get_current_fig_manager()
# manager.full_screen_toggle()
plt.show()
