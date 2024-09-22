import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to generate individual sine waves
def generate_sine_wave(w, a, x):
    return a * np.sin(w * x)

# App layout
st.title("Interactive Sine Wave Mixer")

# Sidebar inputs
st.sidebar.header("Wave Parameters")
frequency1 = st.sidebar.slider('Frequency of First Wave (ω₁)', 1, 20, 1)
frequency2 = st.sidebar.slider('Frequency of Second Wave (ω₂)', 1, 20, 10)
amplitude1 = st.sidebar.slider('Amplitude of First Wave (A₁)', 0.1, 2.0, 1.0)
amplitude2 = st.sidebar.slider('Amplitude of Second Wave (A₂)', 0.1, 2.0, 0.2)

# X range for plotting
x = np.linspace(0, 2 * np.pi, 1000)

# Generate individual waves and the mixed wave
wave1 = generate_sine_wave(frequency1, amplitude1, x)
wave2 = generate_sine_wave(frequency2, amplitude2, x)
mixed_wave = wave1 + wave2

# Plotting
fig, ax = plt.subplots()
ax.plot(x, wave1, label=f'A₁sin(ω₁x)', color='blue',linestyle='--')
ax.plot(x, wave2, label=f'A₂sin(ω₂x)', color='red',linestyle='--')
ax.plot(x, mixed_wave, label=f'Mixed Wave', color='k', linestyle='-')

ax.set_xlabel("x")
ax.set_ylabel("Wave Amplitude")
ax.legend()
st.pyplot(fig)

# Show equation
st.write(f"**Equation:** \n")
st.latex(f"I = {amplitude1}\sin({frequency1}x) + {amplitude2}\sin({frequency2}x)")

