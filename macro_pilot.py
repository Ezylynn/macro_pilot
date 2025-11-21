from playwright.sync_api import sync_playwright, expect
import random
import os 
from dotenv import load_dotenv

# LOAD ENV FROM .env 
load_dotenv()

# CONSTANT
URL = input("Enter website URL: ")
CREDS = os.getenv('CREDS') 

def run():
    with sync_playwright() as p:
        running = True
        has_respond = False

        # LAUNCH NEW BROWSER INSTANCE AND GO TO URL
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto(URL)
        
        # SIGN UP/AUTH
        expect(page.locator(".vt-auth-form__wrapper")).to_be_visible(timeout=15000) # 15 secs timeout window in case website is slow
        auth(page)

        # DISCLAIMER
        expect(page.locator(".ant-modal-body")).to_be_visible(timeout=15000)
        dismiss_disclaimer(page)


        while running:

            while not(has_respond):
                # VALIDATE INPUT
                try:
                    user_input= input("Enter total time quiz to be looped: ") # user set total loop over quiz
                    if not user_input:
                        total_itr = 1 
                    else:
                        total_itr = int(user_input)
                    has_respond = True
                except ValueError as e:
                    print(f"Has to be a integer number {e}")


            # ATTEMPTING THE QUIZ
            for i in range(total_itr):
                qNum_clean = start_quiz(page)
                attempt_quiz(page, qNum_clean)

            # RESTART LOOP
            user_input = input("Type STOP to stop program, ENTER to continue: ").lower()
            if user_input == "stop":
                running = False # stop loop
            else:
                has_respond = False # restart the loop again if continue


def auth(page):
    page.get_by_role("textbox", name="Tên đăng nhập").click()
    page.get_by_role("textbox", name="Tên đăng nhập").fill(CREDS)
    page.get_by_role("textbox", name="Nhập mật khẩu").click()
    page.get_by_role("textbox", name="Nhập mật khẩu").fill(CREDS)
    page.get_by_role("button", name="icon: check-circle Đăng nhập").click()


def dismiss_disclaimer(page):
    disclaimer = page.locator(".ant-modal-body") 
    if disclaimer.count() > 0: # check if 'disclimaer' element body exist
        page.get_by_role("checkbox", name="Tôi đồng ý với nội quy của").check()
        page.get_by_role("button", name="Đồng ý").click()


def start_quiz(page):
    expect(page.get_by_role("heading", name="Luyện theo chủ đề")).to_be_visible(timeout=15000)

    dismiss_disclaimer(page) # prevention against the occasional disclaimer pop ups

    qNum = page.locator('span:has-text("Số câu hỏi:") strong').text_content().strip() # scrapped total questions on website
    qNum_clean = int("".join(qNum.split())) # store total questions num

    expect(page.get_by_role("button", name=f"Luyện tất cả ({qNum})")).to_be_visible(timeout=15000)
    page.get_by_role("button", name=f"Luyện tất cả ({qNum_clean})").click() # starting the quiz
    return qNum_clean


def attempt_quiz(page, qNum_clean):
    for i in range(qNum_clean):
        page.wait_for_timeout(500) # account question delay
        options = page.locator(".mc-text-question__radio-answer input[type='radio']") # fetch all input options available on page
        if options.count() > 0:
            choice_index = random.randint(0, min(3, options.count() - 1)) # return a random number between 0 and (n option - 1)
            options.nth(choice_index).check() # select the option

            btn = page.get_by_role("button", name="Tiếp", exact=True) 
            if btn.count() > 0: # check if 'Next question' element exist, if not then we know we're at the end of the quiz
                page.get_by_role("button", name="Tiếp", exact=True).click()
            else:
                page.wait_for_timeout(random.randint(0,120000))
                page.get_by_role("button", name="Kết thúc luyện thi").click()

run()
