"""

[2019-02-15] Challenge #375 [Hard] Graph of Thrones
Description
We'll focus in this challenge on what's called a complete graph,
wherein every node is expressly connected to every other node.
We'll also work assuming an undirected graph, that relationships are reciprocal.

In social network analysis, you can analyze for structural balance -
a configuration wherein you'll find local stability.
The easy one is when everyone enjoys a positive relationship with everyone else - they're all friends.
Another structurally balanced scenario is when you have -
in a graph of three nodes - two friends and each with a shared enemy,
so one positive relationship and two negative ones.

With larger graphs,
you can continue this analysis by analyzing every three node subgraph and ensuring it has those properties -
all positive or one positive and two negative relationsgips.

A structurally balanced graph doesn't indicate complete future stability, just local stability -
remember, factions can arise in these networks, akin to the Axis and Allies scenario of WW1 and WW2.

Today's challenge is to take a graph and identify if the graph is structurally balanced.
This has great applicability to social network analysis,
and can easily be applied to stuff like fictional universes like the Game of Thrones
and the real world based on news events.

Example Input
You'll be given a graph in the following format:
the first line contains two integers, N and M, telling you how many nodes and edges to load, respectively.
The next M lines tell you relationships, positive (friendly, denoted by ++) or negative (foes, denoted by --).

Example (from a subset of the Legion of Doom and Justice League):

6 15
Superman ++ Green Lantern
Superman ++ Wonder Woman
Superman -- Sinestro
Superman -- Cheetah
Superman -- Lex Luthor
Green Lantern ++ Wonder Woman
Green Lantern -- Sinestro
Green Lantern -- Cheetah
Green Lantern -- Lex Luthor
Wonder Woman -- Sinestro
Wonder Woman -- Cheetah
Wonder Woman -- Lex Luthor
Sinestro ++ Cheetah
Sinestro ++ Lex Luthor
Cheetah ++ Lex Luthor
Example Output
Your program should emit if the graph is structurally balanced or not. Example:

balanced
Challenge Input
This is the Game of Thrones Season 7 house list I found via this list of alliances on the Vulture website -
I don't watch GoT so I have no idea if I captured this right.

120 16
Daenerys Targaryen ++ Jon Snow
Daenerys Targaryen ++ Tyrion Lannister
Daenerys Targaryen ++ Varys
Daenerys Targaryen ++ Jorah Mormont
Daenerys Targaryen ++ Beric Dondarrion
Daenerys Targaryen ++ Sandor “the Hound” Clegane
Daenerys Targaryen ++ Theon and Yara Greyjoy
Daenerys Targaryen -- Sansa Stark
Daenerys Targaryen -- Arya Stark
Daenerys Targaryen -- Bran Stark
Daenerys Targaryen -- The Lords of the North and the Vale
Daenerys Targaryen -- Littlefinger
Daenerys Targaryen -- Cersei Lannister
Daenerys Targaryen -- Jaime Lannister
Daenerys Targaryen -- Euron Greyjoy
Jon Snow ++ Tyrion Lannister
Jon Snow ++ Varys
Jon Snow ++ Jorah Mormont
Jon Snow ++ Beric Dondarrion
Jon Snow ++ Sandor “the Hound” Clegane
Jon Snow -- Theon and Yara Greyjoy
Jon Snow -- Sansa Stark
Jon Snow -- Arya Stark
Jon Snow -- Bran Stark
Jon Snow -- The Lords of the North and the Vale
Jon Snow -- Littlefinger
Jon Snow -- Cersei Lannister
Jon Snow -- Jaime Lannister
Jon Snow -- Euron Greyjoy
Tyrion Lannister ++ Varys
Tyrion Lannister ++ Jorah Mormont
Tyrion Lannister ++ Beric Dondarrion
Tyrion Lannister ++ Sandor “the Hound” Clegane
Tyrion Lannister ++ Theon and Yara Greyjoy
Tyrion Lannister -- Sansa Stark
Tyrion Lannister -- Arya Stark
Tyrion Lannister -- Bran Stark
Tyrion Lannister -- The Lords of the North and the Vale
Tyrion Lannister -- Littlefinger
Tyrion Lannister -- Cersei Lannister
Tyrion Lannister -- Jaime Lannister
Tyrion Lannister -- Euron Greyjoy
Varys ++ Jorah Mormont
Varys ++ Beric Dondarrion
Varys ++ Sandor “the Hound” Clegane
Varys ++ Theon and Yara Greyjoy
Varys -- Sansa Stark
Varys -- Arya Stark
Varys -- Bran Stark
Varys -- The Lords of the North and the Vale
Varys -- Littlefinger
Varys -- Cersei Lannister
Varys -- Jaime Lannister
Varys -- Euron Greyjoy
Jorah Mormont ++ Beric Dondarrion
Jorah Mormont ++ Sandor “the Hound” Clegane
Jorah Mormont ++ Theon and Yara Greyjoy
Jorah Mormont -- Sansa Stark
Jorah Mormont -- Arya Stark
Jorah Mormont -- Bran Stark
Jorah Mormont -- The Lords of the North and the Vale
Jorah Mormont -- Littlefinger
Jorah Mormont -- Cersei Lannister
Jorah Mormont -- Jaime Lannister
Jorah Mormont -- Euron Greyjoy
Beric Dondarrion ++ Sandor “the Hound” Clegane
Beric Dondarrion ++ Theon and Yara Greyjoy
Beric Dondarrion -- Sansa Stark
Beric Dondarrion -- Arya Stark
Beric Dondarrion -- Bran Stark
Beric Dondarrion -- The Lords of the North and the Vale
Beric Dondarrion -- Littlefinger
Beric Dondarrion -- Cersei Lannister
Beric Dondarrion -- Jaime Lannister
Beric Dondarrion -- Euron Greyjoy
Sandor “the Hound” Clegane ++ Theon and Yara Greyjoy
Sandor “the Hound” Clegane -- Sansa Stark
Sandor “the Hound” Clegane -- Arya Stark
Sandor “the Hound” Clegane -- Bran Stark
Sandor “the Hound” Clegane -- The Lords of the North and the Vale
Sandor “the Hound” Clegane -- Littlefinger
Sandor “the Hound” Clegane -- Cersei Lannister
Sandor “the Hound” Clegane -- Jaime Lannister
Sandor “the Hound” Clegane -- Euron Greyjoy
Theon and Yara Greyjoy -- Sansa Stark
Theon and Yara Greyjoy -- Arya Stark
Theon and Yara Greyjoy -- Bran Stark
Theon and Yara Greyjoy -- The Lords of the North and the Vale
Theon and Yara Greyjoy -- Littlefinger
Theon and Yara Greyjoy -- Cersei Lannister
Theon and Yara Greyjoy -- Jaime Lannister
Theon and Yara Greyjoy -- Euron Greyjoy
Sansa Stark ++ Arya Stark
Sansa Stark ++ Bran Stark
Sansa Stark ++ The Lords of the North and the Vale
Sansa Stark ++ Littlefinger
Sansa Stark -- Cersei Lannister
Sansa Stark -- Jaime Lannister
Sansa Stark -- Euron Greyjoy
Arya Stark ++ Bran Stark
Arya Stark ++ The Lords of the North and the Vale
Arya Stark ++ Littlefinger
Arya Stark -- Cersei Lannister
Arya Stark -- Jaime Lannister
Arya Stark -- Euron Greyjoy
Bran Stark ++ The Lords of the North and the Vale
Bran Stark -- Littlefinger
Bran Stark -- Cersei Lannister
Bran Stark -- Jaime Lannister
Bran Stark -- Euron Greyjoy
The Lords of the North and the Vale ++ Littlefinger
The Lords of the North and the Vale -- Cersei Lannister
The Lords of the North and the Vale -- Jaime Lannister
The Lords of the North and the Vale -- Euron Greyjoy
Littlefinger -- Cersei Lannister
Littlefinger -- Jaime Lannister
Littlefinger -- Euron Greyjoy
Cersei Lannister ++ Jaime Lannister
Cersei Lannister ++ Euron Greyjoy
Jaime Lannister ++ Euron Greyjoy
"""


def solution(data):
    """
    solution~ seems to get the correct result. most of the code just formats the text into a nice nxn matrix,
    to make the comparison less annoying!
    the for i for j for k bit just compares if any combination of i < j < k exists such that the sum of our 'edges'
    (denoted 1 for positive and -1 for negative) for subgraph of 3 nodes is always either 3 (all positive)
    or -1 (2 neg, 1 pos).

    :param data: a big'ol chunk of text. see task for format details.
    :return:
    """
    lines = data.splitlines()
    n = 0
    m = 0
    names = []
    connections = 0
    for i in range(len(lines)):
        if i == 0:
            temp = lines[i].split(' ')
            # input N and M were swapped in the task, so I just set n to be the smaller and m the larger number
            m = max(int(temp[1]), int(temp[0]))
            n = min(int(temp[1]), int(temp[0]))
            if n < 3:
                raise ValueError("Graph too small. Need at least 3 Nodes.")
            connections = [[None for x in range(n)] for y in range(n)]
            continue
        if i > m:
            break
        sub = lines[i].split(' ')
        pre = ''
        val = 0
        post = ''
        for item in sub:
            # recognize ++ and --, merge everything before/after ++/-- into 1 string each
            if val == 0:
                if item not in ['++', '--']:
                    pre += (' ' if pre != '' else '') + item
                else:
                    if item == '++':
                        val = 1
                    else:
                        val = -1
            else:
                post += (' ' if post != '' else '') + item
        # list all names
        if pre not in names:
            names.append(pre)
        if post not in names:
            names.append(post)
        # update values 1 / -1 in matrix based on ++ / --
        # None elements are just placeholders, so this warning can be ignored.
        connections[names.index(pre)][names.index(post)] = val
        print(names)
        for vec in connections:
            print(vec)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # ACTUAL COMPARISON STARTS HERE!
    for i in range(len(connections)):
        for j in range(i+1, len(connections)):
            for k in range(j+1, len(connections)):
                # 1 + 1 + 1 = 3, 1 - 1 - 1 = -1, thus the sum of 3 edges in a circle must always be in [3, -1]
                if connections[i][j] + connections[j][k] + connections[i][k] not in [3, -1]:
                    print("unbalanced")
                    return
    # if nothing was returned as unbalanced yet, it's balanced.
    print("balanced")
    return


def example_input():
    """
    example gets the correct result! (balanced)

    :return:
    """
    solution("6 15\n"
             "Superman ++ Green Lantern\n"
             "Superman ++ Wonder Woman\n"
             "Superman -- Sinestro\n"
             "Superman -- Cheetah\n"
             "Superman -- Lex Luthor\n"
             "Green Lantern ++ Wonder Woman\n"
             "Green Lantern -- Sinestro\n"
             "Green Lantern -- Cheetah\n"
             "Green Lantern -- Lex Luthor\n"
             "Wonder Woman -- Sinestro\n"
             "Wonder Woman -- Cheetah\n"
             "Wonder Woman -- Lex Luthor\n"
             "Sinestro ++ Cheetah\n"
             "Sinestro ++ Lex Luthor\n"
             "Cheetah ++ Lex Luthor")


def challenge_input():
    """
    Challenge gets the correct result, too! (unbalanced)

    :return:
    """
    solution("120 16\n"
             "Daenerys Targaryen ++ Jon Snow\n"
             "Daenerys Targaryen ++ Tyrion Lannister\n"
             "Daenerys Targaryen ++ Varys\n"
             "Daenerys Targaryen ++ Jorah Mormont\n"
             "Daenerys Targaryen ++ Beric Dondarrion\n"
             "Daenerys Targaryen ++ Sandor “the Hound” Clegane\n"
             "Daenerys Targaryen ++ Theon and Yara Greyjoy\n"
             "Daenerys Targaryen -- Sansa Stark\n"
             "Daenerys Targaryen -- Arya Stark\n"
             "Daenerys Targaryen -- Bran Stark\n"
             "Daenerys Targaryen -- The Lords of the North and the Vale\n"
             "Daenerys Targaryen -- Littlefinger\n"
             "Daenerys Targaryen -- Cersei Lannister\n"
             "Daenerys Targaryen -- Jaime Lannister\n"
             "Daenerys Targaryen -- Euron Greyjoy\n"
             "Jon Snow ++ Tyrion Lannister\n"
             "Jon Snow ++ Varys\n"
             "Jon Snow ++ Jorah Mormont\n"
             "Jon Snow ++ Beric Dondarrion\n"
             "Jon Snow ++ Sandor “the Hound” Clegane\n"
             "Jon Snow -- Theon and Yara Greyjoy\n"
             "Jon Snow -- Sansa Stark\n"
             "Jon Snow -- Arya Stark\n"
             "Jon Snow -- Bran Stark\n"
             "Jon Snow -- The Lords of the North and the Vale\n"
             "Jon Snow -- Littlefinger\n"
             "Jon Snow -- Cersei Lannister\n"
             "Jon Snow -- Jaime Lannister\n"
             "Jon Snow -- Euron Greyjoy\n"
             "Tyrion Lannister ++ Varys\n"
             "Tyrion Lannister ++ Jorah Mormont\n"
             "Tyrion Lannister ++ Beric Dondarrion\n"
             "Tyrion Lannister ++ Sandor “the Hound” Clegane\n"
             "Tyrion Lannister ++ Theon and Yara Greyjoy\n"
             "Tyrion Lannister -- Sansa Stark\n"
             "Tyrion Lannister -- Arya Stark\n"
             "Tyrion Lannister -- Bran Stark\n"
             "Tyrion Lannister -- The Lords of the North and the Vale\n"
             "Tyrion Lannister -- Littlefinger\n"
             "Tyrion Lannister -- Cersei Lannister\n"
             "Tyrion Lannister -- Jaime Lannister\n"
             "Tyrion Lannister -- Euron Greyjoy\n"
             "Varys ++ Jorah Mormont\n"
             "Varys ++ Beric Dondarrion\n"
             "Varys ++ Sandor “the Hound” Clegane\n"
             "Varys ++ Theon and Yara Greyjoy\n"
             "Varys -- Sansa Stark\n"
             "Varys -- Arya Stark\n"
             "Varys -- Bran Stark\n"
             "Varys -- The Lords of the North and the Vale\n"
             "Varys -- Littlefinger\n"
             "Varys -- Cersei Lannister\n"
             "Varys -- Jaime Lannister\n"
             "Varys -- Euron Greyjoy\n"
             "Jorah Mormont ++ Beric Dondarrion\n"
             "Jorah Mormont ++ Sandor “the Hound” Clegane\n"
             "Jorah Mormont ++ Theon and Yara Greyjoy\n"
             "Jorah Mormont -- Sansa Stark\n"
             "Jorah Mormont -- Arya Stark\n"
             "Jorah Mormont -- Bran Stark\n"
             "Jorah Mormont -- The Lords of the North and the Vale\n"
             "Jorah Mormont -- Littlefinger\n"
             "Jorah Mormont -- Cersei Lannister\n"
             "Jorah Mormont -- Jaime Lannister\n"
             "Jorah Mormont -- Euron Greyjoy\n"
             "Beric Dondarrion ++ Sandor “the Hound” Clegane\n"
             "Beric Dondarrion ++ Theon and Yara Greyjoy\n"
             "Beric Dondarrion -- Sansa Stark\n"
             "Beric Dondarrion -- Arya Stark\n"
             "Beric Dondarrion -- Bran Stark\n"
             "Beric Dondarrion -- The Lords of the North and the Vale\n"
             "Beric Dondarrion -- Littlefinger\n"
             "Beric Dondarrion -- Cersei Lannister\n"
             "Beric Dondarrion -- Jaime Lannister\n"
             "Beric Dondarrion -- Euron Greyjoy\n"
             "Sandor “the Hound” Clegane ++ Theon and Yara Greyjoy\n"
             "Sandor “the Hound” Clegane -- Sansa Stark\n"
             "Sandor “the Hound” Clegane -- Arya Stark\n"
             "Sandor “the Hound” Clegane -- Bran Stark\n"
             "Sandor “the Hound” Clegane -- The Lords of the North and the Vale\n"
             "Sandor “the Hound” Clegane -- Littlefinger\n"
             "Sandor “the Hound” Clegane -- Cersei Lannister\n"
             "Sandor “the Hound” Clegane -- Jaime Lannister\n"
             "Sandor “the Hound” Clegane -- Euron Greyjoy\n"
             "Theon and Yara Greyjoy -- Sansa Stark\n"
             "Theon and Yara Greyjoy -- Arya Stark\n"
             "Theon and Yara Greyjoy -- Bran Stark\n"
             "Theon and Yara Greyjoy -- The Lords of the North and the Vale\n"
             "Theon and Yara Greyjoy -- Littlefinger\n"
             "Theon and Yara Greyjoy -- Cersei Lannister\n"
             "Theon and Yara Greyjoy -- Jaime Lannister\n"
             "Theon and Yara Greyjoy -- Euron Greyjoy\n"
             "Sansa Stark ++ Arya Stark\n"
             "Sansa Stark ++ Bran Stark\n"
             "Sansa Stark ++ The Lords of the North and the Vale\n"
             "Sansa Stark ++ Littlefinger\n"
             "Sansa Stark -- Cersei Lannister\n"
             "Sansa Stark -- Jaime Lannister\n"
             "Sansa Stark -- Euron Greyjoy\n"
             "Arya Stark ++ Bran Stark\n"
             "Arya Stark ++ The Lords of the North and the Vale\n"
             "Arya Stark ++ Littlefinger\n"
             "Arya Stark -- Cersei Lannister\n"
             "Arya Stark -- Jaime Lannister\n"
             "Arya Stark -- Euron Greyjoy\n"
             "Bran Stark ++ The Lords of the North and the Vale\n"
             "Bran Stark -- Littlefinger\n"
             "Bran Stark -- Cersei Lannister\n"
             "Bran Stark -- Jaime Lannister\n"
             "Bran Stark -- Euron Greyjoy\n"
             "The Lords of the North and the Vale ++ Littlefinger\n"
             "The Lords of the North and the Vale -- Cersei Lannister\n"
             "The Lords of the North and the Vale -- Jaime Lannister\n"
             "The Lords of the North and the Vale -- Euron Greyjoy\n"
             "Littlefinger -- Cersei Lannister\n"
             "Littlefinger -- Jaime Lannister\n"
             "Littlefinger -- Euron Greyjoy\n"
             "Cersei Lannister ++ Jaime Lannister\n"
             "Cersei Lannister ++ Euron Greyjoy\n"
             "Jaime Lannister ++ Euron Greyjoy\n")


if __name__ == '__main__':
    # example_input()
    challenge_input()
