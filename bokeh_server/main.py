#mahdi poudeh
#bokeh server

#import bokeh visoalization
from random import random
from bokeh.layouts import column
from bokeh.models import Button
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc

#creat pure plot
p = figure(x_range= (0, 100), y_range= (0, 100))
result = p.text(x= [], y= [], text= [], text_color= [])
dataSource = result.data_source

#creat a Button
button = Button(label= 'Submit')

#creat clickon function for bild data in plot from pure plot
i = 0
def clickOnSubmit():
    global i
    new_data = dict()
    new_data['x'] = dataSource.data['x'] + [random() * 70 + 15]
    new_data['y'] = dataSource.data['y'] + [random() * 70 + 15]
    new_data['text_color'] = dataSource.data['text_color'] + [RdYlBu3[i%3]]
    new_data['text'] = dataSource.data['text'] + [str(random())]
    print(new_data)
    print('i: ' + str(i))
    dataSource.data = new_data
    i = i + 1

#run function after per click
button.on_click(clickOnSubmit)

#Show data
curdoc().add_root(column(button, p))


