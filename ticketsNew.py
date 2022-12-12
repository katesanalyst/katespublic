

from requests_html import HTMLSession
import json
import sys
import pandas as pd

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


def main():
    #Provide an URL for the Movie
    url = 'https://www.ticketnew.com/Avatar-The-Way-of-Water-Movie-Tickets-Online-Show-Timings/Online-Advance-Booking/26192/C/Chennai'
    resp = session.get(url)

    # It extract data of the movie.
    for idx,txx in enumerate(resp.html.find('div[class="tn-entity tn-block tn-entity-and-timing-details"]')):
        print(idx,txx.find('div.tn-entity-details h5',first=True).text)
        for idx,txx in enumerate(txx.find('div.tn-timing-details ul li a')):
            # print(txx.attrs)
            venuen = str(txx.attrs['data-venuen']),
            screen = txx.attrs['data-screenn'],
            date = txx.attrs['data-date'],
            time = txx.text

            for tDetails in (json.loads(txx.attrs['data-tkts'])):
                showdetails = {'venue': venuen[0], 'screen': screen[0], 'date': date[0], 'time':time,
                'Name': tDetails['Name'],'price' :tDetails['Rate'],
                'total': tDetails['Total'],'Avail': tDetails['Avail'],
                'filled': (tDetails['Total'] -tDetails['Avail'])};#print(showdetails)
                showsData.append(showdetails)

if __name__ == '__main__':
    session = HTMLSession()
    showsData = []
    main()

    #create an separate function for Data optimise along with Pandas...
    datax = pd.DataFrame(showsData)
    datax['fillPrice'] = (datax['filled'] * datax['price'])
    datax['AvailPrice'] = (datax['Avail'] * datax['price'])
    datax['totalPrice'] = (datax['total'] * datax['price'])

    # Details of Film about Shows Business.
    # print(datax)

    # GroupBY
    print(datax.groupby(['venue','screen']).sum())

    #Total of Film shows cost...
    print(f" Advance Booking: {round(datax['fillPrice'].sum(),2)},{round(datax['totalPrice'].sum(),2)}, Filled Percentage: {round(((datax['fillPrice'].sum()/ datax['totalPrice'].sum())*100),2)}")
    
