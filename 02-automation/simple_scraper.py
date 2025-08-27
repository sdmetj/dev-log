import requests
from bs4 import BeautifulSoup
import csv
import os

# 스크랩핑할 웹사이트 URL
URL = "https://en.wikipedia.org/wiki/Perry_Township,_Tippecanoe_County,_Indiana"

# CSV 파일명 설정
OUTPUT_CSV_FILE = "scraped_data.csv"

headers_for_request = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

csv_headers = ["페이지 제목", "단락 내용", "링크 텍스트", "링크 URL"] # CSV 헤더 (컬럼명)

def scrape_website(url):
    data_to_save = [] # 데이터를 저장할 리스트 (여기에 각 행을 딕셔너리로 저장할 것임)
    
    
    try:
        print(f"웹페이지를 가져오는 중: {url}")
        response = requests.get(url, headers=headers_for_request)
        
        if response.status_code == 200:
            print(" 웹페이지 가져오기 성공! ")
            soup = BeautifulSoup(response.text, 'html.parser')
            
            page_title = soup.title.string if soup.title else "제목 없음"
            
            # 단락과 링크 정보 추출
            paragraphs = [p.get_text(strip=True) for p in soup.find_all('p') if p.get_text(strip=True)]
            links_info = []
            for link in soup.find_all('a'):
                text = link.get_text(strip=True)
                href = link.get('href')
                if text and href: # 텍스트나 URL이 비어있지 않은 경우만 추가
                    links_info.append({"text": text, "url": href})
            
            # 데이터를 data_to_save 리스트에 추가 (각각의 행은 딕셔너리 형태로)
            # 여기서는 예시로 가장 첫 번째 단락과 가장 첫 번째 링크만 저장하도록 구성.
            # 필요한 경우 더 많은 단락이나 링크를 반복문으로 저장할 수 있음.    
            first_paragraph = paragraphs[0] if paragraphs else ""
            first_link_text = links_info[0]["text"] if links_info else ""
            first_link_url = links_info[0]["url"] if links_info else ""
            
            data_to_save.append({
                "페이지 제목": page_title,
                "단락 내용": first_paragraph[:500],
                "링크 텍스트": first_link_text,
                "링크 URL": first_link_url
            })
            
            # CSV 파일로 저장
            save_to_csv(data_to_save, csv_headers, OUTPUT_CSV_FILE)
            print(f"\n데이터가 '{OUTPUT_CSV_FILE}' 파일에 성공적으로 저장 되었습니다.")
        
        else:
            print(f"웹페이지를 가져오는 데 실패했습니다. 상태 코드: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"네트워크 오류 발생: {e}")
    except Exception as e:
        print(f"스크래핑 중 예상치 못한 오류 발생: {e}")

def save_to_csv(data, headers_to_write, filename):
    """
    제공된 데이터를 CSV 파일로 저장하는 함수.
    :param data: 저장할 데이터 리스트 (딕셔너리 형태로 각 행을 표현)
    :param headers: CSV 파일의 헤더 (컬럼명 리스트
    :param filename: 저장할 CSV 파일의 이름
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        # DictionaryWriter를 사용하여 딕셔너리 데이터를 CSV로 쉽게 작성
        writer = csv.DictWriter(csvfile, fieldnames=headers_to_write)
        
        writer.writeheader() # 헤더 쓰기
        writer.writerows(data) # 데이터 행들 쓰기
        
if __name__=="__main__":
    scrape_website(URL)