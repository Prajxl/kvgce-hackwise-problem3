from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
from waypoint_utils import read_waypoints, parse_waypoints_text
from tsp_solver import build_distance_matrix, nearest_neighbor, two_opt, calculate_path_cost

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/optimize', methods=['POST'])
def optimize():
    try:
        data = request.json
        waypoints_text = data.get('waypoints', '')
        
        # Parse waypoints from text input
        waypoints = parse_waypoints_text(waypoints_text)
        
        if not waypoints or len(waypoints) < 2:
            return jsonify({'error': 'Please provide at least 2 valid waypoints'}), 400
            
        coords = [(x, y, z) for _, x, y, z in waypoints]
        distance_matrix = build_distance_matrix(coords)
        initial_path = nearest_neighbor(distance_matrix)
        optimized_path, optimized_cost = two_opt(initial_path, distance_matrix)
        
        # Get the IDs for the optimized path
        path_ids = [waypoints[i][0] for i in optimized_path]
        
        # Get the full waypoints in optimized order
        ordered_waypoints = [waypoints[i] for i in optimized_path]
        
        return jsonify({
            'path': path_ids,
            'waypoints': ordered_waypoints,
            'cost': round(optimized_cost, 2),
            'success': True
        })
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500

if __name__ == '__main__':
    app.run(debug=True)