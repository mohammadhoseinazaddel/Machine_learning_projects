import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Spectral3
from bokeh.transform import factor_cmap
output_file('thor3.html')

data = pd.read_csv('thor_wwii.csv')
data = data[data['COUNTRY_FLYING_MISSION'].isin(('USA', 'GREAT BRITAIN'))]
dataGrouped = data.groupby('COUNTRY_FLYING_MISSION')['TOTAL_TONS', 'TONS_FRAG', 'TONS_IC', 'TONS_HE'].sum()

dataSource = ColumnDataSource(dataGrouped)
coutries = dataSource.data['COUNTRY_FLYING_MISSION'].tolist()
p = figure(x_range=coutries)

p.vbar_stack(source=dataSource, x='COUNTRY_FLYING_MISSION', width=0.7, color=Spectral3, stackers=['TONS_FRAG', 'TONS_IC', 'TONS_HE'], legend=['قطعات', 'اتشعال‌زا', 'انفجار قوی'])

show(p)