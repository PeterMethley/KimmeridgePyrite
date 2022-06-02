import plotly.graph_objects as go
import plotly.io as pio


def sel_trace(plot, value, prop='name'):
    '''Takes a Plotly FigureWidget and returns the appropriate trace object(s) where the property prop (defaults to the trace name) matches the given values.
    
    Parameters:
    -----------
    plot: Plotly FigureWidget object to select traces from.
    
    value: String, or list of strings, to filter traces by
    
    prop: String to determine which property to filter. Defaults to 'name'. Accepts magic underscore notation.
    
    Returns:
    --------
    A list of Plotly trace objects where prop == value. If the list is only one item long, the single trace is returned.
    '''
    
    if type(value) != list:
        values = [value]
    else:
        values = value
    
    trace_list = [d for d in plot.data if d[prop] in values]
    
    if len(trace_list) == 1:
        return trace_list[0]
    elif len(trace_list) == 0:
        print(f'No traces match the given criteria of {prop} == {value}.')
    else:
        return trace_list


# Visual style of Plotly graphs

black_color = '#231F20' # CMYK 100% black
grid_color = '#E2E7ED' # Default is #eee

axis_layout = {'showline': True, 'mirror': True, 'ticks': 'outside', 'showgrid': True, 'zeroline': True, 'linewidth': 1.3, 'color': black_color, 'gridcolor': grid_color}
axis_layout_3D = dict(showline = True, ticks = 'outside', linewidth = 2, color = black_color, gridcolor=grid_color)

pio.templates['PM_graph_1'] = go.layout.Template(layout = dict(xaxis = axis_layout,
                          yaxis = axis_layout,
                          bargap = 0.05, bargroupgap = 0,
                          height = 700,
                          margin = dict(l=100, r=30, t=30, b=70),
                          hovermode = 'closest',
                          scene = {'xaxis': axis_layout_3D, 'yaxis': axis_layout_3D, 'zaxis': axis_layout_3D},
                          font_family = 'Segoe UI', font_size=20, font_color=black_color, # Default font size = 1
                          plot_bgcolor = 'rgba(255,255,255,180)',
                          paper_bgcolor = 'rgba(255,255,255,0)'))
                         
pio.templates.default='PM_graph_1'

graph_config = {
  'toImageButtonOptions': {
    'format': 'pdf', # one of png, svg, jpeg, webp
    'filename': 'plot_capture',
    'scale': 1 # Multiply title/legend/axis/canvas sizes by this factor
  },
    'displaylogo': False}


