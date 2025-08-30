import numpy as np
import matplotlib.pyplot as plt

# --- Parameters ---
T = 200       # total time (ms)
dt = 0.1      # time step (ms)
time = np.arange(0, T, dt)

tau_m = 10.0   # membrane time constant (ms)
V_rest = -65   # resting potential (mV)
V_reset = -70  # reset potential (mV)
V_th = -50     # spike threshold (mV)
R = 10         # membrane resistance (MΩ)

I = 1.5        # input current (nA)

# --- Variables ---
V = np.ones(len(time)) * V_rest  # membrane potential trace
spikes = []

# --- Simulation ---
for t in range(1, len(time)):
    dV = (-(V[t-1] - V_rest) + R*I) / tau_m * dt
    V[t] = V[t-1] + dV
    
    if V[t] >= V_th:       # spike!
        V[t-1] = 20        # spike peak (for plotting)
        V[t] = V_reset     # reset potential
        spikes.append(time[t])

# --- Plot ---
plt.figure(figsize=(10,5))
plt.plot(time, V, label="Membrane potential")
plt.axhline(V_th, color='r', linestyle='--', label="Threshold")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
plt.title("Leaky Integrate-and-Fire Neuron")
plt.legend()
plt.show()