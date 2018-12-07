import requests
import csv
from bs4 import BeautifulSoup
page_no = 1
file = open('com_book.csv', 'w')
writer = csv.writer(file)
data = ['Name', 'URL', 'Author', 'Price', 'Number of Ratings', 'AverageRating']
writer.writerow(data)
while page_no < 6:
    try:
        if page_no == 1:
            string = ''
        else:
            string = 'ref=zg_bs_pg_2?_encoding=UTF8&pg='+str(page_no)
        page_no += 1
        url = 'https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/'+string
        print ('Fetching data from ',url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html5lib')
        basicwrap = soup.find_all(class_='zg-item-immersion')
        for i in basicwrap:
            try:
                name = (i.find(class_='p13n-sc-truncate p13n-sc-line-clamp-1').get_text().strip())
            except:
                name = ('Not available')
            try:
                author = (i.find(class_='a-row a-size-small').get_text().strip())
            except:
                author = ('Not available')
            try:
                price = (i.find(class_='p13n-sc-price').get_text().strip())
            except:
                price = ('Not available')
            try:
                rate = ((i.find('a', attrs={'class': 'a-size-small a-link-normal'})).get_text().strip())
            except:
                rate = ('Not available')
            try:
                avg_rating = (i.find(class_='a-icon-alt').get_text().strip())
                if avg_rating[len(avg_rating) - 1] == 'Prime':
                    avg_rating[len(avg_rating) - 1] == 'Not available'
            except:
                avg_rating = ('Not available')
            try:
                book_url = ('https://www.amazon.com'+i.find(class_='a-link-normal')['href'])
            except:
                book_url = ('Not available')
            data = [name, book_url, author, price, rate, avg_rating]
            writer.writerow(data)
    except:
        break