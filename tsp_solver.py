import math

def calculate_distance(p1, p2):
    """Calculate Euclidean distance between two 3D points"""
    dx, dy, dz = p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]
    return math.sqrt(dx*dx + dy*dy + dz*dz)

def build_distance_matrix(coords):
    """Build a distance matrix from a list of coordinates"""
    n = len(coords)
    return [[calculate_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

def calculate_path_cost(path, matrix):
    """Calculate the total cost of a path using the distance matrix"""
    return sum(matrix[path[i]][path[i+1]] for i in range(len(path)-1))

def nearest_neighbor(distance_matrix):
    """Implementation of the Nearest Neighbor algorithm for TSP"""
    n = len(distance_matrix)
    unvisited = set(range(1, n))
    path = [0]
    current = 0
    while unvisited:
        next_city = min(unvisited, key=lambda j: distance_matrix[current][j])
        path.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    path.append(0)  # Return to start
    return path

def two_opt(path, matrix, max_iter=1000):
    """Implementation of the 2-opt optimization algorithm for TSP"""
    best = path[:]
    best_cost = calculate_path_cost(best, matrix)
    improved = True
    while improved and max_iter > 0:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i+1, len(best) - 1):
                new_path = best[:i] + best[i:j+1][::-1] + best[j+1:]
                new_cost = calculate_path_cost(new_path, matrix)
                if new_cost < best_cost:
                    best = new_path
                    best_cost = new_cost
                    improved = True
                    break
            if improved:
                break 
        max_iter -= 1
    return best, best_cost