from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome() # start the chrome driver
driver.implicitly_wait(1) # set an implicit wait time of 1 second
driver.maximize_window()

driver.get("https://www.google.com/?gl=us&hl=en&gws_rd=cr&pws=0") # US website
text_areas = driver.find_elements(By.TAG_NAME, "textarea")
len(text_areas)
titles = [x.get_attribute("title") for x in text_areas]

searchbar = text_areas[titles.index("Search")]
searchbar.clear() # clear any previously entered text
searchbar.send_keys("CatalystRPA")
searchbar.send_keys(Keys.ENTER)
driver.current_url

# there are many div elements on the page
div_elements = driver.find_elements(By.TAG_NAME, "div")
len(div_elements) # 1251

# retrieve the parent searchresult element
searchresults = driver.find_elements(By.XPATH, "//div[@id='search']")
len(searchresults) # 1
searchres = searchresults[0]

# check the first link of the results
allresults = searchres.find_elements(By.TAG_NAME, "a")
len(allresults) # 37
allresults[0].get_attribute('href') # 'https://www.catalystrpa.com/' this is the correct element, first search result
# however, this element is not clickable

all_links = searchres.find_elements(By.TAG_NAME, "h3")
len(all_links) # 12
all_links[0].click() # OK

driver.current_url # 'https://www.catalystrpa.com/'
# we could continue...


