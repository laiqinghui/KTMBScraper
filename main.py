from selenium import webdriver
import time
#import winsound
import os

# define alert param
duration = 1000  # milliseconds
freq = 440  # Hz

# specify the url
urlpage = 'https://eticket.ktmb.com.my/guest/ticket/select?origin=37500&destination=37600&odate=22/06/2019&oth=NI&rdate=undefined&rth=MO&adult=6&child=0&isreturn=0&pcode=undefined'
#https://eticket.ktmb.com.my/guest/ticket/select?origin=37500&destination=37600&odate=20/06/2019&oth=NO&rdate=21/06/2019&rth=NI&adult=3&child=0&isreturn=1&pcode=undefined
print(urlpage)

timeoutCounter = 0

# # run firefox webdriver from executable path of your choice
# driver = webdriver.Firefox()

while(True):

    # get web page
    driver = webdriver.Firefox()
    driver.set_window_position(2000, 0)

    while(True):
        try:
            driver.get(urlpage)
            break
        except:
            timeoutCounter += 1
            print("Timeout occurred")
            print("Retrying after 5 seconds...")
            time.sleep(5)


    time.sleep(20)
    # For return trip only: execute script to select 1st origin timeslot and scroll down the page
    #driver.execute_script("document.getElementById('1').click();window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage")

    # find elements by xpath
    results = driver.find_elements_by_xpath('//*[@class="main_content"]')

    for result in results:
        print(result.text)
        if "there is no train availabe" not in result.text:
            print("FOUND!")
            while (True):
                #winsound.Beep(freq, duration)
                os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        else:
            print("NOPE :(")



    driver.quit()
    print("No. of timeouts: ", timeoutCounter)
    time.sleep(30)