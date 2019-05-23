from selenium import webdriver
import time
import winsound

# define alert param
duration = 1000  # milliseconds
freq = 440  # Hz

# specify the url
urlpage = 'https://eticket.ktmb.com.my/guest/ticket/select?origin=37500&destination=37600&odate=20/06/2019&oth=NO&rdate=21/06/2019&rth=NI&adult=3&child=0&isreturn=1&pcode=undefined'
print(urlpage)

# # run firefox webdriver from executable path of your choice
# driver = webdriver.Firefox()

while(True):

    # get web page
    driver = webdriver.Firefox()
    # driver.set_window_position(-2000, 0)
    driver.get(urlpage)
    time.sleep(20)
    # execute script to scroll down the page
    driver.execute_script("document.getElementById('1').click();window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage")


    # find elements by xpath
    results = driver.find_elements_by_xpath('//*[@class="main_content"]')

    for result in results:
        print(result.text)
        if "21/06/2019 21:15" in result.text:
            print("FOUND!")
            while (True):
                winsound.Beep(freq, duration)
        else:
            print("NOPE :(")


    driver.quit()
    time.sleep(30)