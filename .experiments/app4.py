import streamlit as st
import altair as alt
import pandas as pd
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

learning_rate = 0.01

# Create an empty chart
gd_plot = st.empty()

def animate(start_pos, num_steps=200):
    data = pd.DataFrame({
        'x': np.zeros(num_steps),
        'y': np.zeros(num_steps),
        'step': np.arange(num_steps)
    })
    
    current_pos = start_pos
    for i in range(num_steps):
        new_x = current_pos[0] - learning_rate * y_derivative(current_pos[0])
        new_y = y_function(new_x)
        current_pos = new_x, new_y
        data.iloc[i] = [current_pos[0], current_pos[1], i]
    
    # Create the point chart
    point_chart = alt.Chart(data).mark_point(color='red', size=100).encode(
        x='x',
        y='y',
        opacity=alt.value(0.2)  # Default opacity for all points
    ).transform_filter(
        alt.datum.step == data['step'].max()  # Filter to show only the last point
    )

    # Create the parabola chart
    parabola = alt.Chart(pd.DataFrame({'x': x, 'y': y})).mark_line(color='blue').encode(
        x='x',
        y='y'
    )

    # Combine the parabola and the gradient descent point
    final_chart = parabola + point_chart

    # Configure the overall chart
    final_chart = final_chart.properties(
        width=600,
        height=400
    ).configure_axis(
        grid=False
    ).configure_view(
        strokeWidth=0
    ).interactive()

    gd_plot.altair_chart(final_chart, use_container_width=True)
    
    return current_pos

if start_btn:
    current_pos = animate((input_x, y_function(input_x)))
    position_corr_text.text(f'x: {current_pos[0]:.2f} y: {current_pos[1]:.2f}')

if stop_btn:
    pass
