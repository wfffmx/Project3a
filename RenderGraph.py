import pygal

# creates and renders a graph to the browser
def render_graph(chart_type, start_date_str, end_date_str, data, stock_symbol):
   # print(f"Data received in render_graph: {data}")
    # empty arrays for organizing the data
    dates = []
    openData = []
    highData = []
    lowData = []
    closeData = []
    volumeData = []

    # organizing data
    for row in data:
        # skip the header
        print("Data:", data)
        if row.get("timestamp") == "timestamp":
            continue
        # adding the data from each row to their respective arrays
        dates.append(row["timestamp"])
        openData.append(float(row["1. open"]))
        highData.append(float(row["2. high"]))
        lowData.append(float(row["3. low"]))
        closeData.append(float(row["4. close"]))
        volumeData.append(float(row["5. volume"]))

    # making the graph
    if(chart_type == "1"):
        # graph type
        bar_chart = pygal.Bar(x_label_rotation=45) 
        # chart title
        bar_chart.title = 'Stock Data for ' + stock_symbol + ': ' + start_date_str + ' ' + end_date_str
        bar_chart.x_labels = dates
        # adding all of the fields
        bar_chart.add('Open', openData)
        bar_chart.add('High', highData)
        bar_chart.add('Low',  lowData)
        bar_chart.add('Close', closeData)
        # render to the browser
        # bar_chart.render_in_browser()

        chart = bar_chart.render_data_uri()

    else:
        # same thing as above but with a line graph
        line_chart = pygal.Line(x_label_rotation=45)
        line_chart.title = 'Stock Data for ' + stock_symbol + ': ' + start_date_str + ' to ' + end_date_str
        line_chart.x_labels = dates
        line_chart.add('Open', openData)
        line_chart.add('High', highData)
        line_chart.add('Low',  lowData)
        line_chart.add('Close', closeData)
        # line_chart.render_in_browser()
        chart = line_chart.render_data_uri()

    return chart