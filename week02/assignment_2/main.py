from selenium import webdriver
import time


def main():
  try:
    browser = webdriver.Chrome()

    browser.get('https://shimo.im/login?from=home')
    time.sleep(1)

    browser.find_element_by_xpath(
      '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input'
    ).send_keys('test@test.com')

    browser.find_element_by_xpath(
      '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input'
    ).send_keys('password')

    btn_login = browser.find_element_by_xpath(
      '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button')
    btn_login.click()

    time.sleep(1)

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)

  except Exception as e:
    print(e)
  finally:
    browser.close()


if __name__ == '__main__':
  main()
