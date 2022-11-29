import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Spectral3
from bokeh.transform import factor_cmap
output_file('thor4.html')

data = pd.read_csv('thor_wwii.csv')
data['MSNDATE'] = pd.to_datetime(data['MSNDATE'], format='%m/%d/%Y')
dataGrouped = data.groupby('MSNDATE')['TOTAL_TONS', 'TONS_FRAG', 'TONS_IC', 'TONS_HE'].sum()
dataSource = ColumnDataSource(dataGrouped)
p = figure(x_axis_type='datetime')
p.line(x='MSNDATE', y='TOTAL_TONS', source=dataSource, color='blue', legend='کل انفجارها', line_width=2)
p.line(x='MSNDATE', y='TONS_IC', source=dataSource, color='green', legend='اتش‌زا', line_width=2)
p.line(x='MSNDATE', y='TONS_HE', source=dataSource, color='red', legend='انفجار قوی', line_width=2)

show(p)