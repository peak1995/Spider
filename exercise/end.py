from bs4 import BeautifulSoup
import requests,sys


def get_contents(target):
    server = 'https://asa.scitation.org'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    div = bf.find_all('div', class_='sub-section')
    # print(div[0].text)
    # 输出时间
    time = bf.find_all('div', class_='open-access')

    a_bf = BeautifulSoup(str(div[0]), 'lxml')
    a = a_bf.find_all('span', class_='entryAuthor normal hlFld-ContribAuthor')

    # 输出PDF
    # atl=a_bf.find_all('article',class_='card-cont')
    # pdf = a_bf.find_all('a', class_='ref nowrap pdf show-pdf')
    # for w in pdf:
    #     print(self.server+w.get('href'))
    texts = ''
    for each in a:
        b = each.find_all('a')
        for a in b:
            # print(a.string,server+a.get('href'),'JASA EXPRESS LETTERS',time[0].text[4:])
            texts = texts + (
                        a.string + '|' + server + a.get('href') + '|' + 'JASA EXPRESS LETTERS' + '|' + time[0].text[
                                                                                                      4:]) + '\n'
            #   texts=texts+a.string+'\n'
    # print(texts)
    return (texts)
if __name__ == "__main__":
     su=[]
     f = open("/Users/peak/PycharmProjects/spider/exercise/jasa.txt")
     line = f.readline()
     while line:
         # print(line)
         # su=su+line
         su.append(line)
         line = f.readline()
     f.close()
     print(su)
     print (len(su))
     leng= 3  #len(su)
     target = su  #'https://asa.scitation.org/toc/jas/144/3'#

     # print(get_contents(su[1]))
     endresult=''
     # print(get_contents(target))

     with open("jasadata.txt", "w") as f:
         for i in range(leng):
             # print(get_contents(su[i]))
             # endresult=endresult+get_contents(su[i])+'\n'
              f.write(get_contents(su[i])+'\n')




