# Maze Solver

This project provides a Python-based solution for solving mazes using **Breadth-First Search (BFS)**. The maze is represented as an image, where the robot navigates from an entrance to an exit. The solution includes visualization of the shortest path, marking key points such as the start, end, and the traversed route.

---

## Output Image
![Alt text](https://github.com/alam121/Maze_Challenge/blob/main/output.png)

## Features

- Identifies the **start** and **end** points of the maze.
- Computes the shortest path using BFS.
- Visualizes the solution with:
  - **Red dot**: Start point.
  - **Blue dot**: End point.
  - **Green path**: Shortest path through the maze.
- Handles a variety of maze structures provided as image files.

---

## Prerequisites

Ensure you have Python installed (version 3.7+ recommended). You will also need the following Python libraries:

- `Pillow`
- `numpy`
- `matplotlib`

Install them using the following command:
```
pip install pillow numpy matplotlib


## How to Run

Follow these steps to run the maze solver:

### Clone the Repository, Open your terminal and clone the repository using:

git clone https://github.com/alam121/Maze_Challenge.git
cd maze_solver
```
Place your maze image in the project folder.

Ensure the image follows these requirements:
- Black pixels (0) represent walls.
- White pixels (255) represent paths

## Run the Script
Execute the script by running:

```bash
python Maze_Challenge.py
```
## View the Result
The script will process the maze and display the following:

- A red dot marking the start point.
- A blue dot marking the end point.
- A green path representing the shortest path from the start to the end.

