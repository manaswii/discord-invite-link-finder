import urllib.request
import ast
import json
url = 'https://discord.com/api/v6/invites/programming?with_counts=true'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,}
request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read() # The data u need
mydata = json.loads(data.decode('utf-8'))
for x in mydata:
    print(x)
print("-----------")
print(mydata['guild']['name'])
print(mydata['approximate_member_count'])
#print(mydata['name'])