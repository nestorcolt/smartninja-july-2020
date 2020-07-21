# 6) Object-oriented programming (OOP)
##############################################################################################

class BasketballPlayer():

    # the functions declared inside of a class are called methods
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

        # test with init method
        # print("Class name: {} with instance of {} {}".format(self.__class__.__name__, self.first_name, self.last_name))

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm=203, weight_kg=113, points=27.2,
                          rebounds=7.4, assists=7.2)

print(lebron.first_name)
print(lebron.points)
print(lebron.weight_to_lbs())

kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2,
                           rebounds=7.1, assists=4)

print(kev_dur.first_name)
print(kev_dur.points)
print(kev_dur.weight_to_lbs())
