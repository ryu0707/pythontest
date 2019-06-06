q = input("好きな歌手は誰ですか？:")

with open("test7.txt","w",encoding="utf-8") as f:
          f.write(q)
        

import csv

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("movie.csv","w",encoding="utf-8") as s:
    moviecsv = csv.writer(s,delimiter=",")
    for movie_list in movies:
        moviecsv.writerow(movie_list)
        
