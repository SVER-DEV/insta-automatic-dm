import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

x = 0

def dmer():
    usrnames = ['todmuser']  # dm을 받는 상대방의 태그
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument(
        '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    browser = webdriver.Chrome((ChromeDriverManager().install()), options=options)
    browser.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)

    usrname_bar = browser.find_element_by_name('username')
    passwrd_bar = browser.find_element_by_name('password')

    username = 'id'  # 아이디
    password = 'pw'  # 비밀번호

    usrname_bar.send_keys(username)
    passwrd_bar.send_keys(password + Keys.ENTER)

    time.sleep(11)

    def send_msg(usrnames):
        browser.get('https://www.instagram.com/direct/new/')

        time.sleep(5)

        to_btn = browser.find_element_by_name('queryBox')
        to_btn.send_keys(usrnames)

        time.sleep(8)

        chk_mrk = browser.find_element_by_css_selector('.HVWg4')
        chk_mrk.click()

        time.sleep(3)

        nxt_btn = browser.find_element_by_xpath('//div[@class="mXkkY KDuQp"]')
        nxt_btn.click()

        time.sleep(6)

        txt_box = browser.find_element_by_tag_name('textarea')
        txt_box.send_keys(f"text")  # 보낼 텍스트

        time.sleep(2)

        snd_btn = browser.find_elements_by_css_selector('.sqdOP.yWX7d.y3zKF')
        snd_btnn = snd_btn[len(snd_btn)-1]
        snd_btnn.click()

        time.sleep(4)

    count = 0
    try:
        for usrnamee in usrnames:
            send_msg(usrnamee)
            count += 1

    except TypeError:
        print('Failed!')

    browser.quit()

dmer()
