import streamlit as st
import matplotlib.pyplot as plt

# Create a placeholder for the input
placeholder = st.empty()
gg_txt = st.empty()

# Function to update the placeholder with a plot
x = list(range(-100, 101))
y = [value * 2 for value in x]  # Correctly calculate y values
def update_placeholder(x, y):
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='y = 2x')
    ax.set_title('Dynamic Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.legend()
    
    with gg_txt:
        st.text('gg: '+str(gg))
    with placeholder:
        st.pyplot(fig)


# fig1,ax1 = plt.subplots()
# # ax1.plot([3, 4 , 5], [6, 8, 10])
# ax1.scatter(3, 6, color='r')
# st.pyplot(fig1)

# Display the initial plot
gg=-98
update_placeholder(x[gg], y[gg])

# Button to remove the current plot and replace it with a new one
if st.button("Remove and Replace"):
    # Clear the placeholder and add the new plot
    placeholder.empty()
    gg+=1
    update_placeholder(x[gg], y[gg])
