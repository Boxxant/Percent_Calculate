class Percent:
    def get_percent(self):
        while True:
            ask1 = input("What two integers do you want the percent of?")
            ask2 = input("What two integers do you want the percent of?")
            if int(ask1) < int(ask2):
                print(f"{ask1} is {int((int(ask1) / int(ask2))*100)}% of {ask2}")

            else:
                print("Please input the the lowest integer first")
                continue



Instance = Percent()
Instance.get_percent()