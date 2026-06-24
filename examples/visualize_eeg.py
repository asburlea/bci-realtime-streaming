"""
Live visualization of EEG stream
"""

import matplotlib.pyplot as plt
from src.inlet import create_inlet
from src.buffer import CircularBuffer

FS = 250
BUFFER_SEC = 2
N_CHANNELS = 8

inlet = create_inlet()
buffer = CircularBuffer(FS * BUFFER_SEC, N_CHANNELS)

plt.ion()
fig, ax = plt.subplots()

while True:
    sample, _ = inlet.pull_sample()
    buffer.append(sample)
    data = buffer.get()

    ax.clear()
    ax.plot(data)
    ax.set_title("Live EEG (Simulated)")
    plt.pause(0.01)
