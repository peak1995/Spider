from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
     # target ='https://asa.scitation.org/toc/jas/144/3'
     # server ='https://asa.scitation.org'
     # req=requests.get(url= target)
     # html=req.text
     # bf=BeautifulSoup(html,'lxml')
     # div = bf.find_all('section', class_='year-list list-unstyled volume-list')
     # a_bf=BeautifulSoup(str(div[0]),'lxml')
     # # a = a_bf.find_all('a',class_="title expander")
     # a = a_bf.find_all('a')
     # results=''
     # for each in a:
     #    if each.get('href').startswith ('https'):
     #        # print(each.get('href'))
     #        results=results+each.get('href')+'\n'
     # print(results)
     # with open("jasa.txt", "w") as f:
     #     f.write(results)
     su=''
     f = open("/Users/peak/PycharmProjects/spider/exercise/jasa.txt")
     line = f.readline()
     while line:
         # print(line)
         su=su+line
         line = f.readline()
     f.close()
     print(su)
     print (len(su))