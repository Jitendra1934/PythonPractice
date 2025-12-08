from ClassAndObject import User
from post import Post

mainUser = User("jithu", 26, "UAT")
mainUser.get_Details()

p=Post("this is written by", mainUser.name)
p.get_details()