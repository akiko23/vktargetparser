import time
from selenium.webdriver.common.by import By

from parser228.main import deleteTask
from parser228.parse_VK.vk_config import *


def vk_registration():
    vk_driver.get('https://vk.com/login')
    time.sleep(4)

    input_login = vk_driver.find_element(By.CSS_SELECTOR, '#index_email')
    input_login.send_keys('919817124248')
    time.sleep(3)

    btn_log = vk_driver.find_element(By.CLASS_NAME, 'FlatButton--primary')
    btn_log.click()

    time.sleep(6)

    try:
        password = vk_driver.find_elements(By.TAG_NAME, 'input')[-1]
    except IndexError:
        password = vk_driver.find_element(By.TAG_NAME, 'input')

    password.send_keys('aJjnJbiK')
    time.sleep(3)

    btn_password = vk_driver.find_element(By.CLASS_NAME, 'vkuiButton--aln-center')
    btn_password.click()

    time.sleep(10)


def joinToCommunity(com_href):
    vk_driver.get(com_href)
    time.sleep(6)

    try:
        sub_btn = vk_driver.find_element(By.CLASS_NAME, 'FlatButton--wide')
        sub_btn.click()
        # pickle.dump(dr.get_cookies(), open('vk_cookies', 'wb'))

        # for vk_cookie in pickle.load(open('vk_cookies', 'rb')):
        #     vk_dr.add_cookie(vk_cookie)
    except:
        vk_registration()
        vk_driver.get(com_href)

        sub_btn = vk_driver.find_element(By.CLASS_NAME, 'page_action_left').find_elements(By.TAG_NAME, 'button')[-1]
        sub_btn.click()


def likePost(com_href):
    vk_driver.get(com_href)
    time.sleep(5)

    try:
        vk_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        like_btn = vk_driver.find_element(By.CLASS_NAME, 'PostButtonReactions--post')
        like_btn.click()
    except:
        like_btn = vk_driver.find_element(By.CLASS_NAME, 'PostButtonReactions--post')
        like_btn.click()


def watch_post(taskHref):
    try:
        vk_driver.get(taskHref)
        vk_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except:
        pass


def addToFriends(taskHref):
    vk_driver.get(taskHref)
    time.sleep(2)

    add_friend = vk_driver.find_element(By.CSS_SELECTOR,
                                        '#narrow_column > div.page_block.page_photo.ProfileActions > aside > div > div > div > div > button')
    add_friend.click()


# def send_post(taskHref):
#     try:
#         vk_driver.get(taskHref)
#
#         vk_driver.execute_script('window.scrollTo(0, document.body.scrollHeight / 2);')
#
#         send_btn = vk_driver.find_element(By.CSS_SELECTOR, '#post-197097505_4711 > div > div.post_content > div > '
#                                                            'div.like_wrap._like_wall-197097505_4711 > div > '
#                                                            'div.like_btns '
#                                                            '> div.PostBottomAction.PostBottomAction--withBg.share'
#                                                            '._share')
#         send_btn.click()
#         time.sleep(4)
#     except:
#         pass
