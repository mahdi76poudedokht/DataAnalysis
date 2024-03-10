#data import
import pandas as pd

#visualization import
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Spectral3
from bokeh.transform import factor_cmap

# creat output html file
output_file('thor3.html')

#read thor_wwii data
data = pd.read_csv('thor_wwii.csv')

#exchange type of MSNDATE to datetime
data['MSNDATE'] = pd.to_datetime(data['MSNDATE'], format= '%m/%d/%Y')

#groupby and resample data according of MSNDATE column
dataGroup = data.groupby(pd.Grouper(key='MSNDATE', freq='M'))['TOTAL_TONS', 'TONS_IC', 'TONS_HE', 'TONS_FRAG'].sum()
# print(dataGroup)

#creating a ColumnDataSource
datasource = ColumnDataSource(dataGroup) 

#creating plot
p = figure(x_axis_type ='datetime')

    #--->>> creat a color map
# cm = factor_cmap(field_name= 'COUNTRY_FLYING_MISSION', palette= Spectral5, factors= countries)

p.line(x= 'MSNDATE', y= 'TOTAL_TONS', source= datasource, color= 'blue', legend= 'کل انفجار', line_width= 2)
p.line(x= 'MSNDATE', y= 'TONS_IC', source= datasource, color= 'red', legend= 'حجم آتش', line_width= 2)
p.line(x= 'MSNDATE', y= 'TONS_HE', source= datasource, color= 'green', legend= 'انفجار قوی', line_width= 2)

# p.vbar(source= datasource, x='COUNTRY_FLYING_MISSION', top= 'TONS_HE', color= cm, width= 0.6)
# p.vbar_stack(source= datasource, x='COUNTRY_FLYING_MISSION', stackers= ['TONS_HE', 'TONS_IC', 'TONS_FRAG'], legend= ['اشتعال زا', 'انفجار قوی', 'قطعات'], color= Spectral3, width= 0.6)

#show the plot
show(p)
