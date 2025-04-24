import requests
from bs4 import BeautifulSoup

# 네이버 많이 본 뉴스 URL (정치/경제/사회 섹션 예시)
url = "https://news.naver.com/main/ranking/popularDay.naver"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 기사 정보 추출
articles = soup.select(".rankingnews_box a")[:20]

print("📈 많이 본 뉴스 Top 20")
for idx, article in enumerate(articles, start=1):
    title = article.text.strip()
    link = article["href"]
    print(f"{idx}. {title}")
    print(f"   👉 {link}")
