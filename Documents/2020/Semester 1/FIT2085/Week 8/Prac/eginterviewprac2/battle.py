"""
Author: Elysia Giannis (29694736)

Battle class has methods which create two valid armies, conducts combat in stack/circular queue formation
and returns the outcome of the fight
This class is tested in test_task4.py and test_task5.py.
"""

# import files and classes needed
from abc import ABC, abstractmethod
from typing import TypeVar, Generic
T = TypeVar('T')
from army import Army


class Battle(ABC, Generic[T]):


    def __init__(self) -> None:
        """
        Initialise variables to none.
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it is a setter method
        :return: None
        """
        self.name = None
        self.force = None


    def gladiatorial_combat(self, player_one: str, player_two: str) -> int:
        """
        Creates army 1 and army 2 in stack formation
        Time Complexity:
        Best Case = Worst Case
        0(Comp_choose_army + Comp__conduct_combat) as the complexity is dependent on the complexity of the functions it calls.
        :param player_one: player name
        :param player_two: player name
        :return: Winner (0,1,2)
        """
        army1 = Army()
        army2 = Army()

        # calls to method choose_army to create a stack army
        army1.choose_army(player_one, 0)
        army2.choose_army(player_two, 0)

        return self.__conduct_combat(self, army1, army2, 0)


    def fairer_combat(self, player_one: str, player_two: str) -> int:
        """
        Creates army 1 and army 2 in circular queue formation
        Time Complexity:
        Best Case = Worst Case
        0(Comp_choose_army + Comp__conduct_combat) as the complexity is dependent on the complexity of the functions it calls.
        :param player_one: player name
        :param player_two: player name
        :return: Winner (0, 1, 2)
        """
        army1 = Army()
        army2 = Army()

        # calls to method choose_army to create a circular queue army
        army1.choose_army(player_one, 1)
        army2.choose_army(player_two, 1)

        return self.__conduct_combat(self, army1, army2, 1)


    def __conduct_combat(self, army1: Army, army2: Army, formation: int) -> int:
        """
        Conducts combat from the first fighters until the last in stack or queue formation
        Time Complexity:
        Best Case does not equal Worst Case
        Best Case: Both armies are empty, therefore, while loop doesn't run: 0(1)
        Worst Case: Armies have fighters : O(n*Comp_one_v_one_fight+Comp_winner),
        where n is the number of fights undertaken.
        :param army1: refers to player_one's army
        :param army2: refers to player_two's army
        :param formation: 0 (stack formation) and 1 (circular queue formation)
        :return: Winner (0, 1 ,2)
        """
        while len(army1.force) > 0 and len(army2.force) > 0:

            # determines whether to release fighters from the stack or circular queue
            if formation == 0:
                u1 = army1.force.pop()
                u2 = army2.force.pop()
            else:
                u1 = army1.force.serve()
                u2 = army2.force.serve()

            # calls to a method which initiates a fight between the two fighters
            self.one_v_one_fight(u1, u2)

            # determines if life should be lost, experience should be gained and
            # whether the player should be pushed/appended back onto the stack/circular queue
            if u1.is_alive() and u2.is_alive():
                u1.lose_life(1)
                u2.lose_life(1)
                if u1.is_alive() and u2.is_alive():
                    if formation == 0:
                        army1.force.push(u1)
                        army2.force.push(u2)
                    else:
                        army1.force.append(u1)
                        army2.force.append(u2)
                elif u1.is_alive():
                    if formation == 0:
                        army1.force.push(u1)
                    else:
                        army1.force.append(u1)
                    u1.gain_experience(1)
                elif u2.is_alive():
                    if formation == 0:
                        army2.force.push(u2)
                    else:
                        army2.force.append(u2)
                    u2.gain_experience(1)
            elif u1.is_alive():
                u1.gain_experience(1)
                if formation == 0:
                    army1.force.push(u1)
                else:
                    army1.force.append(u1)
            elif u2.is_alive():
                u2.gain_experience(1)
                if formation == 0:
                    army2.force.push(u2)
                else:
                    army2.force.append(u2)

        return self.winner(army1, army2)


    def one_v_one_fight(self, u1, u2) -> None:
        """
        Conducts a fight between two players dependent on speed, attack damage and defence.
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it will only go through the if statement once
        :param u1: popped/served fighter from army 1
        :param u2: popped/served fighter from army 2
        """
        if u1.get_speed() > u2.get_speed():
            u2.defend(u1.attack_damage())
            if u2.is_alive():
                u1.defend(u2.attack_damage())
        elif u2.get_speed() > u1.get_speed():
            u1.defend(u2.attack_damage())
            if u1.is_alive():
                u2.defend(u1.attack_damage())
        else:
            u1.defend(u2.attack_damage())
            u2.defend(u1.attack_damage())


    def winner(self, army1: Army, army2: Army) -> int:
        """
        Computes whether army 1 or army 2 or neither have won the fight based on the final length of their stack/queue
        :param army1:
        :param army2:
        :return: Winner (0,1,2)
        Time Complexity:
        Best case = Worst Case time complexity.
        0(1) as it will only go through the statement once
        """
        if len(army1.force) == 0 and len(army2.force) == 0:
            return 0
        elif len(army2.force) == 0:
            return 1
        else:
            return 2
