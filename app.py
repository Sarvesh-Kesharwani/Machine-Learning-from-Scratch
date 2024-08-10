import streamlit as st 
import matplotlib.pyplot as plt

st.title('Anomaly Detection Simulation')

fig, ax = plt.subplots()
ax.scatter([2], [4])
st.pyplot(fig)

