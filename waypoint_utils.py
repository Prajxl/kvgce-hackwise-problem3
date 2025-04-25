def read_waypoints(filename):
    """Read waypoints from a file"""
    waypoints = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 4:
                try:
                    waypoint_id = parts[0]
                    x, y, z = map(float, parts[1:])
                    waypoints.append((waypoint_id, x, y, z))
                except ValueError:
                    pass  # Skip malformed lines
    return waypoints

def parse_waypoints_text(text):
    """Parse waypoints from text input"""
    waypoints = []
    for line in text.strip().split('\n'):
        parts = line.strip().split()
        if len(parts) == 4:
            try:
                waypoint_id = parts[0]
                x, y, z = map(float, parts[1:])
                waypoints.append((waypoint_id, x, y, z))
            except ValueError:
                pass  # Skip malformed lines
    return waypoints