#!/usr/bin/python
# coding: UTF-8
#作者 蒋明
#作用 reg购买存款标
#pip install pywinauto
#P6 - Time Series Forecasting
#http://www.youtubecomtomp3.com/zh/YouTube-to-MP4.php
#日期 2016-12-16
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
#import win32gui
import os,io
from selenium.webdriver.support.ui import Select
#import win32con
import time,platform,sys, getopt,paramiko,random,re

#back=socket.socket
#socks.set_default_proxy(socks.SOCKS5, "127.0.0.1",1080)
#print(requests.get('http://ifconfig.me/ip').text)
global index1
import psycopg2
index1=10
def save(name,src):
	os.system("mkdir -p /"+name)
	f=io.open("/"+name+"/index.htm",mode="w",encoding="UTF-8")
	f.write(src)
	f.close()
def l(url):
	linkall=""
	e.get(url)
	time.sleep(5)
	for link in e.find_elements_by_xpath("//*[@id='main-layout-sidebar']/div/div[1]/ol/li/a"):
		linkall=linkall+link.get_attribute('href')+" "
	save(url.replace('https://classroom.udacity.com/',''),linkall)
	alllink=linkall.split()
	index1=0
	for link in e.find_elements_by_xpath("//*[@id='main-layout-sidebar']/div/div[1]/ol/li/a"):
		e.set_window_size(1024, 640)
		time.sleep(1)
		link.click()
		e.set_window_size(320,768)
		time.sleep(2)
		href=alllink[index1].replace('https://classroom.udacity.com/','')
		save(href,e.page_source.replace('video class="video__el" crossorigin="anonymous">','video class="video__el" controls controlsList="nodownload" autoplay="autoplay" crossorigin="anonymous">') )
		index1=index1+1
def o(url):
	lk=""
	e.get(url)
	time.sleep(2)
	print(e.title)
        if e.title==u"未找到页面 - Udacity":
		time.sleep(0)
	else:
		url=url.replace('https://classroom.udacity.com/','').replace("\n", "")
		save(url,e.page_source)
		for link in e.find_elements_by_xpath("//a[contains(@href, 'courses/ud')]"):
			href=link.get_attribute('href')
			lk=lk+href+" "
		for link in lk.split():
			l(link)
def login(root,passwd):
	url="https://auth.udacity.com/sign-in?next=https%3A%2F%2Fclassroom.udacity.com%2Fauthenticated"
	e.get(url)
	#e.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div[2]/div/div[1]/div/form/div/div[1]/input').send_keys(root)
	#e.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div[2]/div/div[1]/div/form/div/div[2]/input').send_keys(passwd)
	#e.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div[2]/div/div[1]/div/form/button').click()
	e.find_element_by_css_selector("#app > div > div.main-container--content--1CGTM > div > div > div > div.tabbed-pane--content--2o3OQ > div > div > form > div > div:nth-child(1) > input").send_keys(root)
	e.find_element_by_css_selector("#app > div > div.main-container--content--1CGTM > div > div > div > div.tabbed-pane--content--2o3OQ > div > div > form > div > div:nth-child(2) > input").send_keys(passwd)
	e.find_element_by_css_selector("#app > div > div.main-container--content--1CGTM > div > div > div > div.tabbed-pane--content--2o3OQ > div > div > form > button").click()

WIDTH = 320
HEIGHT = 640
PIXEL_RATIO = 3.0
UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'
mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
options = webdriver.ChromeOptions()
options.add_argument("--kiosk")
options.add_experimental_option('mobileEmulation', mobileEmulation)
e=webdriver.Chrome()
e.implicitly_wait(10)
login("qq21008037@iigogo.com","aa123456")
time.sleep(5)
for i in range(100,280):
	o("https://classroom.udacity.com/courses/ud"+str(i))