import requests, bs4, re, sys, os

parser = bs4.BeautifulSoup

class younisxyz:

	def __init__(self):		self.ses = requests.Session()

		self.os = os.system

	

	def login(self):

		self.os("clear")

		self.coki = input(" cookie : ")

		try:

			self.nama = re.search('name="primary_first_name" value="(.*?)"',str(self.ses.get("https://m.facebook.com/settings/account/?name&refresh_on_back=1&refid=70",cookies={"cookie": self.coki}).text)).group(1)

			print("\033[1;37m Welcome\033[1;32m %s "%(self.nama))

			open(".cookie.txt","w").write(self.coki)

		except: exit("\033[1;31m> invalid\033[1;37m")

		self.yj_xyz()

		

	def yj_xyz(self):

		self.os("clear")

		try:

			self.cok = {"cookie": open(".cookie.txt","r").read()}

			self.nama = re.search('name="primary_first_name" value="(.*?)"',str(self.ses.get("https://m.facebook.com/settings/account/?name&refresh_on_back=1&refid=70",cookies=self.cok).text)).group(1)

		except: self.login()

		apa = input(f"\t \033[1;32m- YOUNIS-XYZ X {self.nama.upper()} -\n\n\033[1;90m[\033[1;33m1\033[1;90m] \033[1;37mDump Single Public\n\033[1;90m[\033[1;33m2\033[1;90m] \033[1;37mDump Multi Public ID\n\033[1;90m[\033[1;33m3\033[1;90m] \033[1;37mGrap separate links from file\n\033[1;90m[\033[1;33m4\033[1;90m] \033[1;37mCut duplicate links from file\n\033[1;90m[\033[1;33m5\033[1;90m] \033[1;31mLogout \033[1;90mdelete cookie\033[1;37m\n> Choose : ")

		print("-"*30)

		if apa in ["1","01"]:

			akun = input("[?] target : ")

			self.file = input("\033[1;35m> johnxyz.txt \033[0;97m\n> Put path to save file : ")

			if "https" in str(akun): self.user = akun.split("/")[3]

			else: self.user = akun

			self.cek_target()

			self.info_file()

			self.dump_publik(f"https://mbasic.facebook.com/{self.user}/friends")	

		elif apa in ["2","02"]:

			xx = int(input("> how many ids you want to add? : "))

			self.file = input("\033[1;35m> johnxyz.txt \033[0;97m\n> Put path to save file : ")

			self.info_file()

			for x in range(xx):

				akun = input("[?] target : ")

				if "https" in str(akun): self.user = akun.split("/")[3]

				else: self.user = akun

				self.cek_target()

				self.dump_publik(f"https://mbasic.facebook.com/{self.user}/friends")

		elif apa in ["5","05"]: self.os("rm -rf .cookie.txt"); exit()

		else: exit()

	

	def info_file(self):

		print(f"> save in : /sdcard/{self.file}.txt")

		

	def info_file(self):

		print(f"> save in : /sdcard/{self.file}.txt")

		

	def cek_target(self):

		try:

			link = self.ses.get(f"https://mbasic.facebook.com/{self.user}/friends", cookies=self.cok).text

			if "No Friends To Show" in link:

				exit("[!] friend list not published")

			elif "The page you requested was not found." in link:

				exit(f"[!] user with id {self.user} not found")

			elif "You Cannot Use This Feature Now" in link:

				exit("[!] facebook limits every activity, limit bro, please switch accounts")

			elif "Content Not Found" in link:

				exit(f"[!] User With Id {self.user} not found")

			else: pass

		except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):

			exit("\033[1;90m[\033[1;31m!\033[1;90m] \033[1;31mconnection error\033[1;37m")

	

	

	def dump_publik(self, url):	

		try:

			link = self.ses.get(url, headers={"Host": "mbasic.facebook.com", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "accept-encoding": "gzip, deflate", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "cache-control": "max-age=0", "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="106"', "sec-ch-ua-mobile": "?0", "sec-ch-ua-model": "", "ch-ua-platform": '"Android"', "sec-fetch-dest": "document", "sec-fetch-mode": "navigate", "sec-fetch-site": "none", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36 OPR/72.4.3767.69265", "cookie": self.cok["cookie"]}).text

			data = re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',link)

			for user in data:

				if "profile.php?" in user[0]:

					mentah = re.findall("id\=(.*?)\&",user[0])[0]+"|"+user[1]

					open(f"/sdcard/{self.file}.txt","a").write(str(mentah)+"\n")

					xxx = open(f"/sdcard/{self.file}.txt","r").read().splitlines()

					print(f'\r[!] {len(xxx)} - %s        '%(user[1]),end=" ")

				else:

					mentah = re.findall("\/(.*?)\?eav",user[0])[0]+"|"+user[1]

					open(f"/sdcard/{self.file}.txt","a").write(str(mentah)+"\n")

					xxx = open(f"/sdcard/{self.file}.txt","r").read().splitlines()

					print(f'\r[!] {len(xxx)} - %s        '%(user[1]),end=" ")

				sys.stdout.flush()

			if "See More Friends" in link:

				self.dump_publik("https://mbasic.facebook.com"+parser(link, "html.parser").find("a", string="Lihat Teman Lain").get("href"))

		except Exception as e: print(e)

		

younisxyz().yj_xyz()		
