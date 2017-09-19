#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cgi, cgitb
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#from credintials import user,pwd
import json
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import re


class Login(object):
	"""
	This class is for initiliazing driver path
	"""

	def __init__(self):
		self.base_url = 'https://twitter.com/search?l=&q=%23SwissRe&src=typd&lang=en'
		self.driver = webdriver.Chrome(executable_path=r"C:\Users\Mitesh Yadav\Downloads\chromedriver_win32\chromedriver.exe")
	#self.driver.get(self.base_url)
	#self.userbox = self.driver.find_element_by_id("signInUsername")
	#self.userbox.send_keys('mitesh@thinkanalytics.in')
	#self.pwdbox = self.driver.find_element_by_id("signInPassword")
	#self.pwdbox.send_keys('madarchod')
	#self.loginbtn = self.driver.find_element_by_id("signInBtn")
	#self.loginbtn.click()

	"""
	Function that is used to reload the page by scrolling down and extracting all source information and returning back.
	"""
	def get_twitter_data(self,url):
		
		
		self.driver.get(url)

		SCROLL_PAUSE_TIME = 0.5

		# Get scroll height
		last_height = self.driver.execute_script("return document.body.scrollHeight")
		i=0
		while True:
			# Scroll down to bottom
			i=i+1
			
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

			# Wait to load page
			time.sleep(SCROLL_PAUSE_TIME)

			# Calculate new scroll height and compare with last scroll height
			new_height = self.driver.execute_script("return document.body.scrollHeight")
			if new_height == last_height:
				break
			last_height = new_height
			
		return self.driver.page_source
				


def get_all_data(text):
	extract_post_func(text)
	extract_date_func(text)
	extract_comments_func(text)
	extract_neg_comments_func(text)
	extract_location_func(text)




def extract_location_func(html):
	
	soup = BeautifulSoup(html,'html.parser')
	#print soup.find_all(re.compile('<time class=\'date subtle small\' datetime="(.+?)">'))
	#print soup.find_all('span',attrs={'class' : 'authorLocation middle'})
	for item in soup.find_all('span',attrs={'class' : 'authorLocation middle'}):
		print item.text
		
		
	#re_com=re.findall(r'<span class=\'authorLocation\'>(.+?)</span>',text)
	#print re_com,len(re_com),'com'
	#return re_com
	
def extract_comments_func(html):
	
	soup = BeautifulSoup(html,'html.parser')
	#print soup.find_all(re.compile('< class=\'date subtle small\' datetime="(.+?)">'))
	print 'oyee'
	#print soup.find_all('p',attrs={'class' : 'pros mainText truncateThis wrapToggleStr'})
	for item in soup.find_all('div',attrs={'class' : 'cell top padTopMd'}):
		extracted=item.text.encode('utf-8')
		if 'Pros' in extracted:
			print 'Pros',extracted
		elif 'Cons' in extracted:
			print 'Cons',extracted
		else:
			print 'AdvToMgmt',extracted
		
		
	#re_com=re.findall(r'<p class=\' pros mainText truncateThis wrapToggleStr\'>(.+?)</p>',text)
	#print re_com,len(re_com),'com'
	#return re_com
	

	
	
			
		
def extract_tweet_func(html):

	soup = BeautifulSoup(html,'html.parser')
	#print soup.find_all(re.compile('<time class=\'date subtle small\' datetime="(.+?)">'))
	i=0
	for item in soup.find_all('div',attrs={'class' : 'js-tweet-text-container'}):
		i=i+1
		print item.text.encode('utf-8')
		
	print i,'length'
	#re_date=re.findall(r'time class=\'date subtle small\' datetime="(.+?)">',text)
	#print re_date,len(re_date),'wwwwww'
		

		
		

	
def main():
	login=Login()
	
	
	#url='https://twitter.com/search?l=&q=%23SwissRe&src=typd&lang=en'
	"""
	enter name to be searched on twitter for tweets
	"""
	name='dhoni'
	
	url="https://twitter.com/search?q="+name+"&src=typd&lang=en"
	
	html=login.get_twitter_data(url).encode('utf-8')
	html =re.sub(re.compile("<!--.*?-->",re.DOTALL),"",html)
	print html
	
	
	soup = BeautifulSoup(html,'html.parser')
	print soup.prettify().encode('utf-8'),'asasdsas'
	#get_all_data(html)

	
	extract_tweet_func(html)
	#get_all_data(html)
	#raw_input()
	
	#print soup.find_all('time',attrs={'class' : 'date subtle small'}),'plplp'
	#raw_input()
	#for item in soup.find_all('time',attrs={'class' : 'date subtle small'}):
	#	print item,'mmmm'
	#	raw_input()
	
	
if __name__ == '__main__':
	main()