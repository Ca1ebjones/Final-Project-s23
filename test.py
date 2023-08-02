from Manager import Manager
m=Manager()
m.generate_password("google","gman", 12)
m.generate_password("youtube","gman", 14)
m.save()
print(m.load())