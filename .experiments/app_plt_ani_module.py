import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

# Create a DataFrame with x and y coordinates that change over time
data = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': np.sin(np.linspace(0, 10, 100)),
    'time': np.arange(100)
})

# Set up the Streamlit app
st.title("Animated Scatter Plot with Matplotlib")

# Create an empty placeholder for the plot
chart_placeholder = st.empty()

# Define constant axis limits
x_min, x_max = 0, 10
y_min, y_max = -1.5, 1.5

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
point, = ax.plot([], [], 'ro', markersize=10)  # 'ro' means red color, circle marker

# Function to initialize the plot
def init():
    point.set_data([], [])
    return point,

# Function to update the plot for each frame
def update(frame):
    current_data = data.iloc[frame]
    point.set_data([current_data['x']], [current_data['y']])  # Pass x and y as lists
    ax.set_title(f"Frame: {frame}, X: {current_data['x']:.2f}, Y: {current_data['y']:.2f}")
    return point,

# Animation loop
for i in range(len(data)):
    update(i)
    # Render the plot in Streamlit
    chart_placeholder.pyplot(fig)
    time.sleep(0.1)  # Pause for a short duration to create the animation effect
