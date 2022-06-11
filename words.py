import requests
from bs4 import BeautifulSoup

class Words:
    def __init__(self):
        pass

    def Words_Five(word_list=[]):
        url = "https://gist.github.com/cfreshman/a7b776506c73284511034e63af1017ee" # all possible official wordle words. It does not include gibberish words.
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        words = soup.find_all("tr")
        for data in words:
            word_list.append(data.text.rstrip().lstrip().upper())
        return word_list

    def Words_Six(word_list=[]):
        url = "https://www.thefreedictionary.com/6-letter-words.htm" # couldn't find bigger dataset.
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        word = soup.find('div', {'class': 'TCont'})
        word_li_fin = [word_list.append((word.text)[i:i + 6].upper()) for i in range(0, len(word.text), 6)]
        return word_list

    def Words_Four(word_list=[]):
        url = "https://www.thefreedictionary.com/4-letter-words.htm" #
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        word = soup.find('div', {'class': 'TCont'})
        word_li_fin = [word_list.append((word.text)[i:i + 4].upper()) for i in range(0, len(word.text), 4)]
        return word_list