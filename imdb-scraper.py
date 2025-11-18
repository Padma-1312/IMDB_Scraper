from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def scrape_imdb_top250():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    url = "https://www.imdb.com/chart/top/"
    driver.get(url)

    time.sleep(3)  # allow page content to load

    movies = driver.find_elements(By.CLASS_NAME, "ipc-metadata-list-summary-item__tc")

    movie_data = []

    for movie in movies:
        try:
            title_element = movie.find_element(By.TAG_NAME, "a")
            title = title_element.text.strip()

            year_element = movie.find_element(By.CLASS_NAME, "sc-b189961a-8")
            year = year_element.text.strip().replace("(", "").replace(")", "")

            rating_element = movie.find_element(By.CLASS_NAME, "ipc-rating-star--rating")
            rating = rating_element.text.strip()

            movie_data.append({
                "Title": title,
                "Year": year,
                "Rating": rating
            })

        except Exception:
            continue

    driver.quit()

    # Store into CSV
    df = pd.DataFrame(movie_data)
    df.to_csv("imdb_top250_movies.csv", index=False)
    print("Scraping complete! File saved as imdb_top250_movies.csv")


if __name__ == "__main__":
    scrape_imdb_top250()
