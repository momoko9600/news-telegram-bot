import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

NAVER_URL = "https://news.naver.com/main/ranking/popularDay.naver"

def get_news():
    print("📥 뉴스 불러오는 중...")
    res = requests.get(NAVER_URL)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')

    articles = soup.select('.rankingnews_box .list_title')
    titles_and_links = [(a.text.strip(), a['href']) for a in articles]
    print(f"✅ {len(titles_and_links)}개의 뉴스 가져옴")
    return titles_and_links

def send_telegram_message(message):
    print("📤 텔레그램 전송 중...")
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, data=payload)
    print(f"✅ 텔레그램 응답: {response.status_code}, {response.text}")

def main():
    news = get_news()
    if not news:
        send_telegram_message("❗️오늘의 뉴스를 불러오지 못했습니다.")
        return

    top_20 = news[:20]
    bottom_20 = news[-20:]

    msg = "<b>📰 Top 20 뉴스</b>\n"
    for title, link in top_20:
        msg += f"• <a href=\"{link}\">{title}</a>\n"

    msg += "\n<b>📉 Bottom 20 뉴스</b>\n"
    for title, link in bottom_20:
        msg += f"• <a href=\"{link}\">{title}</a>\n"

    send_telegram_message(msg)

if __name__ == "__main__":
    main()
