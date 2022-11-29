import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Spectral5
from bokeh.transform import factor_cmap
output_file('thor2.html')

data = pd.read_csv('thor_wwii.csv')
dataGrouped = data.groupby('COUNTRY_FLYING_MISSION')['TOTAL_TONS', 'TONS_FRAG', 'TONS_IC', 'TONS_HE'].sum()

dataSource = ColumnDataSource(dataGrouped)
coutries = dataSource.data['COUNTRY_FLYING_MISSION'].tolist()
p = figure(x_range=coutries)

cm = factor_cmap(field_name='COUNTRY_FLYING_MISSION', palette=Spectral5, factors=coutries)

p.vbar(source=dataSource, x='COUNTRY_FLYING_MISSION', top='TOTAL_TONS', width=0.7, color=cm)
h = HoverTool()
h.tooltips = [
    ('جمع',
    'جمع مواد منفجره تفکیک قوی @TONS_HE است و جمع مواد آتش‌زا @TONS_IC است و تعداد @TONS_FRAG قطعه منفجر شده است')
]
h.mode = 'vline'
p.add_tools(h)
show(p)