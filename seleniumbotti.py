from selenium import webdriver
import random
import time
from selenium import howrsefeed
from selenium import howrsetraining


def log_in():
    # address where is chrome driver
    driver = webdriver.Chrome('CHROMEDRIVER ADDRESS')

    driver.get("http://wwww.howrse.fi")
    driver.maximize_window()
    sleep()
    driver.find_element_by_id('header-login-label').click()
    long_sleep()
    user = driver.find_element_by_id('login')

    #Username and password
    user.send_keys('USERNAME')
    long_sleep()
    password = driver.find_element_by_id('password')
    password.send_keys('PASSWORD')
    sleep()
    driver.find_element_by_id('authentificationSubmit').click()
    sleep()
    driver.get("http://www.howrse.fi/elevage/chevaux/")
    sleep()
    # Horse ID where start
    driver.get('https://www.howrse.fi/elevage/chevaux/cheval?id=FIRSTHORSEID')

    """
    You can choose.
    If you have automatic feed, choose Auto_takeCare_Lesson
    or Auto_takeCare (no lesson then)
    If you don't have automatic feed then choose NoAuto_takeCare
     Use # to hide other
    """
    # Change value that how many horse you want take care of
    NoAuto_takeCare(driver, 1)
    Auto_takeCare_Lesson(driver, 1)
    Auto_takeCare(driver, 1)


    #Log out
    log_out = driver.find_element_by_xpath("html/body/div[@id='container']/header/nav[1]/ul/li[3]")
    sleep()
    log_out.click()
    sleep()
    log_out = driver.find_element_by_xpath("html/body/div[@id='container']/header/nav[1]/ul/li[3]/div/ul/li[6]")
    log_out.click()
    sleep()
    driver.close()

def NoAuto_takeCare(driver, takecare):
    sleep()
    care = 0
    count = 0
    randhorse = random_horse()
    while(care <takecare):
        driver.find_element_by_id("boutonPanser").click()
        sleep()
        driver.find_element_by_id("boutonCoucher").click()
        sleep()
        driver.find_element_by_id("boutonNourrir").click()
        sleep()
        try:
            howrsefeed.findfeed(driver)
            sleep()

        except:
            pass
            sleep()

        care += 1
        count += 1
        print(care)
        randhorse = check(randhorse, count)
        driver.find_element_by_id("nav-next").click()
        sleep()

def Auto_takeCare(driver, takecare):
    sleep()
    care = 0
    count = 0
    randhorse = random_horse()
    while care < takecare:
        driver.find_element_by_id("boutonPanser").click()
        sleep()
        try:
            driver.find_element_by_id("boutonNourrir").click()
            sleep()
            driver.find_element_by_id("feed-button").click()
            sleep()
        except:
            pass
        care += 1
        count += 1
        print(care)
        randhorse = check(randhorse, count)
        driver.find_element_by_id("nav-next").click()
        sleep()

def Auto_takeCare_Lesson(driver, takecare):
    sleep()
    care = 0
    count = 0
    randhorse = random_horse()
    while care < takecare:
        lesson(driver)
        sleep()
        driver.find_element_by_id("boutonPanser").click()
        sleep()
        try:
            driver.find_element_by_id("boutonNourrir").click()
            sleep()
            driver.find_element_by_id("feed-button").click()
            sleep()
        except:
            pass

        care += 1
        count += 1
        print(care)
        randhorse = check(randhorse, count)
        driver.find_element_by_id("nav-next").click()
        sleep()


def lesson(driver):
    try:
        driver.find_element_by_id("boutonMissionEquus").click()
    except:
        try:
            driver.find_element_by_id("boutonMissionForet").click()
        except:
            try:
                driver.find_element_by_id("boutonMissionMontagne").click()
            except:
                pass
        sleep()


def check(randhorse, count):
    if count == randhorse:
        wait = random_wait()
        print("Wait ", wait, " seconds")
        time.sleep(wait)
        randhorse = random_horse()
        return randhorse
    else:
        return randhorse


def sleep():
    time.sleep(random.uniform(0.47, 0.55))


def long_sleep():
    time.sleep(random.uniform(5.75, 12.103))


def very_long_sleep():
    time.sleep(random.uniform(90.75, 454.103))


def random_horse():
    horse = random.randint(18, 170)
    return horse


def random_wait():
    wait = random.uniform(5, 50)
    return wait

if __name__ == "__main__":
    log_in()
    exit()
