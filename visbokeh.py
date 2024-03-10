from bokeh.plotting import figure, output_file, show
output_file('visb.html')
  
x1 = [1, 2, 22, 54, 98, 47]
x2 = [87, 51, 65, 4, 21, 3]

p = figure()
p.line(x1, x2, color='red', legend='line')
p.circle(x1, x2, color='blue', legend='temp')

p.legend.click_policy='hide'

show(p)