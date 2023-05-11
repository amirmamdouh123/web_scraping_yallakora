import requests
from bs4 import BeautifulSoup
import csv

x=input('Please Enter date : (in Format YYYY-MM-DD)')


page= requests.get(f"https://www.yallakora.com/Match-Center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={2022-11-23}")

def main(page):
    src =page.content
    soup=BeautifulSoup(src,'lxml')#da kol al web page , 3aizin na5od mnha div mo3ian
    champianships = soup.find_all("div",{'class':'matchCard'}) #btgiblk kol al champians fe list
    def get_match_info(champianships):        #find htrg3lk al h2 kamla w goaha altext w 7walih spaces
        dic_champias={}
        for champianship in champianships:
            dic_matches={}
            chamipanship_title = champianship.contents[1].find("h2").text.strip() #contents de btrg3 kol children klist
            Matches=champianship.contents[3].find_all('li',{'class':'item'})
            for i,Match in enumerate(Matches):
                dic_match={}
                dic_match['team1']=Match.find("div",{"class":"teamCntnr"}).find("div",{'class':'teamA'}).find('p').text.strip()
                dic_match['team2']=Match.find("div",{"class":"teamCntnr"}).find("div",{'class':'teamB'}).find('p').text.strip()
                dic_match['time']=Match.find("span",{"class":"time"}).text.strip()
                (score1,score2)=Match.find_all('span',{'class':'score'})
                dic_match['score']=(score1.text,score2.text)
                dic_matches[f'match{i+1}']=dic_match
            dic_champias[chamipanship_title]=dic_matches
        return dic_champias 
     #awel btolla kas al3allam
    return get_match_info(champianships)
print(main(page))

