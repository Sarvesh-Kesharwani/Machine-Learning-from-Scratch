import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
i   mport time

# Create a DataFrame with x and y coordinates that change over time
data = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': np.sin(np.linspace(0, 10, 100)),
    'time': np.arange(100)
})

# Create an empty chart
chart = st.empty()

# Define constant axis limits
x_min, x_max = 0, 10
y_min, y_max = -1.5, 1.5

# Animate the scatter plot
for i in range(len(data)):
    # Select the current data point
    current_data = data.iloc[i:i+1]
    
    # Create the scatter plot with fixed axis limits
    scatter = alt.Chart(current_data).mark_circle(size=100).encode(
        x=alt.X('x', scale=alt.Scale(domain=[x_min, x_max])),
        y=alt.Y('y', scale=alt.Scale(domain=[y_min, y_max]))
    ).properties(width=600, height=400)
    
    # Display the chart
    chart.altair_chart(scatter)
    
    # Pause for a short duration to create the animation effect
    time.sleep(0.1)
