import numpy as np
import matplotlib.pyplot as plt
import csv

#Initializing empty lists
book_ids, years, prices, pages, genres = [], [], [], [], []

#Appending csv items to list
with open("book_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        book_ids.append(int(row["Book_ID"]))
        years.append(int(row["Year_Published"]))
        prices.append(float(row["Price"]))
        pages.append(int(row["Pages"]))
        genres.append(row["Genre"])

#Converting python list to numpy array
years = np.array(years)
prices = np.array(prices)
pages = np.array(pages)
book_ids = np.array(book_ids)
genres = np.array(genres)

#Line-plot of book trends over the years
plt.plot(years, prices, marker='o', linestyle='-')
plt.xlabel("Year Published")
plt.ylabel("Book Price")
plt.title("Line Plot: Book Price Over Years")
plt.show()

#Bar-plot of no of books per genre
unique_genres, counts = np.unique(genres, return_counts=True)
plt.bar(unique_genres, counts)
plt.xlabel("Genre")
plt.ylabel("Number of Books")
plt.title("Bar Chart: Books per Genre")
plt.show()

#Histogram- of distribution of book prices
plt.hist(prices, bins=6)
plt.xlabel("Book Price")
plt.ylabel("Frequency")
plt.title("Histogram: Book Price Distribution")
plt.show()

#Scatter-plot of page vs price
plt.scatter(pages, prices)
plt.xlabel("Number of Pages")
plt.ylabel("Book Price")
plt.title("Scatter Plot: Pages vs Price")
plt.show()

#Box-plot of price distribution of books
plt.boxplot(prices)
plt.ylabel("Book Price")
plt.title("Box Plot: Book Price Distribution")
plt.show()