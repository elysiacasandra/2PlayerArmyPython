"""
Author: Elysia Giannis (29694736)

Abstract class (Fighter) and derived non-abstract classes (Soldier, Archer and Cavalry)
represent the characteristics of each type of fighter in the game described.
These classes are tested in test_task2.py

Class "Army" creates an army with an appropriate number of each type of fighter.
It then prints the life and experience of each member of the army.
This class is tested in test_task3.py
"""

# import files and classes needed
from abc import ABC, abstractmethod
from typing import TypeVar, Generic
T = TypeVar('T')
import stack
import queue


"Creating abstract parent class 'Fighter' with methods which hold information about qualities of the fighter."
class Fighter(ABC, Generic[T]):


    def __init__(self, life: int, experience: int) -> None:
        """
        Initialise the variables using the amount received as input.
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a setter method
        :param life: the amount of lives the fighter has
        :param experience: the experience the fighter has
        :return: None
        """
        # validate inputs life and experience using a precondition
        if life < 0:
            raise ValueError("Life cannot be negative")
        if experience < 0:
            raise ValueError("Experience cannot be negative")

        # define instance variables
        self.life = life
        self.experience = experience


    def is_alive(self) -> bool:
        """
        Declares whether the player is alive (T if alive).
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a setter method
        :return: True/False (bool)
        """
        if self.life > 0:
            return True
        else:
            return False


    def lose_life(self, lost_life: int) -> None:
        """
        Decreases the life of the unit by the amount indicated by lost_life.
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a setter method
        :param lost_life: number of lives lost
        :return: None
        """
        # validate input lost_life by using a precondition
        if lost_life < 0:
            raise ValueError("Lost lives must be greater than or equal to zero")

        # decrement life by the amount of lives lost
        self.life -= lost_life


    def gain_experience(self, gained_experience: int) -> None:
        """
        Increases the experience of the unit by the amount indicated by gained_experience.
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a setter method
        :param gained_experience: the number of experiences gained from killing another fighter
        :return: None
        """
        # validate input gained_experience by using a precondition
        if gained_experience < 0:
            raise ValueError("Gained experience must be greater than or equal to zero")

        # increment experience by the amount of experience gained
        self.experience += gained_experience


    def get_experience(self) -> int:
        """
        Returns the experience of the unit.
        No current implementation.
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a getter method
        :return: amount of experiences the fighter has (int)
        """
        return self.experience


    @abstractmethod
    def get_speed(self) -> int:
        """
        No current implementation.
        """
        pass


    @abstractmethod
    def get_cost(self) -> int:
        """
        No current implementation.
        """
        pass


    @abstractmethod
    def attack_damage(self) -> int:
        """
        No current implementation.
        """
        pass


    @abstractmethod
    def defend(self, damage: int) -> None:
        """
        No current implementation.
        """
        pass


    @abstractmethod
    def __str__(self) -> str:
        """
        No current implementation.
        """
        pass



"Creating child class of 'Fighter', 'Soldier'"
class Soldier(Fighter[T]):


    # modifying inherited methods to give them implementation for Soldier


    def __init__(self) -> None:
        # calling parent class with Soldier's inputs for life and experience
        Fighter.__init__(self, 3, 0)


    def get_speed(self) -> int:
        """
        Gets the speed of the Soldier.
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a getter method
        :return: speed of the fighter (int)
        """
        return 1 + self.get_experience()


    def get_cost(self) -> int:
        """
        Gets cost of the Soldier.
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a getter method
        :return: cost of the fighter (int)
        """
        return 1


    def attack_damage(self) -> int:
        """
        Calculates the amount of damage the Soldier can have on attack
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a setter method
        :return: the amount of damage the fighter inflicts on attack (int)
        """
        return 1 + self.get_experience()


    def defend(self, damage: int) -> None:
        """
        Calculates whether a life is lost after the Soldier defends an attack.
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a setter method
        :param damage: the amount of damage the fighter has incurred due to defending an attack
        :return: None
        """

        # validate input damage by using preconditions
        if damage < 1:
           raise ValueError("Damage must be greater than or equal to zero")
        if damage > self.experience:
            #decrement life by one after defence
            self.lose_life(1)


    def __str__(self) -> str:
        """
        Returns a string with the Soldier and current life and experience
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a getter method
        :return: string with soldiers current life and experience (str)
        """
        return "Soldier's life = " + str(self.life) + " and experience = " + str(self.get_experience())



"Creating child class of 'Fighter', 'Archer'"
class Archer(Fighter[T]):


    # modifying inherited methods to give them implementation for Archer


    def __init__(self) -> None:
        # calling parent class with Archer's inputs for life and experience
            Fighter.__init__(self, 3, 0)


    def get_speed(self) -> int:
        """
        Gets the speed of the Archer.
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a getter method
        :return: speed of the fighter (int)
        """
        return 3


    def get_cost(self) -> int:
        """
        Gets cost of the Archer.
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a getter method
        :return: cost of the fighter (int)
        """
        return 2


    def attack_damage(self) -> int:
        """
        Calculates the amount of damage the Archer can have on attack
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a setter method
        :return: the amount of damage the fighter inflicts on attack (int)
        """
        return 1 + self.get_experience()


    def defend(self, damage:int) -> None:
        """
        Calculates whether a life is lost after the Archer defends an attack.
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a setter method
        :param damage: the amount of damage the fighter has incurred due to defending an attack
        :return: None
        """
        # validate input damage by using a precondition
        if damage < 0:
            raise ValueError("Damage must be greater than or equal to zero")

        # decrement life by one after defence
        self.life -= 1


    def __str__(self) -> str:
        """
        Returns a string with the Archer and current life and experience
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a getter method
        :return: string with archer's current life and experience (str)
        """
        return "Archer's life = " + str(self.life) + " and experience = " + str(self.get_experience())



"Creating child class of 'Fighter', 'Cavalry' "
class Cavalry(Fighter[T]):

    # modifying inherited methods to give them implementation for Cavalry

    def __init__(self) -> None:
        # calling parent class with Cavalry's inputs for life and experience
            Fighter.__init__(self, 4, 0)


    def get_speed(self) -> int:
        """
        Gets the speed of the Cavalry.
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a getter method
        :return: speed of the fighter (int)
        """
        return 2


    def get_cost(self) -> int:
        """
        Gets cost of the Cavalry.
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a getter method
        :return: cost of the fighter (int)
        """
        return 3


    def attack_damage(self) -> int:
        """
        Calculates the amount of damage the Cavalry can have on attack
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a setter method
        :return: the amount of damage the fighter inflicts on attack (int)
        """
        return 1 + 2*self.get_experience()


    def defend(self, damage: int) -> None:
        """
        Calculates whether a life is lost after the Cavalry defends an attack.
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a setter method
        :param damage: the amount of damage the fighter has incurred due to defending an attack
        :return: None
        """
        # validate input damage by using a precondition
        if damage < 1:
            raise ValueError("Damage must be greater than or equal to zero")
        if damage > (self.experience/2):

            # decrement life by one after defence
            self.lose_life(1)


    def __str__(self) -> str:
        """
        Returns a string with the Cavalry and current life and experience
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a getter method
        :return: string with cavalry's current life and experience (str)
        """
        return "Cavalry's life = " + str(self.life) + " and experience = " + str(self.get_experience())



" Class 'Army' creates an army with an appropriate number of soldier, archers and cavalry. "
class Army:


    # declare constant variable for max expenditure
    BUDGET = 30


    def __init__(self) -> None:
        """
        Initialises the variables to None
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a setter method
        :return: None
        """
        # define instance variables
        self.name = None
        self.force = None


    def choose_army(self, name:str, formation: int) -> None:
        """
        Allows users to input the number of each type of fighter in the army
        Time Complexity:
        Best Case != Worst Case
        Best Case = 0(1) if the user inputs correct values the first time as only runs through once
        Worst Case = 0(n) where n is the amount of time the user inputs incorrect data
        :param name: name of user
        :param formation: 0 (stack formation) or 1 (circular queue formation)
        :return: None
        """

        # initially setting the input as not valid
        valid_army = False

        while not valid_army:
            # read input
            army_amount = input("Player " + name + "choose your army as S A C \n where S is the number of soldiers \n        A is the number of archers \n        C is the number of Cavalry")

        try:
            # split the string so that only its non spaced characters are kept and put in a list
            fighters = army_amount.split("")
            # assign each character to s, a and c whilst turning their type into int.
            s = int(fighters[0])
            a = int(fighters[1])
            c = int(fighters[2])
        except ValueError:
            print("Invalid Input. Try again!")
            valid_army = False
        except IndexError:
            print("Invalid Input. Try again!")
            valid_army = False
        else:
            #if three valid integers are entered, call internal method __correct_army_given with our inputs
            valid_army = self.__correct_army_given(s, a, c)

        # assign army if previous conditions are met or loop back to beginning of while loop
        if valid_army:
            self.__assign_army(name, s, a, c, formation)



    def __correct_army_given(self, soldiers:int, archers: int, cavalry: int) -> bool:
        """
        Checks that the input numbers meet the budget and are all greater than or equal to zero
        :param soldiers: number of soldiers in army
        :param archers: number of archers in army
        :param cavalry: number of cavalry in army
        :return: True/False
        Time Complexity:
        Best case = Worse Case
        0(1) as it only runs through once
        """
        # total price of the army
        total_cost = soldiers * Soldier().get_cost() + archers * Archer().get_cost()+ cavalry * Cavalry().get_cost()

        # returns true if Budget <=30 and all inputs are positive
        if soldiers < 0 or archers < 0 or cavalry < 0:
            return False
        elif total_cost > self.BUDGET:
            return False
        else:
            return True



    def __assign_army(self, name:str, sold: int, arch: int, cav: int, formation: int) -> None:
        """
        Creates a stack or circular queue with the members of the army in the correct order and binds the name and force variables
        :param name: name of user
        :param sold: number of soldiers in army
        :param arch: number of archers in army
        :param cav: number of cavalry in army
        :param formation: 0 (stack formation) or 1 (circular queue formation)
        Time Complexity:
        Best Case = Worst Case
        0(m+n+o) where m, n and o are the number of soldiers, archers and cavalry in the army.
        """
        # declare the total number of people in the army
        max_cap = sold + arch + cav

        # if player wants the army in stack formation
        if formation == 0:
            self.force = stack.ArrayStack(max_cap)
            # pushes the number of each element in formation (FIFO)
            for a in range(cav):
                self.force.push(Cavalry())
            for a in range(arch):
                self.force.push(Archer())
            for a in range(sold):
                self.force.push(Soldier())

        # if player wants the army in queue formation
        elif formation == 1:
            self.force = queue.CircularQueue(max_cap)
            # pushes the number of each element in formation (LIFO)
            for a in range(sold):
                self.force.append(Soldier())
            for a in range(arch):
                self.force.append(Archer())
            for a in range(cav):
                self.force.append(Cavalry())

        # binds variable
        self.name = name



    def __str__(self) -> str:
        """
        Returns a string of the life and experience of each army fighter
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a setter method
        :return: string with the current life and experience of all the fighters in the army.
        """
        army = self.force
        return str(army)