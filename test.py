from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)

driver.set_window_size(800, 480) # set the window size that you need
driver.get('https://twitter.com/cathcam/status/1057659326767226880')
driver.save_screenshot('github.png')