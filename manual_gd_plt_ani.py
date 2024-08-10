import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

# Create a DataFrame with x and y coordinates that change over time
data = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': np.linspace(0, 10, 100)*2,
    'time': np.arange(100)
})



# Define constant axis limits
x_min, x_max = -20, 20
y_min, y_max = -10, 10

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
point, = ax.plot([], [], 'ro', markersize=10)  # 'ro' means red color, circle marker


############################################################
st.title('Gradient Descent')
input_x = st.number_input('Initial Position', -100, 100)
st_c_point = st.text('')

# Create an empty placeholder for the plot
chart_placeholder = st.empty()

start_btn = st.button('Start')
stop_btn = st.button('Stop')

def y_function(x):
    return x**2

def y_derivative(x):
    return 2*x

x = list(range(-100, 101))
y = list(map(y_function, x))

# current_pos = 50, y_function(50)
current_pos = -50, y_function(-50)
current_pos = input_x, y_function(input_x)
learning_rate = 0.01
############################################################


# Function to initialize the plot
def init():
    point.set_data([], [])
    return point,

# Function to update the plot for each frame
def update(frame):
    current_data = data.iloc[frame]
    point.set_data([current_data['x']], [current_data['y']])  # Pass x and y as lists
    ax.set_title(f"Frame: {frame}, X: {current_data['x']:.2f}, Y: {current_data['y']:.2f}")
    return current_data['x'], current_data['y']

# Animation loop
if start_btn:
    for i in range(len(data)):
        # Updating frame
        c_point = update(i)
        st_c_point.text(str(c_point))
        # Render the plot in Streamlit
        chart_placeholder.pyplot(fig)
        time.sleep(0.1)  # Pause for a short duration to create the animation effect
        if stop_btn:
            break