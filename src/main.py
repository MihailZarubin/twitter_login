from UsersRepository import UsersRepository
from MainHandler import MainHandler

users = UsersRepository.get_all_users()

for user in users:
    main_handler = MainHandler(user)
    main_handler.init_browser()
    main_handler.clear_browser_cache()  # TODO: enable
    try:
        main_handler.login()
    except Exception as e:
        print(str(e))
        break
    main_handler.close_browser()
