import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self,url):
        self.url=url
        self.html=None
        self.soup=None
    def fetch_page(self):
        response=requests.get(self.url)
        self.html=response.text
    def parse_page(self):
        self.soup=BeautifulSoup(self.html,"html.parser")
    def extract_data(self):
        results=[]
        for link in self.soup.find_all("a"):
            title=link.get_text(strip=True)
            href=link.get("href")
            if title and href:
                results.append((title,href))
        return results
    def display(self,data):
        for i, (title,link) in enumerate(data,1):
            print(f"{i}, {title}")
            print(f"    {link}")
    def run(self):
        self.fetch_page()
        self.parse_page()
        data=self.extract_data()
        self.display(data)
class ScraperApp:
    def start(self):
        url=input("Enter Website URL: ")
        scraper=WebScraper(url)
        scraper.run()

if __name__=="__main__":
    app=ScraperApp()
    app.start()