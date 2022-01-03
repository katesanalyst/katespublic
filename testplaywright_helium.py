
''' Sample file learn for Helium vs Playwright'''

from playwright.sync_api import sync_playwright
from requests_html import HTMLSession
import random
import time

def playwright_sample(url):
    with sync_playwright() as p:
        browser =  p.firefox.launch(headless = False)
        page =  browser.new_page()
        page.goto(url)

        # Select COLOR of the phone from ListBox
        page.select_option('#colors', 'Gold')
        page.click('button[type=submit]')    # page.click('text = Add to cart'); found TYPE hence used as same; below button used as Text because of link.
        # Cart Process
        page.click('text = Proceed to checkout')
        page.wait_for_load_state('load')
        print('Cart process... Done')

        # Checkout / Billing Details
        page.fill('#billing_first_name', 'Kates First')
        page.fill('#billing_last_name', 'kates Last')
        page.fill('#billing_address_1', 'Address Bunny')
        page.fill('#billing_city', 'TEST CITY')
        page.fill('#billing_postcode','00000')
        page.fill('#billing_phone', str(phone))
        page.fill('#billing_email', str(email))
        print('Checkout process... Done')

        # User Account creation
        page.click('input[name=createaccount]')
        page.fill('#account_password','1231231232131231@')
        print('Account creation suceeded... ',phone,' |', email, ' |', pwd)

        # Order placement intitation
        page.keyboard.press('PageDown')
        page.click('text = place order')
        # page.wait_for_load_state('load')
        
        # The site doesn't support for CLICK action well; then added few codes for continuation 
        # Did some break by using IF condition then doing the same action; web automation to makeup based on developed. The exportation to  success order placement.
        if page.url == 'https://bigcrewnow.in/checkout/':
            print('Seems not rendered ... have to place order again')
            page.click('text = place order') 
            page.wait_for_load_state('load')
            page.wait_for_url('**/order-received**')
            print('Order placed successfully', page.url)

        else:
            print('Order placed successfully', page.url)
        
        # To get order details by using requests_html 
        durl = (page.url);res = session.get(durl)
        ord = (res.html.find('ul[class="woocommerce-order-overview woocommerce-thankyou-order-details order_details"]',first=True).text.encode("ascii", "ignore").decode("utf-8", "ignore"));print(ord)
        # Saving as file
        odetails = {'Phone Number': phone, 'Password': pwd, 'EMAIL': email, 'Details': ord, 'URL': durl}
        text_file = open(f'{phone}.txt', "w")
        text_file.write(str(odetails))
        text_file.close();  browser.close()
        print('Order details saved sucessfully...')

if __name__ == '__main__':
    url = 'https://bigcrewnow.in/product/iphone-5s-32gb/'
    session =  HTMLSession()
    phone =  random.randint(1500105000, 9199999999); email = f'{phone}@buggy.co.k'; pwd = email
    playwright_sample(url)


