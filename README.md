# Here i will have some bots with different functionality

#
## DEPLOYING OUR APP ON HEROKU:
1) Brew install heroku/brew/heroku
2) heroku login *Enter your email and password from the heroku profile
3) heroku create *Make a new rep on the heroku server
4) git status *See what files (in the current folder) aren't included in the rep 
5) pip install PyTelegramBotApi  *Installing some necessary libraries 
6) heroku git:remote --app  <NAME OF UR REP>
7) git remote
8) git push heroku master 
# Launch 
9) heroku ps:scale bot=1 *Turn on the bot
10) heroku ps:stop bot * Turn off the bot

# Check Your bot and make commit:
1) git status *Nake sure that you are ready for it
2) git commit -m "Initial Commit" -a
3) git push heroku master
### we've made a commit
1) heroku ps -a <REP NAME HERE> *See stats of ur rep
