import requests
import plotly.graph_objects as go
import urllib
import webbrowser
import textwrap
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
    return link

paralist=list()

def getcontent(links,keywords,country,key):             

#This function stores all the paragraphs with relevent keywords to a .txt file. Automatically called after getlinks() function.
 
    for i in links:
        print(i)
        res=requests.get(i)
        s=soup(res.text,'html.parser')
        content=s.find_all('p')
        
        
        for j in content:
            #print(((j.text).lower()))
            for k in keywords:
                #print(k.lower())
                if k.lower() in (j.text).lower():
                    paralist.append(j.text)
    
    paralist1=list(dict.fromkeys(paralist))
    print(len(paralist1))
    if not open(country+key+".txt", 'w',encoding='utf-8'):
        open(country+key+".txt", 'w',encoding='utf-8')
    with open(country+key+".txt", 'a+',encoding='utf-8') as output:
        i=0
        for row in paralist1:
            i+=1
            r=textwrap.fill(row,200)
            output.write(str(i)+'. '+ r + '\n\n')
            print('\n')

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
check=['coronavirus','covid','covid-19','pandemic','exit plan']

if choice=='1':
    country=input('Enter the country: ')
    getstats(country)  
elif choice=='2':
    key=list(input('Enter keywords separated by ",": ').split(','))
    country=input("Enter the country: ")
    linklist=list()
    linklist.clear()
    for i in range(len(key)):  
        inp=key[i]+'+'+ country
        got=getlinks(inp)
        linklist.extend(got)
        getcontent(linklist,check,country,key[i])
        print('Finished Search.\n')
else:
    print('INVALID CHOICE!')
print('\nYour txt file has now been saved as "country-namecovid.txt"!')
