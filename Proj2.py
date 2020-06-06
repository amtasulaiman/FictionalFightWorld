import random


class Person(object):

    def __init__(self, name: str, age: int, wealth: int = 0):
        """Constructor for Person with name, age as compulsory arguments and wealth as optional,
        it checks if the Person is an adult or not, based on that sets the '_adult field"""
        self._name = name
        self._age = age
        self._wealth = wealth
        self._adult = self.check_adult(age)

    def get_wealth(self) -> int:
        """"Getter method for retrieving a Person's wealth"""
        return self._wealth

    def get_age(self) -> int:
        """Getter method for a Person's age"""
        return self._age

    def get_name(self) -> str:
        """Getter method for a Person's name"""
        return self._name

    def set_wealth(self, wealth: int):
        """Setter method for a Person's wealth"""
        self._wealth = wealth

    def __eq__(self, other: 'Person') -> bool:
        """Returns true if both Person have the same name and age, else false"""
        if type(self) == type(other):
            return self._name == other.get_name() and self._age == other.get_age()
        return False

    def str(self) -> str:
        """Returns the string representation of this Person object's state"""
        return "\n" + str(self._name) + "| Wealth:" + str(self.get_wealth()) + "| Adult:" + str(self._adult)

    def check_adult(self, age: int) -> bool:
        """" checks if the passed argument(age) is an adult equivalent age
        and it returns if a person is a adult or not based on the age passed"""
        if age >= 18:
            self._adult = True
        else:
            self._adult = False
        return self._adult

    def get_adult(self) -> bool:
        """Getter method for adult attribute of a Person"""
        return self._adult

    def set_age(self, age: int):
        """Setter method for a Person's age"""
        self._age = age


class Fighter(Person):

    def __init__(self, name: str, age: int, wealth: int = 0):
        """Constructor first check if passed age is valid for a Fighter, if not then it creates
        the Fighter of age=18. It has a set of skills which is randomly generated with score 0-10.
        It also has a list of not with-drawable Fighters"""
        if super().check_adult(age):
            super().__init__(name, age, wealth)
        else:
            super().__init__(name, 18, wealth)
        self.__skills = {"spear": random.randint(0, 10), "unarmed combat": random.randint(0, 10),
                         "mace": random.randint(0, 10), "broadsword": random.randint(0, 10)}
        self._not_withdraw = []

    def get_skill(self, key: str) -> int:
        """Getter method for retrieving the score(level) of the particular skill for this Fighter"""
        return self.__skills.__getitem__(key)

    def set_skill(self, key: str, value: int):
        """Setter method for the skill's level it takes the particular skill and assign a valid value
        to it"""
        value = int(value)
        if 0 <= value <= 10:
            self.__skills.__setitem__(key, value)
        else:
            print("level of skill out of range [0,10]".format(value))

    def challenge(self, f1: 'Fighter', skill: str) -> None:
        """Challenge method takes two arguments, a Fighter and a desired skill to fight with.
        It first checks if a Fighter is challenging himself, prints the error if so.
        else if Fighter challenges any type of Warrior, it sends the request to that Warrior.
        else if the wealth of both the Fighter is not 0, only then we may start the fight,
        it lets both the fighters a random chance to +1 their fighting skill by calling
        'add_to_skill' method before deciding who is the winner. If else to add points
        to the winner and subtract from the loser, and prints the states of both the
        fighters after the fight."""
        if self == f1:
            print("\nA Fighter can't fight himself")

        elif isinstance(f1, Warrior):
            print("Request Sent!")
            f1.get_challenges().append(self)
            f1.challenged_skill.append(skill)
            self._not_withdraw.append(f1)

        elif self.get_wealth() != 0 and f1.get_wealth != 0:
            self._not_withdraw.clear()
            f1._not_withdraw.clear()
            fighting = Fight(self, f1, skill)
            fighting.add_to_skill(self, f1)
            winner = fighting.winner()
            print("\nWinner:", winner.get_name())

            if self.get_name() == winner.get_name():
                self.set_wealth((self.get_wealth()) + 10)
                min_wealth = (f1.get_wealth()) - 10
                if min_wealth < 0:
                    min_wealth = 0
                f1.set_wealth(min_wealth)
            else:
                f1.set_wealth((f1.get_wealth()) + 10)
                min_wealth = self.get_wealth() - 10
                if min_wealth < 0:
                    min_wealth = 0
                self.set_wealth(min_wealth)
            print("After Fight the fighters stats are:")
            print(self.str())
            print(f1.str())
        else:
            print("Not enough wealth to Fight")

    def withdraw(self, warrior: 'Warrior'):
        """This method checks if the fighter has sent any request to the passed warrior,
         if that's he case then it removes his own request sent to him so that
         he can't fight him. It prints the appropriate msg based of the withdrawal request"""
        temp = None
        for item in warrior.get_challenges():
            if item is self:
                temp = item
                if warrior not in self._not_withdraw:
                    warrior.get_challenges().remove(item)
                    print("Fighter's request has been withdrawn")
                    return
        if temp is not self:
            print("Request was never sent")
        else:
            print("Request can't be withdrawn")

    def get_not_withdraw(self) -> list:
        """Returns the list of all the Fighters that are not with-drawable for
        this Fighter"""
        return self._not_withdraw

    def str(self) -> str:
        """Returns the string representation of this Fighter object's state"""
        return super().str() + '| Skills: ' + str(self.__skills)


class Fight(object):

    def __init__(self, fighter_1: 'Fighter', fighter_2: 'Fighter', skill: str):
        """Constructor creates two fighter based to passed arguments and has a skill
        which they use for fight"""
        if isinstance(fighter_1, Fighter):
            self._f1 = fighter_1
        if isinstance(fighter_2, Fighter):
            self._f2 = fighter_2
        else:
            print("Non-Fighters can't fight")
        self._skill = skill

    def winner(self) -> 'Fighter':
        """It returns the Fighter which has the higher skill as compared to the
        the other one. If both Fighters have same skill level, random choice is
        made between the two Fighters"""
        if self._f1.get_skill(self._skill) > self._f2.get_skill(self._skill):
            return self._f1
        elif self._f1.get_skill(self._skill) < self._f2.get_skill(self._skill):
            return self._f2
        else:
            return random.choice([self._f1, self._f2])

    def add_to_skill(self, fighter_1: 'Fighter', fighter_2: 'Fighter'):
        """It creates a random generator for deciding the luck for +1 skill
        addition to each Fighter. Level is only increased for the skill they're
        fighting with."""
        chosen = random.choice([0, 1])
        max_skill = fighter_1.get_skill(self._skill) + 1
        if chosen and max_skill <= 10:
            fighter_1.set_skill(self._skill, max_skill)
            print("Skill increased for:", fighter_1.get_name())
        chosen = random.choice([0, 1])
        max_skill = fighter_2.get_skill(self._skill) + 1

        if chosen and max_skill <= 10:
            fighter_2.set_skill(self._skill, max_skill)
            print("Skill increased for:", fighter_2.get_name())


class Warrior(Fighter):

    def __init__(self, name: str, age: int, wealth: int = 0):
        """Constructor creates a Warrior which is a Fighter with additional qualities of having
        list of challenge requests(_challenges) and their respective challenged_skill
        is another list. _accepted is used to start the fight when it has been
         accepted from list"""
        super().__init__(name, age, wealth)
        self._challenges = []
        self.challenged_skill = []
        self._accepted = False

    def get_accepted(self) -> bool:
        """Getter method for accepted attribute"""
        return self._accepted

    def set_accepted(self, accept: bool):
        """"Setter method for changing the accepted state."""
        self._accepted = accept

    def str(self) -> str:
        """Returns the string representation of this Warrior object's state"""
        return super().str()

    def str_challenges(self) -> str:
        """Returns the string representation of all the challenge requests
        this Warrior has received."""
        combine = "Challenges:"
        for item in self._challenges:
            combine += " ~ " + item.str()
        return combine

    def challenge(self, f1: 'Warrior', skill: str):
        """This method overrides the method is Fighter class. With similar case:
        If this Warrior is not in a state to accept challenges, and the other person is
        a type of Warrior then leave challenge request and add to the 'not_withdraw' list
        Else if it is a valid fighter then do the same things to start the fight. If the
        winner is a fighter then add 25 pts to fighter's wealth and take 25pts out of this
        warrior's wealth. Otherwise follow the same rules as per handled in Fighter's challenge.
        """
        if self == f1:
            print("\nA Fighter can't fight himself")

        elif not self.get_accepted() and isinstance(f1, Warrior):
            print("Request Sent!")
            f1._challenges.append(self)
            f1.challenged_skill.append(skill)
            self._not_withdraw.append(f1)

        elif isinstance(f1, Fighter):

            if self.get_wealth() != 0 and f1.get_wealth != 0:
                self._not_withdraw.clear()
                f1._not_withdraw.clear()
                fighting = Fight(self, f1, skill)
                fighting.add_to_skill(self, f1)
                winner = fighting.winner()
                print("\nWinner:", winner.get_name())
                self.set_accepted(False)

                if type(winner) == Fighter:
                    f1.set_wealth((f1.get_wealth()) + 25)
                    min_wealth = (self.get_wealth()) - 25
                    if min_wealth < 0:
                        min_wealth = 0
                    self.set_wealth(min_wealth)
                    max_skill = winner.get_skill(skill) + 1
                    if max_skill > 10:
                        max_skill = 10
                    winner.set_skill(skill, max_skill)

                elif self.get_name() == winner.get_name():
                    self.set_wealth((self.get_wealth()) + 10)
                    min_wealth = (f1.get_wealth()) - 10
                    if min_wealth < 0:
                        min_wealth = 0
                    f1.set_wealth(min_wealth)

                else:
                    f1.set_wealth((f1.get_wealth()) + 10)
                    min_wealth = self.get_wealth() - 10
                    if min_wealth < 0:
                        min_wealth = 0
                    self.set_wealth(min_wealth)
                print("After Fight the fighters stats are:")
                print(self.str())
                print(f1.str())

            else:
                print("Not enough wealth to Fight")

    def accept_random(self: 'Warrior'):
        """Accept_random randomly chooses a Fighter from the list of challenges requests
        , it takes the skill from its respective list. and set the accept state to be true
         so that a successful fight can occur. Else if no requests exist, it prints the msg."""
        if not self._challenges:
            print("Challenges don't exist")
        else:
            print("\nOn accept random->")
            self.set_accepted(True)
            choose = random.choice(self._challenges)
            a_skill = self.challenged_skill.pop(self._challenges.index(choose))
            self._challenges.remove(choose)
            self.challenge(choose, a_skill)

    def decline_random(self: 'Warrior'):
        """If the list of challenges is empty is prints the appropriate msg, else it
        chooses a random request and remove it from the list."""
        if not self._challenges:
            print("Challenges don't exist")
        else:
            print("\nOn decline random->")
            choose = random.choice(self._challenges)
            if self in choose.get_not_withdraw():
                choose.get_not_withdraw().remove(self)
            self.challenged_skill.pop(self._challenges.index(choose))
            self._challenges.remove(choose)

    def accept_first(self: 'Warrior'):
        """If the list is empty, it prints the appropriate msg. Else it takes the
        first challenge and starts the fight with the challenged skill. It modifies
        the '_accept' state as well."""
        if not self._challenges:
            print("Challenges don't exist")
        else:
            print("\nOn accept first->")
            self.set_accepted(True)
            self.challenge(self._challenges.pop(0), self.challenged_skill.pop(0))

    def decline_first(self: 'Warrior'):
        """If the list is empty, it prints the msg. Else it removes the first request
        from the challenged list."""
        if not self._challenges:
            print("Challenges don't exist")
        else:
            print("\nOn decline first->")
            if self in self._challenges[0].get_not_withdraw():
                self._challenges[0].get_not_withdraw().remove(self)
            del self._challenges[0]
            del self.challenged_skill[0]

    def get_challenges(self) -> list:
        """Getter method for the challenges requests list"""
        return self._challenges


class KnightErrant(Warrior):

    def __init__(self, name: str, age: int, wealth: int = 0):
        """Constructor for creating a KnightErrant which is a Warrior with ability to
        travel."""
        super().__init__(name, age, wealth)
        self.__travelling = False

    def travel(self):
        """This methods marks the beginning of a journey of this KnightErrant"""
        print(self.get_name(), "begins journey.")
        self.__travelling = True

    def return_from_travel(self):
        """This method marks the end of a journey for this KnightErrant. It lets
        the KnightErrant sometimes find treasure en-route which adds to his wealth"""
        print(self.get_name(), "ends journey.")
        treasure = random.choice([0, 1, 2])
        if treasure:
            print("Treasure found.")
            self.set_wealth(self.get_wealth() + random.randint(5, 21))
        self.__travelling = False

    def is_travelling(self) -> bool:
        """Returns whether the KnightErrant is travelling or not"""
        return self.__travelling

    def str(self) -> str:
        """Returns a string representation of the KnightErrant's object state along
        with it's status of travelling."""
        return Fighter.str(self) + '\nTravelling Status:' + str(self.is_travelling())

    def str_challenges(self) -> str:
        """Returns the string representation of all the challenge requests
        this KnightErrant has received."""
        combine = "Challenges:"
        for item in self._challenges:
            combine += " ~ " + item.str()
        return combine

    def challenge(self, f1: 'KnightErrant', skill: str):
        """This method overrides the one in Warrior class. It has additional features of
        checking whether the Knight is travelling or not. If he is travelling then he can't
        challenge anyone or accept challenge, while others can leave him challenge requests.
        If an ordinary fighter wins against the Knight Errant, he gains 40 wealth pts and Knight
        looses 40pts from his wealth. If a Warrior wins against a Knight Errant, he wins
        20pts and Knight looses 20pts from his wealth. In all other cases, the rules have
        been set to that of Warrior's challenge method."""
        if self == f1:
            print("\nA Fighter can't fight himself")

        elif self.is_travelling():
            print("Can't fight, You're travelling")

        elif type(f1) == KnightErrant and f1.is_travelling():
            print("KnightErrant is current travelling, can't fight.")
            print("Request Sent!")
            f1._challenges.append(self)
            f1.challenged_skill.append(skill)
            self.get_not_withdraw().append(f1)

        elif not self.get_accepted() and isinstance(f1, Warrior):
            print("Request Sent!")
            f1._challenges.append(self)
            f1.challenged_skill.append(skill)
            self.get_not_withdraw().append(f1)

        elif isinstance(f1, Fighter):
            if self.get_wealth() != 0 and f1.get_wealth != 0:
                self._not_withdraw.clear()
                f1._not_withdraw.clear()
                fighting = Fight(self, f1, skill)
                fighting.add_to_skill(self, f1)
                winner = fighting.winner()
                print("\nWinner:", winner.get_name())
                self.set_accepted(False)

                if type(winner) == Fighter:
                    f1.set_wealth((f1.get_wealth()) + 40)
                    min_wealth = (self.get_wealth()) - 40
                    if min_wealth < 0:
                        min_wealth = 0
                    self.set_wealth(min_wealth)
                    max_skill = winner.get_skill(skill) + 2
                    if max_skill > 10:
                        max_skill = 10
                    winner.set_skill(skill, max_skill)

                elif type(winner) == Warrior:
                    f1.set_wealth((f1.get_wealth()) + 20)
                    min_wealth = (self.get_wealth()) - 20
                    if min_wealth < 0:
                        min_wealth = 0
                    self.set_wealth(min_wealth)
                    max_skill = winner.get_skill(skill) + 1
                    if max_skill > 10:
                        max_skill = 10
                    winner.set_skill(skill, max_skill)

                elif self.get_name() == winner.get_name():
                    self.set_wealth((self.get_wealth()) + 10)
                    min_wealth = (f1.get_wealth()) - 10
                    if min_wealth < 0:
                        min_wealth = 0
                    f1.set_wealth(min_wealth)
                else:
                    f1.set_wealth((f1.get_wealth()) + 10)
                    min_wealth = self.get_wealth() - 10
                    if min_wealth < 0:
                        min_wealth = 0
                    self.set_wealth(min_wealth)
                print("\nAfter Fight the fighters stats are:")
                print(self.str())
                print(f1.str())

            else:
                print("Not enough wealth to Fight")

    def accept_first(self: 'KnightErrant'):
        """this method overrides the one in Warrior class because Knight Errant has the
        ability to travel and while travelling he can't accept a fight. Hence, if only
        Knight Errant is not travelling, then Accept the challenge. It takes the first
        challenge from the list and starts the fight."""
        if not self._challenges:
            print("Challenges don't exist")
        elif not self.is_travelling():
            print("\nOn accept first->")
            self.set_accepted(True)
            self.challenge(self._challenges.pop(0), self.challenged_skill.pop(0))

    def accept_random(self: 'KnightErrant'):
        """This method overrides the one in Warrior class. It randomly chooses a Fighter
        from the list of challenge requests and starts the fight if this Knight Errant is
        not travelling."""
        if not self._challenges:
            print("Challenges don't exist")
        elif not self.is_travelling():
            print("\nOn accept random->")
            self.set_accepted(True)
            choose = random.choice(self._challenges)
            a_skill = self.challenged_skill.pop(self._challenges.index(choose))
            self._challenges.remove(choose)
            self.challenge(choose, a_skill)
