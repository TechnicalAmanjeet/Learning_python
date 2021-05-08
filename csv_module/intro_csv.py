import csv

with open('Book1.csv') as csvfile:
  book=csv.reader(csvfile)
  for i in book:
    print(i)