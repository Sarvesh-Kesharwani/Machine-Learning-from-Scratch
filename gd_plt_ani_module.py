import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

st.title('Gradient Descent')
input_x = st.number_input('Initial Position', -100, 100)
start_btn = st.button('Start')
stop_btn = st.button('Stop')
position_corr_text = st.empty()

def y_function(x):
    return x**2

def y_derivative(x):
    return 2*x

# Generate x values for the parabola
x = np.linspace(-100, 100, 200)
y = np.array(list(map(y_function, x)))

# Initialize current position based on user input
current_pos = input_x, y_function(input_x)
learning_rate = 0.01

# Create an empty chart
gd_plot = st.empty()

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.plot(x, y, label='y = x^2')
point, = ax.plot([], [], 'ro', markersize=10)  # 'ro' means red color, circle marker
ax.set_xlim(-100, 100)  # Set x limits
ax.set_ylim(-10, 10000)  # Set y limits to accommodate the parabola
ax.set_title('Gradient Descent')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()

# Function to initialize the plot
def init():
    point.set_data([], [])
    return point,

# Function to update the plot for each frame
def update(frame):
    global current_pos
    new_x = current_pos[0] - learning_rate * y_derivative(current_pos[0])
    new_y = y_function(new_x)
    current_pos = new_x, new_y
    point.set_data([current_pos[0]], [current_pos[1]])  # Update point position
    position_corr_text.text(f'x: {current_pos[0]:.2f} y: {current_pos[1]:.2f}')
    return point,

# Animation control
if start_btn:
    # Reset current position based on user input
    current_pos = input_x, y_function(input_x)

    # Create the animation
    ani = animation.FuncAnimation(fig, update, frames=200, init_func=init, interval=100, blit=True)

    # Render the plot in Streamlit
    while True:
        gd_plot.pyplot(fig)
        if stop_btn:
            break

if stop_btn:
    position_corr_text.text("Animation stopped.")
