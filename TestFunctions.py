from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

# Open Chrome and load my personal website
driver = webdriver.Chrome("C:\\Users\\SeanMac\\Selenium\\chromedriver.exe")
driver.get("http://killertechwolf.com/SeanProjects/Index.html")
driver.maximize_window()
time.sleep(3)


# Dictionary for each mathematical function on the bi-lingual math functions page
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


# Function for the math functions that only take one input
def test_func_single(x, num, input_id, compute, reset, top):
    driver.find_element(By.XPATH, '//button[text()="' + func_call(x) + '"]').click()
    time.sleep(3)
    driver.find_element_by_id(input_id).send_keys(num)
    time.sleep(3)
    driver.find_element_by_id(compute).click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(3)
    driver.find_element_by_id(reset).click()
    time.sleep(3)
    driver.find_element_by_id(top).click()


# Separate function for the greatest common divisor function because it takes two inputs
def test_func_double(y, num1, num2, input1_id, input2_id, compute, reset, top):
    driver.find_element(By.XPATH, '//button[text()="' + func_call(y) + '"]').click()
    time.sleep(3)
    driver.find_element_by_id(input1_id).send_keys(num1)
    driver.find_element_by_id(input2_id).send_keys(num2)
    time.sleep(3)
    driver.find_element_by_id(compute).click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(3)
    driver.find_element_by_id(reset).click()
    time.sleep(3)
    driver.find_element_by_id(top).click()


# Separate function for the reverse the string function page
def test_rev_string(z, strng, strng_input, rev_ltr, rev_wrd, rev_wrd_let, orig_strng, reset, top):
    driver.find_element_by_xpath('//button[text()="' + func_call(z) + '"]').click()
    time.sleep(5)
    driver.find_element_by_id(strng_input).send_keys(strng)
    time.sleep(3)
    driver.find_element_by_id(rev_ltr).click()
    time.sleep(5)
    if rev_wrd:
        driver.find_element_by_id(rev_wrd).click()
        time.sleep(5)
    if rev_wrd_let:
        driver.find_element_by_id(rev_wrd_let).click()
        time.sleep(5)
    driver.find_element_by_id(orig_strng).click()
    time.sleep(5)
    driver.find_element_by_id(reset).click()
    time.sleep(3)
    driver.find_element_by_id(top).click()


# Once the site has loaded, select the bi-lingual math functions page, and select English language option
driver.find_element_by_id('Bi_Functions').click()
time.sleep(7)
driver.find_element_by_id('eng_button').click()
eng_functions = True
jp_functions = True
time.sleep(3)
driver.switch_to.alert.send_keys('Sean')
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)

# Execute functions for English
while eng_functions:
    test_func_single(0, random.randint(10, 102), 'fibonacci1', 'fib_compute', 'fib_reset', 'fib_top_return')
    time.sleep(5)
    test_func_double(1, random.randint(1, 10000000), random.randint(1, 10000000), 'greatcomdiv1', 'greatcomdiv2',
                     'gcd_compute', 'gcd_reset', 'gcd_top_return')
    time.sleep(5)
    test_func_single(2, random.randint(1, 21), 'factorialInput', 'fact_compute', 'fact_reset', 'fact_top_return')
    time.sleep(5)
    test_func_single(3, random.randint(1, 100000000000), 'primeNumberInput', 'chkprime_compute', 'chkprime_reset',
                     'chkprime_top_return')
    time.sleep(5)
    test_func_single(4, random.randint(1, 1000), 'numbprimesInput', 'primedisp_compute', 'primedisp_reset',
                     'primedisp_top_return')
    time.sleep(5)

    test_string = 'Testing automation with Selenium in Python'

    test_rev_string(5, test_string, 'stringreverse1', 'reverse_letters', 'reverse_words', 'rev_words_letters', 'orig_string'
                    , 'string_reset', 'string_top_return')
    time.sleep(3)
    jp_functions = eng_functions
    eng_functions = False

# Change language to Japanese and run tests again
driver.find_element_by_id('jp_lang').click()
time.sleep(3)
driver.switch_to.alert.send_keys('ショーン')
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)

# Execute tests in Japanese language
while jp_functions:
    test_func_single(6, random.randint(10, 102), 'fibonacciJ1', 'fib_computeJ', 'fib_resetJ', 'fib_top_returnJ')
    time.sleep(5)
    test_func_double(7, random.randint(1, 10000000), random.randint(1, 10000000), 'greatcomdivJ1', 'greatcomdivJ2',
                     'gcd_computeJ', 'gcd_resetJ', 'gcd_top_returnJ')
    time.sleep(5)
    test_func_single(8, random.randint(1, 21), 'factorialJInput', 'fact_computeJ', 'fact_resetJ', 'fact_top_returnJ')
    time.sleep(5)
    test_func_single(9, random.randint(1, 100000000000), 'primeNumberJInput', 'chkprime_computeJ', 'chkprime_resetJ',
                     'chkprime_top_returnJ')
    time.sleep(5)
    test_func_single(10, random.randint(1, 1000), 'numbprimesJInput', 'primedisp_computeJ', 'primedisp_resetJ',
                     'primedisp_top_returnJ')
    time.sleep(5)

    test_stringJ = 'パイソンのプログラミング言語でSeleniumのテストスクリプトを勉強してる。'

    test_rev_string(11, test_stringJ, 'stringreverse1J', 'reverse_lettersJ', '', '', 'orig_stringJ', 'string_resetJ',
                    'string_top_returnJ')
    time.sleep(3)
    jp_functions = False

# After testing all of the math functions, go back to the top page and run through the Japan Packing List
driver.find_element(By.XPATH, '//button[text()="Projects Top"]').click()
time.sleep(3)

driver.find_element_by_id('Japan_Packing').click()
time.sleep(5)

packing_list_divs = driver.find_elements_by_tag_name('div')

# Go through and click on each individual button item
packing_list_buttons = driver.find_elements_by_tag_name('button')
numbuttons = len(packing_list_buttons)
for x in range(1, numbuttons):
    driver.find_element_by_xpath('//button[text()="' + packing_list_buttons[x].text + '"]').click()
    time.sleep(1)

# After every button has been clicked, click each of the categories as well until the packing has been completed
numdivs = len(packing_list_divs)
for div in range(1, numdivs):
    driver.find_element_by_xpath('//p[text()="' + packing_list_divs[div].text + '"]').click()
    time.sleep(1)

time.sleep(3)
driver.switch_to.alert.accept()

# Return to the top page and click link to go to my personal Wordpress page
driver.find_element(By.XPATH, '//button[text()="Projects Top"]').click()
time.sleep(3)

driver.find_element_by_id('Wordpress_page').click()
time.sleep(15)


# Function to test playing embedded YouTube videos on the page via links
def test_wp_page(linkname):
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

# Go through and test all videos on the page, playing 7 seconds of each video
for vid in vids:
    test_wp_page(vid.text)

driver.execute_script("window.scrollTo(0,document.body.scrollTop)")
time.sleep(3)

driver.close()
