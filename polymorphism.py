class Application:
    def chat(self):
        raise NotImplementedError("Subclass must implement this method")


class LinkedIn(Application):
    def chat(self):
        return "LinkedIn can perform chating"


class Facebook(Application):
    def chat(self):
        return "Facebook can perform chatting!"


apps = [LinkedIn(), Facebook()]

# Call the speak method on each object
for applications in apps:
    print(applications.chat())
