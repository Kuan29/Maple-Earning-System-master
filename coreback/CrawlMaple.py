import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options 


# def crawl_maple(charName):   
#     chrome_options = Options()
#     chrome_options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get(f'https://maplestory.nexon.com/N23Ranking/World/Total?c={charName}')
#     time.sleep(3) 
#     test = driver.find_element_by_css_selector(".search_com_chk a") 
#     print(test)
#     search_box = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[10]/td[2]/dl/dt/a')
#     print(search_box)
#     search_box.click()

def crawlMaple(charName): 
    href = ""
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver,10)
    driver.get(f'https://maplestory.nexon.com/N23Ranking/World/Pop?c={charName}')
    try:
        result = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[@class="search_com_chk"]/td[2]/dl/dt/a[@href]')))
        href = result.get_attribute("href") 
        rankurl = href.replace('?', '/Ranking?')
    except Exception:
        print(Exception)
    else:
        driver.get(rankurl)  
        
        # character_level = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="wrap"]/div[2]/div[1]/div[2]/dl[1]/dd')))
        # world_name = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="wrap"]/div[2]/div[1]/div[2]/dl[3]/dd')))
        # character_class = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="wrap"]/div[2]/div[1]/div[2]/dl[2]/dd'))) 
        # image = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="wrap"]/div[2]/div[1]/div[2]/div[2]/div/img[@src]')))
        # character_image = image.get_attribute('src')

        # result={'character_level': character_level.text, 'world_name': world_name.text, 'character_class': character_class.text, 'character_image': character_image}
        
        # print(result) 
        rank= {}
        for i in range(1,7,1):
            rankname = wait.until(EC.presence_of_element_located((By.XPATH,f'//*[@id="container"]/div[2]/div[2]/div/div/ul/li[{i}]/dl/dt'))) 
            rankresult = wait.until(EC.presence_of_element_located((By.XPATH,f'//*[@id="container"]/div[2]/div[2]/div/div/ul/li[{i}]/dl/dd[2]'))) 
            rank[rankname.text] = rankresult.text
        print(rank)


    

    
    