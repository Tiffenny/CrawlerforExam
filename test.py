# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
res = requests.get('http://www.aiotestking.com/ec-council/which-of-the-following-commands-shows-you-the-names-of-all-open-shared-files-on-a-server-and-number-of-file-locks-on-each-file-3/')
soup = BeautifulSoup(res.text,'lxml')
i = 0
soup  = soup.findAll('div', attrs={'id':'content','class':'post_text'})[0]
content = soup.findAll('p')
ans = soup.findAll('font', attrs={'color':'#333333'})[0]
for i in content:
     print i.text
print 'ANS: %s'%(ans.text.strip())

