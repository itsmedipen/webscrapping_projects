from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

website = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
driver = webdriver.Chrome()
driver.get(website)
time.sleep(5)

title =driver.find_element(By.ID,"Sovereign_states_and_dependencies_by_population")
print(title.text)

time.sleep(5)

# tables = driver.find_elements(By.XPATH,'//table[@class="wikitable sortable sticky-header sort-under mw-datatable col2left col6left jquery-tablesorter"]/tbody/tr')

# # for table in tables:
# #     print(table.text)

countries = []
Populations = []
percenta_of_worlds = []
Dates = []
Sources = []



country = driver.find_elements(By.XPATH,'//table[@class="wikitable sortable sticky-header sort-under mw-datatable col2left col6left jquery-tablesorter"]/tbody/tr/td[2]')
Population = driver.find_elements(By.XPATH,'//table[@class="wikitable sortable sticky-header sort-under mw-datatable col2left col6left jquery-tablesorter"]/tbody/tr/td[3]')
percenta_of_world = driver.find_elements(By.XPATH,'//table[@class="wikitable sortable sticky-header sort-under mw-datatable col2left col6left jquery-tablesorter"]/tbody/tr/td[4]')
Date = driver.find_elements(By.XPATH,'//table[@class="wikitable sortable sticky-header sort-under mw-datatable col2left col6left jquery-tablesorter"]/tbody/tr/td[5]')
Source= driver.find_elements(By.XPATH,'//table[@class="wikitable sortable sticky-header sort-under mw-datatable col2left col6left jquery-tablesorter"]/tbody/tr/td[6]')

for con in country:
    countries.append(con.text)
for pop in Population:
    Populations.append(pop.text)
for percentage in percenta_of_world:
    percenta_of_worlds.append(percentage.text)
for date in Date:
    Dates.append(date.text)
for source in Source:
    Sources.append(source.text)
time.sleep(5)
print(con.text)

#creating daata frame

df = pd.DataFrame({'Countries':countries,'Populations':Populations,'% of world': percenta_of_worlds,'Date':Dates,'Source':Sources})
df.to_csv('CountrywisePopulation.csv',index=False)
print(df)


# tables = driver.find_element(By.XPATH,'//th[@//tbody/tr]')

# print(tables.text)

driver.quit()

