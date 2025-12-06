# Google-map-auto-ratings-using-multiple-accounts

Google map auto ratings using selenium with python on localhost

https://www.youtube.com/watch?v=FVumnHy5Tzo&t=1s&ab_channel=HelloWorld

# If it not work use 

https://try.cometbrowser.io/

# Comet browser

# Watch up to 3 minutes and 46 seconds, and then remain in the code

## In map.py, on the 22nd line, specify the place or school, etc.

## Replace 45 line with your text..

# If it comfort to use in undetected_chromedriver script and create with multi accounts then fork it...

# 👉 Note: Every time google updates the code, it varies. So press 'Ctrl+Shift+C' to open the developer tools, and inspect and fork it..

First, open Chrome file location In my case, the Chrome location(use start in: path) is

C:\Users\Hp\AppData\Local\Google\Chrome\Application

Next, in the command prompt, navigate to the Chrome directory using the command cd C:\Users\Hp\AppData\Local\Google\Chrome\Application

Then,

use the command

chrome.exe --remote-debugging-port=8080 --user-data-dir="enter your localhost path here"

to open Chrome with remote debugging enabled. In my case, the command was

chrome.exe --remote-debugging-port=8080 --user-data-dir="C:\Users\Hp\Desktop\Bots\Chromedriver\Localhost"

then new terminal in that folder and enter map.py (letter l not one)

After opening Chrome, paste the following two lines of code from the script into the command prompt and hit enter. This will open the google map URL in Chrome, automatically...

That's it! The URL will open in the previously opened localhost Chrome and do auto ratings...

Finally, in the command prompt, enter "pip install Random" and hit enter to install the necessary library.

👉Python Install Setup=https://youtu.be/4bUOrMj88Pc

👉Note:-

👉If you have the latest version of Selenium, the code may not run.

👉open cmd and

enter

pip uninstall selenium

And enter

pip install selenium==4.2.1 or pip install selenium==4.2.0

and hit enter

and

python -c "import selenium; print(selenium.version)"

𝙏𝙝𝙞𝙨 𝙞𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣 𝙞𝙨 𝙤𝙣𝙡𝙮 𝙛𝙤𝙧 𝙚𝙙𝙪𝙘𝙖𝙩𝙞𝙤𝙣al 𝙥𝙪𝙧𝙥𝙤𝙨𝙚 𝙖𝙣𝙙 𝙬𝙚 𝙖𝙧𝙚 𝙣𝙤𝙩 𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙞𝙗𝙡𝙚 𝙛𝙤𝙧 𝙖𝙣𝙮 𝙠𝙞𝙣𝙙 𝙤𝙛 𝙞𝙡𝙡𝙚𝙜𝙖𝙡 𝙖𝙘𝙩𝙞𝙫𝙞𝙩𝙮 𝙙𝙤𝙣𝙚 𝙗𝙮 𝙩𝙝𝙞𝙨 𝙩𝙤𝙤𝙡.
