#!/usr/bin/python
import mysql.connector
import json
from collections import Counter

def dictiter(d) :
    for k, v in d.iteritems():
        f.write("{},{}\n".format(k, v))

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  #passwd="yourpassword",
  database = "assignment"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM sample")

myresult = mycursor.fetchall()
source=[]
medium=[]
campaign=[]
agent=[]

f = open("report.csv","w")

for x in myresult:
    a=json.loads(x[2])
    #print(a["utmParams"])
    medium.append(a["utmParams"]["utmMedium"])
    source.append(a["utmParams"]["utmSource"])
    campaign.append(a["utmParams"]["utmCampaign"])
    agent.append(a["utmParams"]["userAgent"])
#print(medium)
d=Counter(medium)
f.write("utmMedium,user count\n")
dictiter(d)
#print(source)
d=Counter(source)
f.write("utmSource,user count\n")
dictiter(d)
#print(campaign)
d=Counter(campaign)
f.write("utmCampaign,user count\n")
dictiter(d)
#print(agent)
d=Counter(agent)
f.write("userAgent,user count\n")
dictiter(d)

f.close()
