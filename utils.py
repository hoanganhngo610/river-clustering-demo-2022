from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook
from bokeh.layouts import gridplot
from bokeh.palettes import Pastel1
from bokeh.models import Span

import numpy as np

output_notebook()

color_0 = Pastel1[3][0]
color_1 = Pastel1[3][1]
color_2 = Pastel1[3][2]

# Auxiliary function to plot the data
def plot_data(dist_a, dist_b, dist_c, drifts=None):
    left = figure(plot_width=600, plot_height=400,
                  tools="pan,box_zoom,reset,save",
                  title="drift stream",
                  x_axis_label='samples', y_axis_label='value',
                  background_fill_color="#fafafa",
                  border_fill_color=None
                  )
    # add some renderers
    left.circle(range(1000), dist_a, legend_label=r"dist_a",
                fill_color=color_0, line_color=color_0, size=4)
    left.circle(range(1000, 2000, 1), dist_b, legend_label=r"dist_b",
                fill_color=color_1, line_color=color_1, size=4)
    left.circle(range(2000, 3000, 1), dist_c, legend_label=r"dist_c",
                fill_color=color_2, line_color=color_2, size=4)

    right = figure(plot_width=300, plot_height=400,
                   tools="pan,box_zoom,reset,save",
                   title="distributions",
                   background_fill_color="#fafafa"
                   )
    hist, edges = np.histogram(dist_a, density=True, bins=50)
    right.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
               fill_color=color_0, line_color=color_0, legend_label='dist_a')
    hist, edges = np.histogram(dist_b, density=True, bins=50)
    right.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
               fill_color=color_1, line_color=color_1, legend_label='dist_b')
    hist, edges = np.histogram(dist_c, density=True, bins=50)
    right.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
               fill_color=color_2, line_color=color_2, legend_label='dist_c')
    
    if drifts is not None:
        for drift_loc in drifts:
            drift_line = Span(location=drift_loc, dimension='height',
                              line_color='red', line_width=2)
            left.add_layout(drift_line)
    
    p = gridplot([[left, right]])

    show(p)