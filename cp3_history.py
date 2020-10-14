import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.basketball-reference.com/players/p/paulch01.html', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# # 선택자를 사용하는 방법 (copy selector)
# soup.select('태그명')
# soup.select('.클래스명')
# soup.select('#아이디명')
#R
# soup.select('상위태그명 > 하위태그명 > 하위태그명')
# soup.select('상위태그명.클래스명 > 하위태그명.클래스명')
#
# # 태그와 속성값으로 찾는 방법
# soup.select('태그명[속성="값"]')
#
# # 한 개만 가져오고 싶은 경우
# soup.select_one('위와 동일')
#############################
season_data = soup.select('#per_game > tbody > tr')

season = []
pts = []
ast = []
reb = []

for years in range(len(season_data)):
    seas_tag = season_data[years].select_one('th > a')
    seas_year = seas_tag.text
    if '-' in seas_year:
        # print(seas_year)
        season.append(seas_tag.text)
        rate_tag = season_data[years].select('td')

        # print(type(rate_tag))
        for i in range(len(rate_tag)):
            if "ast_per_g" in str(rate_tag[i]):
                ast_per_g = rate_tag[i].text
                ast.append(ast_per_g)

            if "trb_per_g" in str(rate_tag[i]):
                trb_per_g = rate_tag[i].text
                reb.append(trb_per_g)

            if "pts_per_g" in str(rate_tag[i]):
                pts_per_g = rate_tag[i].text
                pts.append(pts_per_g)


for i in range(len(pts)):
    print(season[i], ":", pts[i], ast[i], reb[i])

    # print(rate_tag)