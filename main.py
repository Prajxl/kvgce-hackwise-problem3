from waypoint_utils import read_waypoints
from tsp_solver import build_distance_matrix, nearest_neighbor, two_opt, calculate_path_cost
import os

def main():
    input_file = "waypoints.txt"
    waypoints = read_waypoints(input_file)
    coords = [(x, y, z) for _, x, y, z in waypoints]
    distance_matrix = build_distance_matrix(coords)
    initial_path = nearest_neighbor(distance_matrix)
    optimized_path, optimized_cost = two_opt(initial_path, distance_matrix)
    path_ids = [waypoints[i][0] for i in optimized_path]
    
    # Print to console (keep existing functionality)
    print("Optimized Path:", " → ".join(map(str, path_ids)))
    print(f"Total Fuel Cost: {optimized_cost:.2f} units")
    
    # Write the results to sample_output/path.txt using ASCII characters instead of Unicode
    output_path = os.path.join("sample_output", "path.txt")
    with open(output_path, "w") as f:
        f.write("Optimized Path: " + " -> ".join(map(str, path_ids)) + "\n")
        f.write(f"Total Fuel Cost: {optimized_cost:.2f} units\n")
        
        # Optional: Include detailed waypoint information
        f.write("\nDetailed Waypoint Information:\n")
        for idx in optimized_path:
            waypoint = waypoints[idx]
            f.write(f"Waypoint {waypoint[0]}: ({waypoint[1]:.2f}, {waypoint[2]:.2f}, {waypoint[3]:.2f})\n")

if __name__ == "__main__":
    main()