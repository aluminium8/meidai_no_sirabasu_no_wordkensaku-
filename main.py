import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('http://syllabus.engg.nagoya-u.ac.jp/syllabus/')
time.sleep(5)
nendo=driver.find_element_by_name("n")
nendo_select=Select(nendo)
nendo_select.select_by_visible_text("２０２１年度")
#<input type="radio" name="k" value="wpX3izGdMLU=">
daigakuin=driver.find_elements_by_name('k')[1] #工学部のばあいは0, 工学研究科の場合は1
daigakuin.click()
kettei=driver.find_elements_by_xpath("//input[@type='submit']")[0]
print(kettei)
kettei.click()
sennkoutachi=driver.find_elements_by_partial_link_text("専攻")
links=[i.get_attribute("href") for i in sennkoutachi]
for a in sennkoutachi:
    print(a.get_attribute("href"))
    print(a.get_attribute("text"))
for a in links:
    driver.get(a)
    time.sleep(0.5)
    
    kamokutachi=driver.find_elements_by_partial_link_text("論")# "" と設定(空文字列)すると，全部のページを確認する
    
    time.sleep(0.1)
#    for b in kamokutachi:
        #print(b.get_attribute("href"))
        #print(b.get_attribute("text"))
    kamokulinks=[i.get_attribute("href") for i in kamokutachi]
    for b in kamokulinks:
        driver.get(b)
        time.sleep(0.1)
        target_str_num=driver.page_source.count('制御')
        #print(target_str_num)
        #kennsaku=driver.find_elements_by_xpath("//*[contains(text(), 'オンデマンド')]")
        #print(len(kennsaku))
        if(target_str_num!=0):
           # print(len(kennsaku))
            print(driver.find_elements_by_xpath("//*[contains(text(), '専攻')]")[1].text, end=': ')
            print(driver.find_elements_by_xpath("//h3[contains(text(), '')]")[0].text)
        driver.back()
        time.sleep(0.1)
    driver.back()
    time.sleep(0.1)

time.sleep(5)
driver.quit()