''' Helium that makes specifying web automation cases as simple as describing them to someone looking over their shoulder at a screen as well as scraping utility by using with requests_HTML to get results. '''
''' katesanalyst@gmail.com | @katesanalyst '''

from helium import *
from requests_html import HTMLSession
import time
import random

url = 'https://bigcrewnow.in/product/iphone-5s-32gb/'
session =  HTMLSession(); res =  session.get(url)
xtest = start_firefox(res.url,headless=True)

phone =  random.randint(1100100000, 9199999999); email = f'{phone}@buggy.co.k'; pwd = email

# Select COLOR of the phone from ListBox
select(ComboBox("Choose an option"),"Gold")
click("Add to cart")

# Cart Process
wait_until(Text("You Have 1 Item In Your Cart").exists)
press(PAGE_DOWN)
click("Proceed to checkout")
print('Cart process... Done')

# Checkout / Billing Details
write("First name", into='First name')
write("Last name", into='Last name')
write("STADDRESS", into='Street address')
write("Town", into='Town'); 
write("Chennai", into='State')
write("000000", into='Postcode')
write(phone, into='Phone')
write(email, into='Email')
press(TAB);press(PAGE_DOWN) 
print('Checkout process... Done')

# User Account creation
if not CheckBox("Create an account").is_checked():
    click(CheckBox("Create an account"))

write(email, into='Create account password') if Text("Create account password").exists() else print('Create account password not availed')
print('Account creation suceeded... ',phone,' |', email, ' |', pwd)

# Order placement intitation
click("Place order");press(PAGE_DOWN);time.sleep(5)
if xtest.current_url  == 'https://bigcrewnow.in/checkout/':
    click("Place order");press(PAGE_DOWN);time.sleep(15)
    # wait_until(Text('order').exists,timeout_secs=20,interval_secs=0.2)

if xtest.current_url == 'https://bigcrewnow.in/checkout/':
    print('Internet connection outage check net speed..')
    xtest.quit();kill_browser()
    print('Account Created whereas Order Placement not happend')
else:
    print('Order placed successfully', xtest.current_url)
    # To get order details by using requests_html 
    durl = (xtest.current_url);res = session.get(durl)
    print(res.html.find('ul[class="woocommerce-order-overview woocommerce-thankyou-order-details order_details"]',first=True).text.encode("ascii", "ignore").decode("utf-8", "ignore"))
    ord = (res.html.find('ul[class="woocommerce-order-overview woocommerce-thankyou-order-details order_details"]',first=True).text.encode("ascii", "ignore").decode("utf-8", "ignore"))
    xtest.quit();kill_browser()

    # Saving as file
    odetails = {'Phone Number': phone, 'Password': pwd, 'EMAIL': email, 'Details': ord, 'URL': durl}
    text_file = open(f'{phone}.txt', "w")
    text_file.write(str(odetails))
    text_file.close()
    print('Order details saved sucessfully...')
