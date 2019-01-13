from bs4 import BeautifulSoup
import requests,sys

     # target = 'http://www.biqukan.com/1_1094/5403177.html'
     # req = requests.get(url = target)
     # html = req.text
     # bf = BeautifulSoup(html,'lxml')
     # texts = bf.find_all('div', id='content',class_= 'showtxt')
     # print(texts[0].text.replace('\xa0'*8,'\n\n'))
class downloader(object):
     def __init__(self):
         self.target ='https://asa.scitation.org/toc/jas/144/3'   #"http://www.biqukan.com/1_1094"
         self.server ='https://asa.scitation.org'                 #'http://www.biqukan.com'
         # self.names = []  # 存放作者名
         self.urls = []  # 存放作者链接
         self.nums = 0

     def get_download_url(self):

         su = ''
         f = open("/Users/peak/PycharmProjects/spider/exercise/jasa.txt")
         line = f.readline()
         while line:
             # print(line)
             su = su+ line
             line = f.readline()
         f.close()
         self.urls=su
         self.nums=len(su)


     def get_contents(self, target):
         req=requests.get(url= target)
         html=req.text
         bf=BeautifulSoup(html,'lxml')
         div=bf.find_all('div',class_='sub-section')
         # print(div[0].text)
         # 输出时间
         time=bf.find_all('div',class_='open-access')


         a_bf=BeautifulSoup(str(div[0]),'lxml')
         a=a_bf.find_all('span',class_='entryAuthor normal hlFld-ContribAuthor')

         #输出PDF
         # atl=a_bf.find_all('article',class_='card-cont')
         pdf =a_bf.find_all('a', class_='ref nowrap pdf show-pdf')
         # for w in pdf:
         #     print(self.server+w.get('href'))
         texts=''
         for each in a:
            b=each.find_all('a')
            for a in b:
                # print(a.string,server+a.get('href'),'JASA EXPRESS LETTERS',time[0].text[4:])
                texts=texts+a.string+self.server+a.get('href')+'JASA EXPRESS LETTERS'+time[0].text[4:]
         return texts




     def writer(self, text):
         # write_flag = True
         # with open(path, 'a', encoding='utf-8') as f:
         #     f.writelines(text)
         #     f.write('\n\n')
         with open("jasa11.txt", "w") as f:
             f.write(text)

if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('jasa开始下载：')
    for i in range(dl.nums):
        dl.writer('JASA', dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" % float(i / dl.nums) + '\r')
        sys.stdout.flush()
    print('JASA下载完成')