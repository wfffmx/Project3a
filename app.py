from flask import Flask, render_template, request, url_for, flash, redirect, abort
from ping import pingAPI
from RenderGraph import render_graph
from datetime import datetime
from SP500 import sp500_symbols

# make a Flask application object called app
app = Flask(__name__)
app.config["DEBUG"] = True

#flash the secret key to secure sessions
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/', methods=['GET', 'POST'])
def index():

    chart = None
    symbol = None
    chart_type = None
    time_series = None
    
    symbols = sp500_symbols()
    if request.method == 'POST':
        # Get user inputs from the form
        symbol = request.form['symbol']
        chart_type = request.form['chart_type']
        time_series = request.form['time_series']
        start_Date_str = request.form['lowerDate']
        end_Date_str = request.form['upperDate']

        processed_data = None 
        
        # Validate form data
        if symbol == "":
            flash("Symbol is required")
        elif chart_type == "":
            flash("Chart type is required")
        elif time_series == "":
            flash("Time Series is required")
        elif start_Date_str == "":
            flash("Enter Start date")
        elif end_Date_str == "":
            flash("Enter End date")
        else:
            if start_Date_str and end_Date_str:

                # Convert date strings to datetime objects
                start_Date = datetime.strptime(start_Date_str, '%Y-%m-%d')
                end_Date = datetime.strptime(end_Date_str, '%Y-%m-%d')
                


                if end_Date < start_Date:
                 flash("The end date cannot be before the start date")
                else:
            
                # If no error, query the api
                 processed_data = pingAPI(time_series, symbol, start_Date, end_Date) 

                if not processed_data:
                    flash("No data available for the selected range.")
                else:
                    # Calling the function that renders the graph
                  chart = render_graph(chart_type, start_Date_str, end_Date_str, processed_data, symbol)
              
    # Render the template with the chartdata, if any
    return render_template('stock.html', chart=chart, symbols=symbols)



# main driver function
if __name__ == '__main__':
 
# run() method of Flask class runs the application
 app.run(host="0.0.0.0")
