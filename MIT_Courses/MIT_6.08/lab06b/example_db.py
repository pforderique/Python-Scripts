import os
os.environ["BOKEH_RESOURCES"] = 'inline'

import sqlite3
import datetime
from bokeh.plotting import figure,show
#script is meant for local development and experimentation with bokeh
ht_db = 'example.db' #database has table called sensor_data with entries: time_ timestamp, user text, temperature real, pressure real
USERS = ["dog","cat"] # the two users in this database are users called "dog" and "cat"
now = datetime.datetime.now()
# conn = sqlite3.connect(ht_db)
# c = conn.cursor()

with sqlite3.connect(ht_db) as c:
    results = c.execute('''SELECT temperature, pressure, time_ FROM sensor_data WHERE user = ? ORDER by time_ ASC;''',(USERS[0],)).fetchall() 
    temp1 = []
    pressure1 = []
    time1 = []
    for tup in results:
        temp1.append(tup[0])
        pressure1.append(tup[1])
        time1.append(datetime.datetime.strptime(tup[2],'%Y-%m-%d %H:%M:%S.%f'))

    results = c.execute('''SELECT temperature, pressure, time_ FROM sensor_data WHERE user = ? ORDER by time_ ASC;''',(USERS[1],)).fetchall() 
    temp2 = []
    pressure2 = []
    time2 = []
    for tup in results:
        temp2.append(tup[0])
        pressure2.append(tup[1])
        time2.append(datetime.datetime.strptime(tup[2],'%Y-%m-%d %H:%M:%S.%f'))


#make sure the plots have titles, x labels, y labels and each user is a different color with legend annotation  
plot1 = figure(x_axis_type="datetime")
plot2 = figure(x_axis_type="datetime")

plot1.line(time1, temp1, line_color="orange", legend_label="dog")
plot1.line(time2, temp2, legend_label="cat")

plot2.line(time1, pressure1, line_color="orange", legend_label="dog") 
plot2.line(time2, pressure2, legend_label="cat")

#either show plot1 or plot2
show(plot1)
show(plot2)