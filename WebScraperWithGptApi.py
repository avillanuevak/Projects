# Web scraper with the chat gpt api
import requests
from bs4 import *
from openai import OpenAI

ai = OpenAI(api_key = '')

url = ''
prompt = 'Get me info on ____'

def scrapeSite(url,prompt):
    response = requests.get(url)

    if response.status_code == 200:
        soup =  BeautifulSoup(response.content,'html.parser')

        text = soup.get_text(separator='\n', strip=True)

        print(text)

    else:
        print(f"Failed to retrive the website. Status code: {response}")
    
    searchSite(text, prompt)

def searchSite(website, prompt):
    print('generating...')
    completion = ai.chat.completions.create(
        model="",
        messages = [
            {"role": "system", "content": f"You are going to analyze a website's content"},
            {"role": "user", "content": f"This is the text content of a website"}
        ]
    )
    searchResult = completion.choices[0].message.content
    print(f'Search Results: {searchResult}')
    return (searchResult)

scrapeSite(url,prompt)

