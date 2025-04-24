import requests
from bs4 import BeautifulSoup

# 뉴스 URL을 크롤링하는 함수
def get_news_links():
    url = 'https://news.naver.com/main/ranking/popularDay.naver'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 클래스명 'list_title'로 뉴스 제목 찾기
    news_items = soup.find_all('a', class_='list_title')  # 'list_title'로 뉴스 제목을 찾습니다
    
    top_news = []
    for item in news_items:
        title = item.get_text(strip=True)  # 뉴스 제목
        link = item.get('href')  # 뉴스 링크
        top_news.append(f"{title}: https://n.news.naver.com{link}")
    
    return top_news

# 뉴스 제목과 링크 출력하기
def print_news():
    news = get_news_links()
    
    # 상위 20개 뉴스 출력
    print("Top 20 News Titles and Links:")
    for idx, item in enumerate(news[:20]):  # 상위 20개 뉴스만 출력
        print(f"{idx+1}. {item}")

# 실행
print_news()

