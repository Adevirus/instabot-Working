from instabot import Bot 

bot=Bot()

bot.login(username=" ",password=" ")

tags=['python','programmer','technology']

for i in tags:
	bot .like_hashtag(i,amount=20)

 
