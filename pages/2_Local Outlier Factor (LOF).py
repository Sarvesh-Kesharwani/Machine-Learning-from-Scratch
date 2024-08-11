import streamlit as st

st.header("Local Outlier Factor (LOF) Simulation")
st.sidebar.title('Inputs')
st.sidebar.number_input('Inputs', 1, 10)

from sklearn.datasets import make_blobs
from numpy import quantile, random, where
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt