#default login page spring login will username and password trigger the authentication process is /login.
u='rushikesh'
p='rushikesh'
username = input("Please enter your username: ")
if (username == u):
 password = input("Please enter your password: ")
 if (password == p):
  print("logged in successfully")
 else:
    print("password incorrect")
else:
   print("username incorrect") 
