from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By, ByType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path="/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"
total_cookies_id = "cookies"
product_prefix = "product"
product_price_prefix = "productPrice"


def wait_for_element(by: ByType, value: str):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, value)))


def select_language():
    wait_for_element(By.XPATH, '//*[contains(text(), "English")]')
    driver.find_element(By.XPATH, '//*[contains(text(), "English")]').click()


def main():
    select_language()

    wait_for_element(By.ID, cookie_id)
    cookie = driver.find_element(By.ID, cookie_id)

    products_count = len(driver.find_elements(By.CLASS_NAME, product_prefix))

    while True:
        for i in range(100):
            cookie.click()

        cookies_count = driver.find_element(
            By.ID, total_cookies_id).text.split(" ")[0]
        cookies_count = int(cookies_count.replace(",", ""))

        for i in range(products_count - 1, -1, -1):
            product_price = driver.find_element(
                By.ID, product_price_prefix + str(i)
            ).text.replace(",", "")

            if not product_price:
                continue

            product_price = int(product_price)

            while cookies_count >= product_price:
                product = driver.find_element(By.ID, product_prefix + str(i))
                product.click()
                break


if __name__ == "__main__":
    main()
