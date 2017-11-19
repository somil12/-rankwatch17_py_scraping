import urllib2
from bs4 import BeautifulSoup
import csv

def check_redirection(url):
    req = urllib2.Request(url=url)
    resp = urllib2.urlopen(req, timeout=3)
    redirected = resp.geturl() != url # redirected will be a boolean True/False
    return redirected

regions = ["american","arabic","australian","christian","english","french","german","indian"]

genders = ["boy","girl"]

letters = list("abcdefghijklmnopqrstuvwxyz")

url = "https://www.babynamesdirect.com/baby-names"

with open("names.csv", "wb") as csvfile:
    spamwriter = csv.writer(csvfile1, delimiter=',')
    spamwriter.writerow(["name","gender"])

def get_names(url,gender):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    all_li=soup.find_all('li', class_='ntr')
    for i in all_li:
        if(i.dl):
            if(i.dl.dt):
                if(i.dl.dt.b):
                    if(i.dl.dt.b.a):
                        with open("names.csv", "a") as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=',')
                            spamwriter.writerow([i.dl.dt.b.text, gender])

for region in regions:
    url_now = url + "/" + region
    for gender in genders:
        url_now_2 = url_now + "/" + gender
        for letter in letters:
            url_now_1 = url_now_2 + "/" + letter
            get_names(url_now_1, gender)
            print url_now_1
            const = 2
            url_number = url_now_1 + "/" + str(const)
            while(not(check_redirection(url_number))):
                get_names(url_number, gender)
                print url_number
                const = const + 1
                url_number = url_now_1 + "/" + str(const)
