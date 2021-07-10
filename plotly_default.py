import plotly.graph_objects as go
import plotly.io as pio

# Visual style of Plotly graphs
axis_layout = {'showline': True, 'mirror': True, 'ticks': 'outside', 'showgrid': True, 'zeroline': True, 'linewidth': 1.3, 'color': 'black'}

axis_layout_3D = dict(showline = True, ticks = 'outside', linewidth = 2, color = 'black')

pio.templates['PM_graph_1'] = go.layout.Template(layout = dict(xaxis = axis_layout,
                          yaxis = axis_layout,
                          bargap = 0.05, bargroupgap = 0,
                          height = 700,
                          margin = dict(l=60, r=30, t=30, b=60),
                          hovermode = 'closest',
                          scene = {'xaxis': axis_layout_3D, 'yaxis': axis_layout_3D, 'zaxis': axis_layout_3D},
                          font_family = 'Arial', font_size=16, font_color='black'))
                         
pio.templates.default='PM_graph_1'

graph_config = {
  'toImageButtonOptions': {
    'format': 'svg', # one of png, svg, jpeg, webp
    'filename': 'plot_capture',
    'scale': 1 # Multiply title/legend/axis/canvas sizes by this factor
  },
    'displaylogo': False}