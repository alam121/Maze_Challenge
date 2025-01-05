from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

class MazeSolver:
    def __init__(self, image_path):
        self.image_path = image_path
        self.maze_image = Image.open(image_path)
        self.maze_gray = self.maze_image.convert("L")
        self.maze_array = np.array(self.maze_gray)

    def find_point(self, rows_to_scan, from_top=True):
        """
        Finds a point in the maze based on scanning rows.
        :param rows_to_scan: Number of rows to scan.
        :param from_top: If True, scans from the top; otherwise, from the bottom.
        :return: Coordinates of the point or None if not found.
        """
        if from_top:
            row_range = range(rows_to_scan)  # Scan from top
        else:
            row_range = range(self.maze_array.shape[0] - 1, self.maze_array.shape[0] - rows_to_scan - 1, -1)  # Bottom up

        black_pixel = None
        for y in row_range:
            for x in range(self.maze_array.shape[1]):
                if self.maze_array[y, x] == 0:  # Black pixel
                    black_pixel = (x, y)
                    break
            if black_pixel:
                break

        if black_pixel:
            black_x, black_y = black_pixel
            consecutive_white_count = 0
            for x in range(black_x, self.maze_array.shape[1]):
                if self.maze_array[black_y, x] == 255:  # White pixel
                    consecutive_white_count += 1
                    if consecutive_white_count == 5:  # Found 5 consecutive white pixels
                        return (x - 4, black_y)
                else:
                    consecutive_white_count = 0
        return None

    def bfs_pathfinding(self, start, end):
        """
        Performs BFS to find the shortest path from start to end.
        :param start: Starting point coordinates.
        :param end: Ending point coordinates.
        :return: List of coordinates representing the path.
        """
        rows, cols = self.maze_array.shape
        queue = deque([start])
        visited = set()
        visited.add(start)
        parent = {}

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        while queue:
            current = queue.popleft()
            if current == end:
                break

            for dx, dy in directions:
                x, y = current
                nx, ny = x + dx, y + dy

                if (0 <= nx < cols and 0 <= ny < rows and
                        self.maze_array[ny, nx] == 255 and (nx, ny) not in visited):
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    parent[(nx, ny)] = current

        path = []
        current = end
        while current in parent:
            path.append(current)
            current = parent[current]
        path.reverse()
        return path

    def solve_and_display(self):
        """
        Solves the maze and displays the solution.
        """
        start_point = self.find_point(rows_to_scan=10, from_top=True)
        end_point = self.find_point(rows_to_scan=10, from_top=False)

        if start_point and end_point:
            print(f"Starting Point: {start_point}")
            print(f"Ending Point: {end_point}")
            path = self.bfs_pathfinding(start_point, end_point)

            maze_rgb = self.maze_image.convert("RGB")
            draw = ImageDraw.Draw(maze_rgb)

            # Mark the path with darker and larger green pixels
            for x, y in path:
                draw.ellipse((x - 1, y - 1, x + 1, y + 1), fill="darkgreen")

            # Mark the start and end points with darker and larger dots
            sx, sy = start_point
            ex, ey = end_point
            draw.ellipse((sx - 3, sy - 3, sx + 3, sy + 3), fill="darkred")
            draw.ellipse((ex - 3, ey - 3, ex + 3, ey + 3), fill="darkblue")

            plt.figure(figsize=(8, 8))
            plt.title("Path from Start to End")
            plt.imshow(maze_rgb)
            plt.axis("off")
            plt.show()
        else:
            print("Could not determine the starting or ending points!")

# Usage
if __name__ == "__main__":
    maze_solver = MazeSolver('maze.png')  # Replace 'maze.png' with your maze file
    maze_solver.solve_and_display()
