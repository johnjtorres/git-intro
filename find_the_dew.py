import re
import time

import pandas as pd
from selenium import webdriver
import textmyself

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(
    "https://www.walmart.com/ip/Mtn-Dew-Zero-Sugar-Baja-Blast-Soda-12-fl-oz-12-count/389027397"
)
more_pickup_options_button = driver.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/section[1]/button"
)
more_pickup_options_button.click()
time.sleep(2)
product_fulfillment_table = driver.find_element_by_xpath(
    "/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/table"
)
store_data = []
try:
    for element in product_fulfillment_table.find_elements_by_xpath("tr"):
        store = {}
        for div in element.find_elements_by_xpath("td/div"):
            if "mile" in div.text.lower():
                store["distance"] = int(re.search(r"\d+", div.text).group())
            elif "stock" in div.text.lower():
                store["available"] = True if div.text == "In Stock" else False
            else:
                store["city"] = div.text
        try:
            address = element.find_element_by_class_name("pickup-address").text
        except:
            pass
        else:
            store["address"] = address
        if store:
            store_data.append(store)
except Exception as e:
    print(e)
finally:
    driver.close()

message = "WalMarts with Mt. Dew Baja Blast Zero in stock:\n"
for store in store_data:
    if store["available"]:
        message += f"{store['address']} ({store['distance']} miles)\n"

textmyself.textmyself(message)
# df = pd.DataFrame(store_data)
# df.to_csv("dew_data.csv", index=False)
