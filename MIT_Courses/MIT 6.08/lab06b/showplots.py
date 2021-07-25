import sqlite3
import datetime
from bokeh.plotting import figure
from bokeh.embed import components
ht_db = '/var/jail/home/porderiq/lab06/lab06b.db' #assumes you have a lab06b dir in your home dir

USERS = ['porderiq', 'moncadaa'] #update

def request_handler(request):
    if request['method'] =="GET":
        temp1 = []
        pressure1 = []
        time1 = []

        temp2 = []
        pressure2 = []
        time2 = []

        with sqlite3.connect(ht_db) as c:
            results = c.execute('''SELECT temperature, pressure, time_ FROM sensor_data WHERE user = ? ORDER by time_ ASC;''',(USERS[0],)).fetchall() 
            for tup in results:
                temp1.append(tup[0])
                pressure1.append(tup[1])
                time1.append(datetime.datetime.strptime(tup[2],'%Y-%m-%d %H:%M:%S.%f'))

            results = c.execute('''SELECT temperature, pressure, time_ FROM sensor_data WHERE user = ? ORDER by time_ ASC;''',(USERS[1],)).fetchall() 
            for tup in results:
                temp2.append(tup[0])
                pressure2.append(tup[1])
                time2.append(datetime.datetime.strptime(tup[2],'%Y-%m-%d %H:%M:%S.%f'))

        plot1 = figure(x_axis_type="datetime")
        plot2 = figure(x_axis_type="datetime")

        plot1.line(time1, temp1, line_color="orange", legend_label=USERS[0])
        plot1.line(time2, temp2, legend_label=USERS[1])

        plot2.line(time1, pressure1, line_color="orange", legend_label=USERS[0]) 
        plot2.line(time2, pressure2, legend_label=USERS[1])

        script1, div1 = components(plot1)
        script2, div2 = components(plot2)

        return f'''<!DOCTYPE html>
                    <html> <script src="https://cdn.bokeh.org/bokeh/release/bokeh-2.3.0.min.js"></script>
                        <body>
                            {div1}
                            {div2}
                        </body>
                        {script1}
                        {script2}
                    </html>
                    '''
    else:
      return "invalid HTTP method for this url."