import requests 
from bs4 import BeautifulSoup # ai  라이브러리
import webbrowser #웹 브라우저 연결

def search_images(keyword, num_images):
    # 구글 이미지 검색 URL 설정
    url = f"https://www.google.com/search?q={keyword}&tbm=isch"

    # HTTP GET 요청
    response = requests.get(url)

    # HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 이미지 URL 추출
    image_urls = []
    for img in soup.find_all('img', limit=num_images):
        image_url = img['src']
        if not image_url.endswith('.gif'):  # GIF 이미지 제외
            image_urls.append(image_url)

    return image_urls

# 키워드와 이미지 개수를 입력하여 이미지 검색 수행
keyword = input("검색할 키워드 입력: ")
num_images = int(input("가져올 이미지 개수 입력: "))
image_urls = search_images(keyword, num_images)

# 이미지 URL을 크롬 새 창으로 열기
for url in image_urls:
    webbrowser.open_new_tab(url)
