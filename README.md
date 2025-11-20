# macro pilot - cool funny name I totally thought of

a small rant, currently taking an online course that requires me to do practice MCQs as part of the course, but the thing is that even if you score a perfect score and understand the topic well, you would STILL need to fulfil the minimum time quota which can range between 12 - 20 hours (absolutely insane) & some sections have like 120+ MCQs questions 

a while back ago, i noticed the system only check the start and end time, how many questions completed and num of questions incorrect/correct to work out the final time recorded on the app, and you dont need to get all of the question correct as well

at first, i was just mindlessly clicking the options on my phone to fill in the quota but then it got seriously annoying when i had other errands and tasks i had to do. i thought of using a macro application but it got difficult since the MCQs have different range of options for each question (2-4) and the changes in resolution from the questions' pictures makes it unreliable to rely on mouse clicks

and so i had enough, i spent the last 5 hours learning Playwright (an end-to-end testing library) to basically create my own personalized macro that would allow me to leave my machine to automatically do any of the MCQ practice sections. it works so well and ngl i can definitely see myself using this lib more in the future hehe :)

this project is personal and experimental, obviously do it at your own risk if you want to try something similar, for me, this was so worth it haha.  

## Features
- Random answer selection (if you can count that as a feature)
- A random timer is set near the end of the quiz before submitting - i'll let u guess why  
- Automatic navigation through multi-step questions  
- Optional failsafes for popups and modals  
- Works headless or in a visible browser (Playwright)

## Requirements
- Python 3  
- Playwright (`pip install playwright` + `playwright install firefox/chromium`)

## Running the Script (not sure why since this is personalized and tailored to a specific website)
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install playwright`
- `playwright install firefox/chromium`
- `python3 macro_pilot.py`
