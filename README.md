# FictionalFightWorld
You are taken to a fictional world where among the ordinary people reside three ferocious kinds:
Fighters, Warriors, and Knight-Errants. Your job is to implement a few classes to simulate this
fictional world of these three classes of people in a way that honors the specified properties and
attributes. These three classes of people are, of course, Persons. By law, they are also required to
be Adults (<= 18 years old).
2.1 A Person
A Person is required to have a name: str and age: int. They may optionally also have wealth: int.
Depending on the age, each person is (or isn't) an adult. The default creation of a new person
creates a non-adult with zero wealth. For this assignment, you may assume that the name-plus-age
combination uniquely identies a person.

2.2 A Fighter
A Fighter is an adult person who has some positive wealth and a set of skills. Of course, just
having a skill doesn't mean that the ghter has perfected it, so a skill is associated with a level,
which is a score between 0 and 10. The skill details of each ghter must be private.

2.2.1 Skills
There are four types of skills { spear, unarmed combat, mace, and broadsword. A fighter's complete
skillset may be represented as a set of mappings of skills to levels. A fighter who is an expert with
the spear but has no other skills could, for example, have their skills represented by {spear: 10,
unarmed combat: 0, mace: 0, broadsword: 0}

2.2.2 Fight Rules
A Fighter a can invoke a challenge(...) to fight another fighter b. The challenge must also
specify the skill to be used.
1. A Fight can only happen between two fighters, and a fighter cannot fight themselves!
2. A Fighter also cannot enter into a fight (as a challenger or as the recipient of a challenge) if
their wealth is zero.
3. Only one skill may be used in a fight. If b is able to, s/he will accept the challenge immediately.
4. The outcome of the challenge is a winner, determined by which fighter has a higher level
of the chosen skill. If both a and b have the same level, the winner is determined by luck
(see random.choice). Otherwise, the fighter with higher skill level wins. The winner gains
10 wealth points, and the loser forfeits 10 wealth points (restricted to a minimum of zero
points)1.
5. Each fight also provides a random chance for each participating fighter to add 1 point to their
skill level (for the skill chosen in that fight), subject to the maximum limit of 10.
6. Of course, if fighters openly knew each others skill levels, they would only fight weaker oppo-
nents to keep earning money, since the opponent can't decline a challenge. This is why these
details were required to be made private in Sec. 2.2.

2.3 A Warrior
A warrior \is-a" fighter with some additional freedoms. A warrior can keep a list of challenge
requests from other fighters, and can accept or decline each request. A warrior may also simply
leave requests unanswered. However, if a fighter issues a challenge to a warrior, but then ends up
fighting someone else before this warrior accepts the request, the fighter has the right to withdraw
the request (e.g., the fighter may have suffered an injury in this fight, and cannot fight the warrior
any more).
1. If an ordinary fighter wins against a warrior, they attain 25 wealth points. They also increase
their skill level by one (with certainty, no randomness this time).
2. If a warrior loses against an ordinary fighter, they forfeit 25 wealth points (restricted to a
minimum of zero points) and gain no additional skill from the fight they lost.
3. For any remaining scenarios, the property that a warrior \is-a" fighter should be used to
determine the outcome. That is, if two warriors fight each other, you should use the properties
of the base class Fighter and the fight rules in Sec. 2.2.2.

2.4 A Knight-Errant
A knight errant \is-a" warrior, but often has better things to do! For instance, they travel a lot.
Therefore, at any given point of time, a knight errant may be traveling or not.
1. When a knight-errant is traveling, he cannot challenge another fighter. Nor can he accept a
challenge. Others can, however, leave challenge requests during this time.
2. A knight-errant can sometimes nd treasures when they are traveling. This treasure's worth
(in terms of amount of wealth) gets added to the knight-errant's wealth when they return
from a travel.
3. If an ordinary fighter wins against a knight-errant, s/he gains 40 wealth points and 2 skill
levels.
4. If a warrior wins agains a knight-errant, s/he gains 20 wealth points and 1 skill level.
5. If a knight-errant loses against an ordinary fighter, he loses 40 wealth points. And similarly,
if he loses against a warrior, he loses 20 wealth points. He also does not gain any skill.
6. For any remaining scenarios, you should use the fact that a knight-errant \is-a" warrior, and
therefore, \is-a" fighter (just like point 3 in Sec. 2.3).

3 Tasks
In this assignment, you are required to implement three classes for the three types of ghters:
Fighter, Warrior, and KnightErrant, and the base Person class. Further, a class Fight also must
be implemented. The fictional world has already been described above, and your implementation
must honor all those specifications. To provide some guidance, a partial API and class denition
is provided below:
3.1 Person
 Attributes for name, age, wealth, and whether or not the person is an adult.
 Methods to check whether or not two person instances are equal.
3.2 Fight
 Two attributes for the two fighters in a fight.
 A method called winner() that returns the winner of the fight.
3.3 Fighter
 A method challenge(...) and returns None. This method must carry out the responsibility
of ensuring that all the rules of a challenge are observed (e.g., wealth change, skill change,
whether or not the challenge can even be issued and/or accepted, etc.). [Note that you may
have to override this method in some other classes.]
 A method withdraw(...) to withdraw a challenge request s/he issued.
3.4 Warrior
 A method accept random(...) that accepts a random challenge from the list of challenges.
 A method decline random(...) that declines a random challenge from the list of challenges.
 Has similar methods accept first(...) and decline first(...).
3.5 KnightErrant
 A method travel(...) to mark the beginning of a journey.
 A method return(...) to mark the return from a journey. This method must implement
any treasure-related activities.
