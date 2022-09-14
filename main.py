import pickle

from config import *
from parse_VK.vk_actions import *


def deleteTask(task):
    del_task_btn = task.find_element(By.CLASS_NAME, 'close-task-btn')
    del_task_btn.click()


def completeTask(task):
    task.find_element(By.CLASS_NAME, 'blue--text').click()
    time.sleep(3)

    vk_target_driver.switch_to.window(vk_target_driver.window_handles[0])

    vk_target_driver.window_handles.pop(-1)
    time.sleep(2)

    btn_checkout = task.find_element(By.CLASS_NAME, 'mdl-button--with-loader')
    btn_checkout.click()

    time.sleep(3)



def work_with_task(task):
    taskName = task.find_element(By.CLASS_NAME, 'task-name').text
    taskHref = task.find_element(By.CLASS_NAME, 'blue--text').get_property('href')

    actions_dict = {
        'Вступите': joinToCommunity(taskHref),
        'Поставьте': likePost(taskHref),
        'Добавить': addToFriends(taskHref),
    }

    try:
        return actions_dict[taskName.split()[0]]
    except KeyError as e:
        deleteTask(task)


def parse_VK_target(vk_target_cookie_file):
    vk_target_driver.get('https://vktarget.ru')
    time.sleep(5)
    for cookie in pickle.load(open(vk_target_cookie_file, 'rb')):
        vk_target_driver.add_cookie(cookie)

    vk_target_driver.refresh()
    vk_target_driver.get('https://vktarget.ru/list')

    vk_registration()

    time.sleep(5)
    while True:
        try:
            tasks = vk_target_driver.find_elements(By.CLASS_NAME, 'available__row')

            if tasks:
                for i, task in enumerate(tasks):
                    try:
                        work_with_task(task)
                        completeTask(task)
                    except:
                        continue
            else:
                time.sleep(20)
        except Exception as e:
            print(e)
            continue


if __name__ == '__main__':
    parse_VK_target('cookie/vk_target_cookie/cookies_1')
