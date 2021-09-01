from ..control.user_crud import User

get = User.all_email()

print(get[0])

