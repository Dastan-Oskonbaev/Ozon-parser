import time

import undetected_chromedriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def get_ozon_product_prices(product_url: str):
    if product_url[0:28] == 'https://www.ozon.ru/product/' and len(product_url) > 28:
        driver = undetected_chromedriver.Chrome()

        try:
            driver.get(product_url)
            time.sleep(10)

            prices_info = ''

            price_element = driver.find_element(By.XPATH, "//span[contains(@class, 'lo8') and contains(@class, 'l8o')]")
            price = price_element.text
            if price != '':
                prices_info += f'Актуальная цена: {price}\n'
            else:
                prices_info = 'Нет информации о цене или товара нет в наличии.'

            try:
                price_not_sale = driver.find_element(By.XPATH,
                                                     "//span[contains(@class, 'ol7') and contains(@class, 'ol8')]")
                not_sale = price_not_sale.text
                prices_info += f'Старая цена: {not_sale}\n'
            except NoSuchElementException:
                pass

            try:
                ozon_price = driver.find_element(By.XPATH, "//span[contains(@class, 'l3o') and contains(@class, 'ol1')]")
                price_ozon = ozon_price.text
                prices_info += f'Цена с картой Ozon: {price_ozon}'
            except NoSuchElementException:
                pass

            return prices_info

        except Exception as ex:
            print(ex)

        finally:
            driver.close()
            driver.quit()

    else:
        return 'Введите правильную ссылку товара.'
