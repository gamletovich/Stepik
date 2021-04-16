"""
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.

Пример HTML файла:

<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">

Пример ответа:

mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru
"""
from lxml import html
import requests
from urllib.parse import urlparse

# Test N1
# http://pastebin.com/raw/2mie4QYa

"""
a.b.vc.ttepic.org
ftepic.org
mail.ru
neerc.ifmo.ru:1345
sasd.ifmo.ru:1345
stepic.org
www.gtu.edu.ge
www.mya.ru
www.ya.ru
"""

# Test N2
# http://pastebin.com/raw/hfMThaGb

"""
a.b.vc.ttepic-2.org
a.b.vc.ttepic.org
ftepic-2.org
ftepic.org
mail-2.ru
mail.ru
neerc.ifmo-2.ru:1345
neerc.ifmo.ru:1345
sas-_0123d.ifmo.ru:1345
sasd.ifmo-2.ru:1345
steeeeeeepic.org
stepic-2.org
stepic.org
www.gtu.edu-2.ge
www.gtu.edu.ge
www.masdaya.ru
www.mya-2.ru
www.ya-2.ru
www.ya.ru
zzz.last.test-1.stepic.org
zzz.last.test-2.stepic.org
"""

# Test N3
# http://pastebin.com/raw/7543p0ns

"""
adworker.ru
banner.rbc.ru
biztorg.ru
biztorg.ru:80
blogi.rbc.ru
cnews.ru
consensus.rbc.ru
conv.rbc.ru
credit.rbc.ru
data.rbc.ru
dict.rbc.ru
drinktime.ru
events.cnews.ru
export.rbc.ru
finolymp.ru
gift.cnews.ru
graph.rbc.ru
magazine.rbc.ru
map.rbc.ru
marketing.rbc.ru
memori.ru
otc-pif.rbc.ru
otc-stock.rbc.ru
pda.rbc.ru
pogoda.rbc.ru
portfolio.rbc.ru
quote-otc.rbc.ru
quote.ru
raiting.rbc.ru
rating.rbc.ru
realty.rbc.ru
redir.rbc.ru
rss.rbc.ru
seminar.rbc.ru
spb.rbc.ru
sport.rbc.ru
static.feed.rbc.ru
stock.rbc.ru
style.rbc.ru
ta.rbc.ru
tata.ru
top.rbc.ru
top100.rambler.ru
turbo.ru
tv.rbc.ru
ug.rbc.ru
ulov-umov.ru
videoarchive.rbc.ru
www.5ballov.ru
www.armd.ru
www.autonews.ru
www.biztorg.ru
www.cnews.ru
www.conf.rbc.ru
www.event.rbc.ru
www.iglobe.ru
www.informer.ru
www.ivd.ru
www.liveinternet.ru
www.m-2.ru
www.nashidengi.ru
www.pochta.ru
www.quote.ru
www.quoterate.ru
www.quotetotal.ru
www.rbc.ru
www.rbc.ua
www.rbcdaily.ru
www.rbcinfosystems.com
www.rbcnews.com
www.rbctv.ru
www.refunder.ru
www.salon.ru
www.seminar.rbc.ru
www.top.rbc.ru
www.turbo.ru
www.turist.ru
www.utro.ru
www.worldclass.ru
zoom.cnews.ru
"""

import urllib.parse as urllib
import requests
from lxml import html

url = input().rstrip()
page = requests.get(url)
tree = html.fromstring(page.text)
hrefs = tree.xpath('//a/@href')
url_set = set()
for link in hrefs:
    line = urllib.urlsplit(link)[1] if urllib.urlsplit(link)[1] else urllib.urlsplit(link)[2]
    if line[0].isalpha():
        url_set.add(line.split(':')[0]) if len(line.split(':')) > 1 else url_set.add(line)
[print(x) for x in sorted(url_set)]
