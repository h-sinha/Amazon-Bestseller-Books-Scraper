# Amazon Bestseller Books Scraper

This scraper scrapes details of bestsellers from [amazon.in](https://www.amazon.in/gp/bestsellers/books/)  and [amazon.com](https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/) and stores the details in a CSV file.

* [in_bestseller.py](https://github.com/h-sinha/Amazon-Bestseller-Books-Scraper/blob/master/in_bestseller.py) - Scrapes data from [amazon.in](https://www.amazon.in/gp/bestsellers/books/) 

* [com_bestseller_py](https://github.com/h-sinha/Amazon-Bestseller-Books-Scraper/blob/master/com_bestseller.py) - Scrapes data from [amazon.com](https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/)

### Prerequisites
* python 3
* Requests
* CSV
* BeautifulSoup 4

### Instructions for Running 

Run the script using 

```
python3 in_bestseller.py
```
The output will be stored in in_book.csv


```
python3 com_bestseller.py
```
The output will be stored in com_book.csv
