import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

st.title('Dynamic Scatter Plot Example')

# Create a button to start the update process
start_btn = st.button('Start Updating Scatter Plot')

# Initialize empty lists for x and y coordinates
x_data = []
y_data = []

# Create a figure for the scatter plot
cont = st.container(border=True)
fig, ax = plt.subplots()

# Function to update the scatter plot
def update_scatter_plot():
    ax.clear()  # Clear the previous plot
    ax.scatter(x_data, y_data, color='blue')  # Update with new data
    ax.set_xlim(-10, 10)  # Set x-axis limits
    ax.set_ylim(-10, 10)  # Set y-axis limits
    ax.set_title('Dynamic Scatter Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    cont.pyplot(fig, clear_figure=True)  # Render the updated plot
    cont.empty()

if start_btn:
    for i in range(10):  # Update the plot 10 times
        # Generate new random coordinates
        new_x = np.random.uniform(-10, 10)
        new_y = np.random.uniform(-10, 10)
        
        # Append new coordinates to the data lists
        x_data.append(new_x)
        y_data.append(new_y)
        
        # Update the scatter plot
        update_scatter_plot()
        
        time.sleep(1)  # Pause for a second before the next update
