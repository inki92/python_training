security = 0
username = ""
while not username:
	username = input("Login: ")
password = ""
while not password:
	password = input("Password: ")
if username == "test" and password == "test":
	print("Hello 'test'")
	security = 3
elif username == "root" and password == "secret":
	print("Hello 'root'")
	security = 1
elif username == "guest" or password == "guest":
	print("Hello, guest!")
	security = 5
else:
	print("Access denied")
