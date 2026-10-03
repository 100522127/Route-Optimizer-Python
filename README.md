# A* Route Optimizer & Custom Priority Queue

## What is this project?
A pathfinding engine developed completely from scratch in Python that finds the shortest path in large-scale road maps. It implements the A* and Dijkstra algorithms to handle massive graphs without relying on any third-party libraries for the search logic or data structures.

## Key Features
* **Native Data Structures:** Manual implementation of an Open List using a priority queue (Min-Heap) with custom reordering algorithms (`_subir` and `_bajar`) based on the $f(n)$ function.
* **Dual Search Mode:** Ability to run the A* algorithm guided by a heuristic, or switch at runtime to a "brute force" mode (Dijkstra) where the heuristic is nullified ($h=0$).
* **Precise Geographic Heuristic:** Calculation of the Euclidean distance by converting geodetic coordinates to exact meters, using a conversion factor of 111320 meters per degree and adjusting the longitude based on the average latitude.
* **Massive Data Parsing:** Efficient loading of graph topology through `.gr` files (adjacencies and edge costs) and `.co` files (spatial coordinates).
* **Integrated Benchmarking:** Real-time performance calculations, reporting the total number of node expansions, total execution time, and the rate of nodes processed per second.

## Tech Stack
* **Language:** Python 3 (No external libraries used for the core logic, relying exclusively on native modules like `math`, `sys`, and `time`).
* **Architecture:** Object-Oriented Design (Graph, Open List, Closed List, Algorithm).

## Installation and Usage
1. Clone this repository.
2. Run the main script passing the following arguments: source node, target node, map file prefix, and output file name.
