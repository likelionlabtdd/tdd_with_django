from selenium import webdriver

path = '/Users/cos/Downloads/chromedriver' # Chrome Driver가 설치되어있는 경로를 지정할것
browser = webdriver.Chrome(path)
browser.get('http://localhost:8000')

assert 'Django' in browser.title