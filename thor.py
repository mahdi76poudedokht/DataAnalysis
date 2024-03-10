#data import
import pandas as pd

#visualization import
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

#creat output html file
output_file('thor.html')

data = pd.read_csv('thor_wwii.csv').sample(200)
datasource = ColumnDataSource(data)

#cerat a new plot with a title and axis labels
p = figure(title='جنگ جهانی دوم', x_axis_label='نیروی هوایی', y_axis_label='حجم مواد منفجره')

# add a circle renderer and circle size to the plot
p.circle(source = datasource, x = 'AC_ATTACKING', y = 'TOTAL_TONS',
fill_color = 'orange', fill_alpha = 0.6, line_color = 'blue', size = 'TONS_IC')

#creat HoverTools
h = HoverTool()
h.tooltips = [
    ('تاریخ حمله','@MSNDATE'),
    ('کشور اعزام کننده ','@COUNTRY_FLYING_MISSION'),
    ('نیروی هوایی', '@AIRCRAFT_NAME')
]
p.add_tools(h)

# show the results
show(p)