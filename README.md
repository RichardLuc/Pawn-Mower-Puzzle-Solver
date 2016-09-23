# Pawn-Mower-Puzzle-Solver
A program that solves chess pawn mower puzzles. It is made with python. It uses the idea of depth-first search to solve puzzles.

# Instructions
Lookup pawn mower chess puzzles before using this script.  
First type in the number of pawns in the puzzle. Second, type in the coordinates of each pawns. Third, type in the piece you are controlling. Fourth, type in the coordinates of said piece.

# Initial Goals From Finishing This Project
- Keep myself busy so I won't get rusty [x]

# What I Learned
In this project I learned about different methods to search through a graph or a tree. I implemented a breadth-first search algorithm in my code.  
It is possible to return two variables from a function at once.

# Things I Can Improve On/ Do In The Future
Do version control and backup my saves more often. I almost my files for this project.  
Name my variables better. I got confused by some of my variables and that slowed down progress.

# Thought Process Throughout The Project
1. I wanted to work on a project to keep my programming skills sharp. I came across an interesting type of chess puzzle on Reddit called pawn mower puzzles. I decided to work on a script that solves those puzzles.  
2. I started by making a few functions I know that are going to be important. After that, I worked on placing pieces onto a chessboard.
3. Once the pieces are placed I made a function to move the pieces. 
4. I decided to move the controlling piece randomly. My initial idea was to use python's quick processing power to hopefully receive a solution to the puzzle.
5. The random movements of the piece works great on simple puzzles, but the time it took to solve a puzzle with 8+ pawns increases exponentially. Sometimes the script was unable to solve large puzzles.
6. I deleted my bad code and started researching how to create a puzzle solver. I was unable to find any information about creating a puzzle solver so I looked at my problem in a different perspective. I visualized pawn mower puzzles as a maze. I thought that whenever the controlling piece cannot eat a pawn, then that direction is a dead end.
7. I researched on how programs solve randomly generated mazes. I learned that those programs use algorithms to search through a tree.
8. I immediately started to work on my code again. I used the breadth-first search algorithm to find the solution of the puzzle and it worked out great.

# Time It Took To Complete This Project
Less than a week
