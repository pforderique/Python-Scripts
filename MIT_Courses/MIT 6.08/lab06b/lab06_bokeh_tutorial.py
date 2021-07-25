import os
os.environ["BOKEH_RESOURCES"] = 'inline'

import numpy as np
from bokeh.plotting import figure, show

x = np.linspace(0, 4*np.pi, 100) #create array for x
y = np.sin(x)  #create sine based off of x

p = figure() #create a figure called p

p.circle(x, y, legend_label="sin(x)") # add a circle plot of x vs. y arrays
p.line(x, y, legend_label="sin(x)") #add a line plot of x vs. y arrays

# add another line that is x and 2*y (numpy array keep in mind), make dashed, orange, thicker:
p.line(x, 2*y, legend_label="2*sin(x)", line_dash=[4, 4], line_color="orange", line_width=2)

# like circle plot but with squares and y is scaled by three:
p.square(x, 3*y, legend_label="3*sin(x)", fill_color=None, line_color="green")
p.line(x, 3*y, legend_label="3*sin(x)", line_color="green")

show(p) #render it in your browser