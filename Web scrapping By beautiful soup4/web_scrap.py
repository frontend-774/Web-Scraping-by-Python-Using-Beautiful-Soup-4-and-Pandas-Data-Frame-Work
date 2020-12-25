import requests
import pandas
import re
from bs4 import BeautifulSoup
i = 0
li=[]
while i < 50:
    r= requests.get("https://www.pakwheels.com/used-cars/search/-/mk_honda/ct_karachi/pr_1500000_More/?page="+str(i))
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    #print(soup.prettify())
    all = soup.find_all("div",{"class":"col-md-9 grid-style"})
    for item in all:
        #print("\n")
        data={}
        data["Price"]=item.find("div",{"class","price-details generic-dark-grey"}).text.replace("\n","").replace(" ","")
        data["Car Name"]=item.find("h3").text.replace("\n","").replace(" "," ")
        data["Car Kilometers "]=item.find("ul",{"class","list-unstyled search-vehicle-info-2 fs13"}).text.replace("\n"," ").replace(" "," ")
        try:
            data["Rating From Users"]=item.find("span",{"class","auction-rating"}).text
        except:
            data["Rating From Users"]=("Not given till yet")
        RealValue = item.find("button", {"class":"phone_number_btn"})['data-content']
        val = BeautifulSoup(RealValue, 'html.parser')
        data["Car owner Name"]=val.find("div",{"class":"primary-lang"}).text
        data["Car owner Number"]=val.find("h4").text
        data["Pak wheels"]=val.find("p",{"class":"fs12"}).text
        li.append(data)
        
        
    i=i+1
    

df = pandas.DataFrame(li)
df.to_excel("Output_web_scrap123.xlsx")
   