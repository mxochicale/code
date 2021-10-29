import os
from bs4 import BeautifulSoup
import requests
import json
import matplotlib.pyplot as plt

def get_list_of_title():
    """ Ask the user for a list of books, one per line. """
    print("Enter one book title per line.  End with an empty line.")
    books = []
    while True:
        title = input("Title: ")
        if title == "":
            break
        books.append(title)
    return books

# Get the GoodReads API key from the environment
key = os.environ.get("GOODREADS_API_KEY")
    print("Please exit")
    sys.exit(1)

def scrape_goodreads(title) :
    """ Get the average rating for each book from GoodReads, and return a list of floats"""
    ratings = []
    for title in titles:
        # Get the book's ID from GoodReads
        url = "https://www.goodreads.com/search/index.xml?key={}&q={}".format(key, title)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "xml")
        book_id = soup.find("best_book").id.text
    
    return ratings

def show_ratings(titles, ratings):
    """ Show the ratings in the bar chart"""
    plt.bar(titles, ratings)
    plt.xticks(range(len(titles)), titles, rotation=45)
    plt.show()

titles = get_list_of_title()
ratings = scrape_goodreads(titles)
show_ratings(titles, ratings)

