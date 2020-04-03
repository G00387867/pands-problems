#Adam Shaat
# a program that displays a plot of functions
#  f(x) = x, g(x) = x**2 and h(x) = x**3 in the range[0,4] on the one set of axes

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.0, 4.0)
y1 = x
y2 = x**2
y3 = x**3
plt.plot(x, y1, 'g.', label = 'f(x)') # plot of f(x) = x
plt.plot(x, y2, 'r.', label = 'g(x)') # plot of g(x) = x**2
plt.plot(x, y3, 'b.', label = 'h(x)') # plot of h(x) = x**3

# legend of graphs output
plt.legend()
# title for the graph
plt.title('Task08')
