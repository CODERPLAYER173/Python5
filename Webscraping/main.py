import bs4 as bs
import requests
import pandas as pd
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
a  = response.text
soup = bs.BeautifulSoup(a, "html.parser")
movie_list = [a.text for a in soup.find_all("h3", {"class": "title"})]
a =movie_list[::-1]
print(a)
pd.DataFrame(a).to_csv('movies.csv', index=False)