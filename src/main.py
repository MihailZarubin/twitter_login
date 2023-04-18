import time
import sys
from UsersRepository import UsersRepository
from MainHandler import MainHandler


users = UsersRepository.get_all_users()
main_handler = MainHandler()

for user in users:
    main_handler.set_user(user)
    main_handler.init_browser()
    if not main_handler.check_log_in():
        main_handler.close_browser()
        continue
    else:
        # main_handler.create_twit('Hello world!')
        # prompt = 'Write a tweet like you are Elon Musk promoting the new cryptocurrency called Doge Coin.'
        # main_handler.create_twit_ai(prompt)
        # time.sleep(5)

        # channel_name = 'dogecoin'
        channel_name = sys.argv[2]

        # With ChatGTP filtering the tweets mood
        # main_handler.like_user_twits(channel_name, 5, 'Whether the tweet is positive?')

        # Simple liking from top to down
        main_handler.like_user_twits(channel_name, 50)

    main_handler.close_browser()
