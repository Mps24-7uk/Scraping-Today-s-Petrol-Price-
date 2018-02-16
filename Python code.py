from urllib.request import urlopen 
from bs4 import BeautifulSoup
import pandas as pd

page=urlopen("http://www.sify.com/finance/today-petrol-price/")
soup5=BeautifulSoup(page)

table=soup5.find_all("table")[0]

data=[[column.text for column in row.find_all('td') ] for row in table.find_all('tr')]

Current_Price=pd.DataFrame(data,columns=['Capital','Petrol Current Price(Per Lt)','Petrol Previous Price(Per Lt)','Change(Rs)']).iloc[1:,0:2]