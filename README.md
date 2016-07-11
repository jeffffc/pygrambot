# pygrambot
Telegram Bot API Python Framework

Follow these steps to quickly setup a Python-powered Telegram bot using Heroku. I hope it saves you some time!

1. Create an account on https://heroku.com/
2. Install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and figure out how to use it in your OS
3. Clone this repo: `git clone https://github.com/cauebs/pygrambot.git` OR download and extract [this zip](https://github.com/cauebs/pygrambot/archive/master.zip)
4. Open the `pygrambot` folder
5. Authenticate with `heroku login`
6. Create the app with `heroku apps:create #app-name-here# --buildpack heroku/python` (only lower case and hyphens allowed)
7. And `heroku git:remote -a #app-name-here#` to make things easier
7. If you haven't yet, create a bot with the [BotFather](https://telegram.me/botfather) and copy the token
8. Now run `heroku config:set TOKEN=#paste-token-here#`
9. And `heroku config:set APPNAME=#app-name-here#` (last time you have to type that name in, I promise)

X. Lastly, run `git push heroku master` and test your bot.

If it doesn't work, [telegram me](https://telegram.me/cauebs) and we can try to figure it out together.


*License: GPLv3*