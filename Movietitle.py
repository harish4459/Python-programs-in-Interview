To solve this challenge, you are required to write an HTTP GET method to retrieve information from a movie database. Function Description Given a string substr, getMovieTitles must perform the following tasks:

Query https://jsonmock.hackerrank.com/api/movies/search/?Title=substr (replace substr).
Initialize the titles array to store total string elements. Store the Title of each movie meeting the search criterion in the titles array.
Sort titles in ascending order and return it as your answer. The query response from the website is a JSON response with the following five fields: page : The current page. per_page : The maximum number of results per page. total : The total number of movies in the search result. total_pages : The total number of pages which must be queried to get all the results. data : An array of JSON objects containing movie information where the Title field denotes the title of the movie. In order to get all results, you may have to make multiple page requests. To request a page by number, your query should read https://jsonmock.hackerrank.com/api/movies/search/? Title=substr&page=pageNumber , replacing substr and pageNumber.


Solution -

#!/bin/python3
import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json

# Complete the function below.
# Base url: https://jsonmock.hackerrank.com/api/movies/search/?Title=
import requests
import json

def  getMovieTitles(substr):
    Movietitles =[]
    connections = requests.get("https://jsonmock.hackerrank.com/api/movies/search/?Title={}".format(substr))
    response =json.loads(connections.content.decode('utf-8)'))
    for page in range(0, response["total_pages"]):
        page_response = requests.get("https://jsonmock.hackerrank.com/api/movies/search/?Title={}&page={}".format(substr, page+1))
        page_content =json.loads(page_response.content.decode('utf-8'))
        for item in range(0, len(page_content["data"])):
            Movietitles.append(str(page_content["data"][item]["Title"]))
    Movietitles.sort()
    return Movietitles
            
f = open(os.environ['OUTPUT_PATH'], 'w')
    

try:
    _substr = str(input())
except:
    _substr = None

res = getMovieTitles(_substr)
for res_cur in res:
    f.write( str(res_cur) + "\n" )

f.close()
