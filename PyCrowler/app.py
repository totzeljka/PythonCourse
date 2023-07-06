import requests
from bs4 import BeautifulSoup


# u treminalu prvo instalirati
# pipenv install beautifulsoup4
# pipenv install requests
# instalirati pylint

responce = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(responce.text, "html.parser")

questions = soup.select(".question-summary")
for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    print(question. select_one(".vote-count-post").getText())
