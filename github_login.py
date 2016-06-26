import requests
import urllib
from BeautifulSoup import BeautifulSoup

#Set proxies to null if not required
proxies = {'http':'127.0.0.1:8081','https':'127.0.0.1:8081'}
headers={"Connection": "keep-alive", "Accept": "*/*", "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0", "Accept-Encoding": "gzip", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "Proxy-Connection": "keep-alive"}


def getLoginSession():	
	#Login page https://github.com/login
	r_login = requests.get('https://github.com/login',headers=headers,proxies=proxies,verify=False)
	soup = BeautifulSoup(r_login.text);
	
	commit="Sign in"
	login="git Username"
	password="git password"

	#finding the authenticity token by scrapping
	inpuT = soup.findAll('input',{'name':'authenticity_token'})
	token = inpuT[0]['value']
	
	#finding the urf8 value
	inpuT = soup.findAll('input',{'name':'utf8'})	
	utF = inpuT[0]['value']
	
	params = {}

	#put the required name-value pair in dictionary params
	params['login'] = login;
	params['password'] = password;
	params['commit'] = commit;
	params['authenticity_token'] = urllib.unquote(token);
	params['utf8'] = utF;
	cookies = dict(r_login.cookies);
	
	try:
		#request to https://github.com/session to get the login sessions
		login_req = requests.post('https://github.com/session',data=params,cookies=cookies,headers=headers,proxies=proxies,verify=False);
		login_cookies = dict(login_req.cookies)

		return login_cookies;
	except Exception,e:
		print e;
		return False;


if __name__ == '__main__':
	pass;
