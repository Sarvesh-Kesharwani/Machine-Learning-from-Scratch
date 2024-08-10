import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

st.title('Gradient Descent')
input_x = st.number_input('Initial Position', -100, 100)
start_btn = st.button('Start')
stop_btn = st.button('Stop')
position_corr_text = st.empty()

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

# Create an empty chart
gd_plot = st.empty()

def animate(current_pos):
    fig, ax = plt.subplots()
    # updating coordinates
    new_x = current_pos[0] - learning_rate * y_derivative(current_pos[0])
    new_y = y_function(new_x)
    current_pos = new_x, new_y
    # plotting
    # parabola line chart
    ax.plot(x, y, label='y = x^2')
    # single dot scatter plot
    ax.scatter(current_pos[0], current_pos[1], color='red')
    # setting lengends
    ax.set_title('Gradient Descent')
    ax.set_xlabel(f'X-axis: {current_pos[0]}')
    ax.set_ylabel(f'Y-axis: {current_pos[1]}')
    ax.legend()
    # showing current position values    
    position_corr_text.text('x: '+str(current_pos[0])+' y: '+str(current_pos[1]))
    # rendering the updated frame
    gd_plot.altair_chart(fig)

if start_btn:
    for _ in range(200):
        animate(current_pos)
        time.sleep(0.1)
        if stop_btn:
            break


