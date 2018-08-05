################################################################################
# mysql
# CREATE TABLE dram_price (ID int NOT NULL AUTO_INCREMENT, high_daily FLOAT, low_daily FLOAT, avg_daily FLOAT NOT NULL, timestamp TIMESTAMP, PRIMARY KEY (ID));


################################################################################
# Crawler
import re
from urllib.request import urlopen
import ssl 


context = ssl._create_unverified_context()
url = 'https://www.trendforce.com/price'
# urlopen returns an object like "file object"
r = urlopen(url, context=context).read().decode('utf-8')

list_0 = re.findall(r'(?<=<td bgcolor="#FBF9F2" class="tab_tr_gray">).+(?=</td>)', r)
list_1 = re.findall(r'(?<=<td class="tab_tr_gray">).+(?=</td>)', r)

high_daily = list_0[0]
low_daily = list_1[0]
avg_daily = list_0[2]

from datetime import datetime

# print(f"INSERT INTO dram_price (high_daily, low_daily, avg_daily, timestamp) VALUES ({high_daily}, {low_daily}, {avg_daily}, {datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")

print("INSERT INTO dram_price (high_daily, low_daily, avg_daily, timestamp) VALUES ({}, {}, {}, {})".format(high_daily, low_daily, avg_daily, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))                
################################################################################
# Insert data to db 
from datetime import datetime
import mysql.connector

db = mysql.connector.connect(
          host="localhost",
            user="django",
              passwd="qazwsxEDC123**",
                db="stevensite_db"
                )

cur = db.cursor()

#cur.execute(f"INSERT INTO dram_price (high_daily, low_daily, avg_daily, timestamp) VALUES ({high_daily}, {low_daily}, {avg_daily}, {datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")


cur.execute("INSERT INTO dram_price (high_daily, low_daily, avg_daily, timestamp) VALUES ({}, {}, {}, '{}')".format(high_daily, low_daily, avg_daily, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

db.close()
