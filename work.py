


import os 
import imghdr 



base_image_folder =  "./content/media/images/"


def get_image(path):
	'''completes abnd returns the path to get images from the media folder '''
	return os.path.join(base_image_folder , path)

class tech:
	python = "Python"
	c = "c"
	javascript = "Javascript"
	jquery = "Jquery"
	django = "Django"
	bootstrap = " Bootstrap"
	html = "HTML"
	css = "CSS"
	sql = "SQL"
	kivy = "Kivy"
	pygame = "Pygame"
	selenium = "Selenium"
	bs4 = "Beautifulsoup"
	requests = "requests"

class ListItem:
	 
	def __init__(
		self ,
		title ,
		short_description, 
		long_description,
		redirect_url , 
		screenshots_folder , 
		technologies_used:list=[],
		banner = '' ):

		self.title = title
		self.short_description = short_description 
		self.long_description = long_description
		self.redirect_url = redirect_url
		self.banner = banner 
		self.screenshots_folder =  os.path.join(base_image_folder,screenshots_folder)
		self.screenshots = [] 
		self.technologies_used = technologies_used
		self.collect_media()
		self.id = title.strip().replace(" ", "_")
		if not self.banner and len(self.screenshots) > 0:
			self.banner = self.screenshots[0]


	def collect_media(self):
		print(f"Collecting media for project : {self.title} .... " , end = '')
		if not os.path.isdir(self.screenshots_folder):
			print(f"ERROR. Folder {self.screenshots_folder} not found ")
			return
		all_files = os.listdir(self.screenshots_folder)
		for file in os.listdir(self.screenshots_folder):
			file = os.path.join(self.screenshots_folder , file)
			is_image = imghdr.what(file) is not None 
			if not is_image:continue 
			self.screenshots.append( file )
		print(f" ....sorted {len(all_files)} , got {len(self.screenshots)} DONE ! ")


 
PROJECTS = [
		
	 
 ListItem(
			title = "Wholemail", 
			short_description = "An open source email template library built for easier generation and sending of generic emails", 
			long_description = "Useful for generic emails like password reset links ,  email verification and more",
			redirect_url = "https://github.com/victhepythonista/wholemail",
			screenshots_folder = "projects/wholemail/",
			banner = "",
			technologies_used = [tech.python , ]
			), 

 ListItem(
			title = "Crawlfish", 
			short_description = "A Python libary containing useful web scraping related functions ", 
			long_description = "I built it after picking functionalities I kept re-using across different web scraping scenarios",
			redirect_url = "https://github.com/victhepythonista/crawlfish",
			screenshots_folder = "projects/crawlfish/",
			banner = "",
			technologies_used = [tech.python , ]
			), 

 ListItem(
			title = "Mobile table tennis game", 
			short_description = "A table tennis game made using Kivy ,  a python UI library ", 
			long_description = "",
			redirect_url = "https://github.com/victhepythonista/TableTennis",
			screenshots_folder = "projects/android_table_tennis/",
			banner = "",
			technologies_used = [tech.python , tech.kivy ]
			), 

 ListItem(
			title = "Jarball", 
			short_description = "A 2D game where you cut a rope to drop a ball into a jar  ", 
			long_description = "",
			redirect_url = "https://github.com/victhepythonista/JarBall-1.0",
			screenshots_folder = "projects/jarball/",
			banner = "",
			technologies_used = [tech.python , tech.pygame ]
			), 
 ListItem(
			title = "Trex Game", 
			short_description = "A simple remake of the famous browser game", 
			long_description = "I used pygame to build it. I  used this project to learn how  animation frames are rendered in games ",
			redirect_url = "https://github.com/victhepythonista/trex-game-1.0",
			screenshots_folder = "projects/trex_game/",
			banner = "",
			technologies_used = [tech.python , tech.pygame ]
			), 
  ListItem(
			title = "Android calculator", 
			short_description = "A calculator app built using Kivy", 
			long_description = " ",
			redirect_url = "https://github.com/victhepythonista/Android_calculator_with_kivy",
			screenshots_folder = "projects/android_calculator",
			banner = "",
			technologies_used = [tech.python , tech.pygame ]
			), 
 ListItem(
			title = "Android stopwatch", 
			short_description = "A stopwatch app built using Kivy", 
			long_description = " ",
			redirect_url = "https://github.com/victhepythonista/Android-stopwatch/tree/main",
			screenshots_folder = "projects/kivy_stopwatch",
			banner = "",
			technologies_used = [tech.python , tech.pygame ]
			), 
]


FREELANCE_WORK = [
ListItem(
title = "Betmonitor bot", 
short_description = "A tool for scraping prematch sports info on betmonitor.com ", 
long_description = "This tool fetches prematch betting odds across the websites listend on betmonitor.com and stores it in CSV files for further analysis ",
redirect_url = "",
screenshots_folder = "work/bet_monitor/",
banner = "",
technologies_used = [tech.python , ]
), 
ListItem(
title = "Equiply website", 
short_description = "A construction equipment website ", 
long_description = "built on a network of web scrapers , this website provides the latest sales from different categories of construction equipment . The bots communicate with the server via a custom ecrypted API . Some of the bots are listed here on my website like Supplypostbot and Ironplnetbot ",
redirect_url = "",
screenshots_folder = "work/equiply/",
banner = "",
technologies_used = [
tech.python ,
tech.javascript,
tech.jquery,
tech.django ,
tech.html , 
tech.css ]

), 
ListItem(
title = "Ironplanet bot", 
short_description = "A bot that scrapes equipment product data from ironplanet.com", 
long_description = " The user prompts the bot with the equipment categories needed and the bot scrapes the data ",
redirect_url = "",
screenshots_folder = "work/ironplanet/",
banner = "",
technologies_used = [tech.python , tech.bs4 ,tech.requests ]

), 
ListItem(
title = "Amazon bot", 
short_description = "A bot that scrapes product data from the Amazon website", 
long_description = "A commandline based tool for scraping different categories of product data from the Amazon website and saves it in CSV files. To use it , save product category links in a text file and pass the file name to the bot and it'll do the rest.",
redirect_url = "",
screenshots_folder = "work/amazon/",
banner = "",
technologies_used = [tech.python , tech.bs4 ,tech.requests ]

), 
ListItem(
title = "Brutiful store bot", 
short_description = "A bot that scrapes data from brutiful store", 
long_description = "A command line tool for scraping data from brutifulstore.com. Since the website does client side rendering ,I had to use Selenium to come up with a flexible method for collecting data in any state of the page ",
redirect_url = "",
screenshots_folder = "work/brutiful_bot/",
banner = "",
technologies_used = [tech.python , tech.bs4 , tech.selenium]

), 
ListItem(
title = "Autotempest bot", 
short_description = "A bot that scrapes  car dealership and pricing data from Autotempest and saves it to csv files  ", 
long_description = "",
redirect_url = "",
screenshots_folder = "work/autotempest/",
banner = "",
technologies_used = [tech.python , tech.requests , tech.bs4 ]

), 
ListItem(
title = "Supplypost bot", 
short_description = "A bot that scrapes equipment data from the supplypost.com  website", 
long_description = "You provide the categories you want to scrape and it will proceeed to scrape the data and creates well structured folders for the CSV data files",
redirect_url = "",
screenshots_folder = "work/supplypost/",
banner = "",
technologies_used = [tech.python , tech.bs4 ,tech.requests]

), 
ListItem(
title = "Volvoused bot", 
short_description = "A command line based bot that scrapes equipment data from the the volvoused  website and saves it in CSV files", 
long_description = " ",
redirect_url = "",
screenshots_folder = "work/volvoused/",
banner = "",
technologies_used = [tech.python , tech.bs4 ,tech.requests]

), 
ListItem(
title = "Walmartbot", 
short_description = "A bot that scrapes product data from the Walmart website. ", 
long_description = "I had used Selenium in order to navigate the pages like a normal user and scrape the data using BS4 ",
redirect_url = "",
screenshots_folder = "work/walmart/",
banner = "",
technologies_used = [tech.python , tech.selenium , tech.bs4]

), 

ListItem(
title = "Facebook marketplace bot", 
short_description = "A bot that scrapes sales from Facebook marketplace.", 
long_description = "It uses selenium for category navigation and location selection , bs4 does the rest . To use it the user provides their facebook logins and product categories to scrape",
redirect_url = "",
screenshots_folder = "work/fb_mp_bot/",
banner = "",
technologies_used = [tech.python , tech.selenium , tech.bs4]

), 

ListItem(
title = "Catused", 
short_description = "A bot that scrapes equipment data from Catused website and saves it to CSV files . ", 
long_description = " ",
redirect_url = "",
screenshots_folder = "work/catused/",
banner = "",
technologies_used = [tech.python , tech.selenium , tech.bs4]

), 

]

# 1


# 