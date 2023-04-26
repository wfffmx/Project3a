#Ping Function
#Ping's API and gather's information and brings it back 

#important packages to import
import requests
import csv
from datetime import datetime

#test dates: 2022-03-01 -> 2022-03-31

#func is an integer that will represent what type of function is being called
#symbol is a string for the stock symbol we are looking for
#lowerDateStr is the string for the start date
#upperDateStr is the string for end date

def pingAPI(func, symbol, lowerDate, upperDate):
    if(func == 1):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=30min&apikey=MUQCQXXUYY3U4KUE&datatype=csv".format(symbol)
    elif(func == 2):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey=MUQCQXXUYY3U4KUE&datatype=csv".format(symbol)
    elif(func == 3):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={}&apikey=MUQCQXXUYY3U4KUE&datatype=csv".format(symbol)
    elif(func == 4):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={}&apikey=MUQCQXXUYY3U4KUE&datatype=csv".format(symbol)


    #getting the info form the API and turns into a CSV file
    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=",")
        results = list(cr)

    data = [] 
    for row in results:
        if(row[0] == "timestamp"):
            continue
        if(func == 1):
            apiDate = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
        else:
            apiDate = datetime.strptime(row[0], "%Y-%m-%d")
        if(apiDate >= lowerDate and apiDate <= upperDate):
            data.append({
                'timestamp': row[0],
                '1. open': row[1],
                '2. high': row[2],
                '3. low': row[3],
                '4. close': row[4],
                '5. volume': row[5],
            })

    return data


#ignore this, just used for my own testing
# def main():
#     string1 = "2023-03-17 12:00:00"
#     string2 = "2023-03-22 12:00:00"
#     date1 = datetime.strptime(string1, "%Y-%m-%d %H:%M:%S")
#     date2 = datetime.strptime(string2, "%Y-%m-%d %H:%M:%S")
#     results = pingAPI(1, "IBM", date1, date2)

#     for result in results:
#         print(result)

# main()