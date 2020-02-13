import neurons
import matplotlib.pyplot as plt
import time

history = []

network = neurons.Network(256)

s = neurons.Sensory()
n = neurons.Unit()
n.add_input(s)

for i in range(0, 1000):
    if 400 <= i <= 700:
        x = 100
    else: x = 0
    s.activate(x)
    n.activate()
    n.update()
    history.append(n.output)

plt.plot(history)
plt.show()
