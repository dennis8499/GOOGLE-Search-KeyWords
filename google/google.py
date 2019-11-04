import urllib.request
import urllib.parse
import random
from time import sleep, strftime
from googlesearch import search
from bs4 import BeautifulSoup
import requests
import sys 
#**********************************
TittleList = []
UrlList = []
Keywords = []
#**********************************		
def create_Url_File():
	file = open('url.txt', 'w')    
	file.close() 	
	
def read_keyword():
	global Keywords
	keyword = open('keywords', 'r', encoding = 'utf-8')
	for lines in keyword.readlines():
		lines = lines.rstrip('\n')
		Keywords.append(lines)
	keyword.close()  
	createURL(Keywords) 
  
def createURL(Keywords):
	index = 'https://www.google.com.tw/search?q='
	length = len(Keywords)		
	for x in range(length):
		print (str(x) + ": " + Keywords[x] + '\n')		
		url = index + Keywords[x]	
		print ("********************************")
		print ("URL : " + str(url))
		print ("********************************")
		google_scrape(url, x)
		sleep(10)
		
def google_scrape(url, x):  
	global TittleList, UrlList
	try:	
		headers = requests.utils.default_headers()
		headers.update(
			{
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
			}	
		)
		response = requests.get(url, headers=headers)
		if response.status_code == requests.codes.ok:			
			response.encoding='utf-8'
			content = response.text			
			soup = BeautifulSoup(content, 'html.parser')	
			#LabelTittle = soup.find_all("h3", class_="r", limit = 20)			
			#LabelURL = soup.find_all("cite", class_="iUh30", limit = 20)			
			LabelTittle = soup.find_all("h3", class_="r")			
			LabelURL = soup.find_all("cite", class_="iUh30")	
			for a in LabelTittle:
				TittleList.append(a.text)
			for b in LabelURL:
				UrlList.append(b.text)
			RecordFile(TittleList, UrlList, x)		
	except Exception as e:		
		print (e)	
		
def searchInput(url):
	try:	
		headers = requests.utils.default_headers()
		headers.update(
			{
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
			}	
		)
		response = requests.get(url, headers=headers)
		if response.status_code == requests.codes.ok:			
			response.encoding='utf-8'
			content = response.text			
			soup = BeautifulSoup(content, 'html.parser')	
			inputClass = soup.find_all("input")			
			if not inputClass:
				print ("This web has not input")
				return False
			else:
				print ("This web has input")
				return True
	except Exception as e:		
		print (e)		
	
def RecordFile(TittleList, UrlList, x):
	global Keywords
	print ("Search: " + Keywords[x])
	file = open('url.txt', 'a', encoding = 'utf-8')
	file.write(Keywords[x] + '\n')
	for a, b in zip(TittleList, UrlList):
		recordFlag = searchInput(str(b))
		if (recordFlag == True):
			file.write(str(a) + '\n')
			file.write(str(b) + '\n')
	print (" ")
	print ("wait 10 seconds.")
	TittleList.clear()
	UrlList.clear()
	file.write("\n")
	file.flush()
	sleep(10)       
	print ("search next keyword." + '\n')	
	file.close() 
	
if __name__ == '__main__':
	create_Url_File()
	read_keyword()

     

