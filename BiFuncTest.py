from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
import jaconv

driver = webdriver.Chrome("C:\\Users\\SeanMac\\Selenium\\chromedriver.exe")
driver.get("http://killertechwolf.com/SeanProjects/Index.html")
driver.maximize_window()
time.sleep(3)

def func_call(i):
    switcher = {
        0: 'The Fibonacci Sequence',
        1: 'The Greatest Common Divisor',
        2: 'The Factorial Function',
        3: 'Check Prime',
        4: 'Display Primes',
        5: 'Reverse the String',
        6: 'フィボナッチ数列',
        7: '最大公約数',
        8: '階乗',
        9: '素数の確認',
        10: '素数の表示',
        11: '文字を逆にする',
    }
    return switcher.get(i, "Invalid function call")

driver.find_element_by_id('Bi_Functions').click()
time.sleep(7)
driver.find_element_by_id('eng_button').click()
time.sleep(3)
driver.switch_to.alert.send_keys('Sean')
time.sleep(3)
driver.switch_to.alert.accept()

buttons = driver.find_elements_by_tag_name('button.functionbutton')
numbuttons = len(buttons)
print(numbuttons)
for x in range(0, numbuttons//2):
    print(func_call(x))

time.sleep(5)
driver.find_element_by_id('fib_eng').click()

time.sleep(3)

def test_fib(num):
    driver.find_element_by_tag_name('input').send_keys(num)
    time.sleep(3)
    driver.find_element_by_id('fib_compute').click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(3)
    driver.find_element_by_id('fib_reset').click()
    time.sleep(3)
    driver.find_element_by_id('fib_top_return').click()

test_fib(random.randint(25,102))
time.sleep(5)

driver.find_element(By.XPATH, '//button[text()="' + func_call(1) + '"]').click()
time.sleep(3)

def test_gcd(num1, num2):
    driver.find_element_by_id('greatcomdiv1').send_keys(num1)
    driver.find_element_by_id('greatcomdiv2').send_keys(num2)
    time.sleep(3)
    driver.find_element_by_id('gcd_compute').click()
    time.sleep(10)
    driver.find_element_by_id('gcd_reset').click()
    time.sleep(3)
    driver.find_element_by_id('gcd_top_return').click()

test_gcd(random.randint(1,10000000), random.randint(1,10000000))
time.sleep(5)

driver.find_element(By.XPATH, '//button[text()="' + buttons[2].text + '"]').click()
time.sleep(5)

def test_factorial(num):
    driver.find_element_by_id('factorialInput').send_keys(num)
    time.sleep(3)
    driver.find_element_by_id('fact_compute').click()
    time.sleep(10)
    driver.find_element_by_id('fact_reset').click()
    time.sleep(3)
    driver.find_element_by_id('fact_top_return').click()

test_factorial(random.randint(1,21))
time.sleep(5)

driver.find_element_by_xpath('//button[text()="' + buttons[3].text + '"]').click()
time.sleep(5)

def test_prime(num):
    driver.find_element_by_id('primeNumberInput').send_keys(num)
    time.sleep(3)
    driver.find_element_by_id('chkprime_compute').click()
    time.sleep(10)
    driver.find_element_by_id('chkprime_reset').click()
    time.sleep(3)
    driver.find_element_by_id('chkprime_top_return').click()

test_prime(random.randint(1, 100000000000))
time.sleep(5)

driver.find_element_by_xpath('//button[text(), "' + func_call(4) + '"]').click()
time.sleep(5)

def test_display_primes(num):
    driver.find_element_by_id('numbprimesInput').send_keys(num)
    time.sleep(3)
    driver.find_element_by_id('primedisp_compute').click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(2)
    driver.find_element_by_id('primedisp_reset').click()
    time.sleep(3)
    driver.find_element_by_id('primedisp_top_return').click()

test_display_primes(random.randint(1, 1000))
time.sleep(5)

driver.find_element_by_xpath('//button[text()="' + buttons[5].text + '"]').click()
time.sleep(5)

def test_rev_string(strng):
    driver.find_element_by_id('stringreverse1').send_keys(strng)
    time.sleep(3)
    driver.find_element_by_id('reverse_letters').click()
    time.sleep(10)
    driver.find_element_by_id('reverse_words').click()
    time.sleep(10)
    driver.find_element_by_id('rev_words_letters').click()
    time.sleep(10)
    driver.find_element_by_id('orig_string').click()
    time.sleep(10)
    driver.find_element_by_id('string_reset').click()
    time.sleep(3)
    driver.find_element_by_id('string_top_return').click()

revstrng = 'Testing automation with Selenium in Python'
test_rev_string(revstrng)
time.sleep(5)

driver.find_element_by_id('jp_lang').click()
time.sleep(3)
driver.switch_to.alert.send_keys('ショーン')
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)

numbuttonsjp = numbuttons//2

for x in range(numbuttonsjp, numbuttons):
    print(jaconv.normalize(buttons[x].text, 'NFKC'))

time.sleep(7)
driver.find_element(By.XPATH, '//button[text()="Projects Top"]').click()
time.sleep(3)

driver.find_element_by_id('Japan_Packing').click()
time.sleep(5)

packing_list_divs = driver.find_elements_by_tag_name('div')

packing_list_buttons = driver.find_elements_by_tag_name('button')
numbuttons = len(packing_list_buttons)
for x in range(1, numbuttons):
    driver.find_element_by_xpath('//button[text()="' + packing_list_buttons[x].text + '"]').click()
    time.sleep(1)

numdivs = len(packing_list_divs)
for div in range(1, numdivs):
    driver.find_element_by_xpath('//p[text()="' + packing_list_divs[div].text + '"]').click()
    time.sleep(1)

time.sleep(3)
driver.switch_to.alert.accept()

driver.find_element(By.XPATH, '//button[text()="Projects Top"]').click()
time.sleep(3)

driver.find_element_by_id('Wordpress_page').click()
time.sleep(15)

def test_page(linkname):
    driver.find_element_by_link_text(linkname).click()
    time.sleep(3)
    driver.find_element_by_id("colorbox").click()
    time.sleep(7)
    driver.find_element_by_id("colorbox").click()
    time.sleep(3)
    driver.execute_script("$('#cboxOverlay').css('visibility', 'hidden');")
    driver.execute_script("$('#colorbox').css('visibility', 'hidden');")
    time.sleep(2)

vids = driver.find_elements_by_class_name('popup.cboxElement')

for vid in vids:
    test_page(vid.text)

driver.execute_script("window.scrollTo(0,document.body.scrollTop)")
time.sleep(3)

driver.close()
