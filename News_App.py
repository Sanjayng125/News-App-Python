# URLs
import requests
import time
import api_key

top_headlines = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key.API_KEY}"
sports = f"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={api_key.API_KEY}"
business = f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={api_key.API_KEY}"
health = f"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={api_key.API_KEY}"
entertainment = f"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey={api_key.API_KEY}"
technology = f"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey={api_key.API_KEY}"
science = f"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey={api_key.API_KEY}"

def getNews(url, category_Name):
    print(category_Name.upper())
    try:
        req = requests.get(url)
        res = req.json()
        news = list(res["articles"])
        for i in range(0, len(news)):
            print(f"{i + 1}.{news[i]["title"]}")
            print(news[i]["description"])
            print("---------------------------------------------")
    except Exception as e:
        print()
def askCat():
    global query
    while True:
        try:
            user_input = int(input("1 - Top Headlines\n2 - Sports\n3 - Business\n4 - Health\n5 - Technology\n6 - Science\n7 - Entertainment\n8 - Search\n9 - Quit\nEnter news category:"))
            if user_input == 9:
                break
            elif user_input == 1:
                getNews(top_headlines, "Top Headlines:")
            elif user_input == 2:
                getNews(sports, "Sports:")
            elif user_input == 3:
                getNews(business, "Business:")
            elif user_input == 4:
                getNews(health, "Health:")
            elif user_input == 5:
                getNews(technology, "Technology:")
            elif user_input == 6:
                getNews(science, "Science:")
            elif user_input == 7:
                getNews(entertainment, "Entertainment:")
            elif user_input == 8:
                query = input("Search News:")
                if query == "":
                    search = f"https://newsapi.org/v2/everything?sortBy=publishedAt&pageSize=20&language=en&apiKey=f0373d8f9a8a4e3da31da0b274d21f96"
                else:
                    search = f"https://newsapi.org/v2/everything?sortBy=publishedAt&pageSize=20&language=en&q={query}&apiKey=f0373d8f9a8a4e3da31da0b274d21f96"
                getNews(search, "Search Results:")
            else:
                print("Invalid input!!")
        except Exception as e:
            print("Something went wrong!")
askCat()