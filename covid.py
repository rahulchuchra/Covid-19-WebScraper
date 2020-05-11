import requests
import plotly.graph_objects as go
import urllib
import webbrowser
from bs4 import BeautifulSoup as soup
#country='japan'
#key=['pandemic','covid plan']

def getlinks(inp): 
    
    #This function searches the internet with keywords.
    
    print('Searching...\n------------------------------')
    base='https://www.bing.com/search?q='+inp                 #I HAD TO USE Bing BECAUSE IT WASN'T WORKING WITH Google OR DuckDuckGo
    #base=urllib.parse.urljoin('https://www.bing.com/search?q=',inp)
    print(base)
    r=requests.get(base)
    head=list()
    #head.clear()
    des=list()
    #des.clear()
    index=list()
    #index.clear()
    tuplist=list()
    link=list()
    #link.clear()
    
    c=0
    
    s=soup(r.text,"html.parser")
    result=s.find_all('li',class_='b_algo')
    for i in result:
        if(i.find('p')):
            c+=1
            info=i.find('p')
            index.append(c)
            txt=i.find('a',href=True)
        
       # tuplist.append((txt.text,info.text,txt['href']))
            des.append(info.text)
            head.append(txt.text)
            link.append(txt['href'])
    
    headers=['S.No.','Heading','Description']
    fig = go.Figure(data=[go.Table(columnwidth=[20,80,120],header=dict(values=headers),
                 cells=dict(values=[index,head,des]))
                     ])
    fig.show()
    print('LINKS:-\n--------------------')
    for i in range(len(link)):
        print(str(index[i])+'.',link[i])
    print('---------------------')

def getstats(country): 
    
    #This function gives us the live updates about the number of active,recovered,total and death cases.
    
    base="https://www.worldometers.info/coronavirus/country/"
    geturl=urllib.parse.urljoin(base,country)
    r=requests.get(geturl)
    text=r.text
    #print(text)
    lst=list()
    lst.clear()
    s=soup(text,"html.parser")
    cases=s.find_all(class_="maincounter-number")
    for i in cases:
        lst.append(i.find('span').find(text=True))
    lst.append(s.find(class_='number-table-main').find(text=True))
    total=lst[0]
    death=lst[1]
    recovered=lst[2]
    active=lst[3]
    print('Total Cases:',total)
    print('Active Cases:',active)
    print('Dead:',death)
    print('Recovered:',recovered)
print('Press 1 for stats.\nPress 2 for Keyword search.')
choice=input()
if choice=='1':
    country=input('Enter the country: ')
    getstats(country)  
elif choice=='2':
    key=list(input('Enter keywords separated by ",": ').split(','))
    country=input("Enter the country: ")
    for i in range(len(key)):
        
        inp=key[i]+'+'+ country
        getlinks(inp)
        print('Finished Search.\n')
else:
    print('INVALID CHOICE!')
