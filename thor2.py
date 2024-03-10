#data import
import pandas as pd

#visualization import
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Spectral3
from bokeh.transform import factor_cmap

# creat output html file
output_file('thor2.html')

#read thor_wwii data
data = pd.read_csv('thor_wwii.csv')
data = data[data['COUNTRY_FLYING_MISSION'].isin(('USA', 'GREAT BRITAIN'))]

#groupby data according of COUNTRY_FLYING_MISSION column
dataGroup = data.groupby('COUNTRY_FLYING_MISSION')['TOTAL_TONS', 'TONS_IC', 'TONS_HE', 'TONS_FRAG'].sum()
# print(dataGroup)

#creating a ColumnDataSource
datasource = ColumnDataSource(dataGroup) 

countries = datasource.data['COUNTRY_FLYING_MISSION'].tolist()

#creating plot
p = figure(x_range = countries)

    #--->>> creat a color map
# cm = factor_cmap(field_name= 'COUNTRY_FLYING_MISSION', palette= Spectral5, factors= countries)

# p.vbar(source= datasource, x='COUNTRY_FLYING_MISSION', top= 'TONS_HE', color= cm, width= 0.6)
p.vbar_stack(source= datasource, x='COUNTRY_FLYING_MISSION', stackers= ['TONS_HE', 'TONS_IC', 'TONS_FRAG'],
legend= ['اشتعال زا', 'انفجار قوی', 'قطعات'], color= Spectral3, width= 0.6)

#show the plot
show(p)
