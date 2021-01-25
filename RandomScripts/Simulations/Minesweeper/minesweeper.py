'''
Minesweeper

CTCI Instructions:
Design and implement a txt-based Minesweeper game.
NxN grid has B mines hidden accross the grid.
Remaining cells either have number (how many bombs around them) 
    or are blank (meaning #bombs surrounding = 0)
Player uncovers cell:
    - if B, game over
    - if number, only reveal that cell
    - if blank, uncover area of blanks/nums touching it
        - idea: (could do this using BFS)
        - would start at blank clicked cell
        - if cell has not NOT beenVisited AND isBlank OR isNum
            - reveal the cell
        - push all sides in a queue
    - repeat for each neighbor, but if neighbor is a number then reveal number and return
    - User can also flag certain pieces as potential bombs
    - User wins when all NON-bomb cells are exposed
'''