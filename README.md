
🛰️ Space Mission Waypoint Optimizer
===================================

This project finds the most fuel-efficient path through a set of 3D waypoints 
using classical TSP (Traveling Salesman Problem) heuristics. It's designed with 
space mission planning in mind, where each segment of travel has cost implications.

🚀 Features
-----------
📦 Parses 3D waypoints from a file or web form  
📊 Builds a 3D distance matrix for all waypoints  
🔁 Generates an initial path using Nearest Neighbor  
✨ Optimizes the path using the 2-Opt algorithm  
🌐 Web API with Flask + a demo frontend (index.html)  
📄 Outputs both human-readable and machine-friendly results  

🧠 How It Works
---------------
- Input Waypoints — Provided via `waypoints.txt` or through the web UI  
- Distance Calculation — Computes 3D Euclidean distances between points  
- Initial Route — Uses a greedy Nearest Neighbor approach  
- Optimization — Refines the path using the 2-Opt algorithm  
- Output — Shows the ordered path and total fuel cost  

📁 Project Structure
--------------------
.
├── app.py               # Flask API server  
├── main.py              # CLI interface to optimize waypoints  
├── tsp_solver.py        # Contains the core TSP logic (NN and 2-Opt)  
├── waypoint_utils.py    # Utilities to parse waypoint data  
├── waypoints.txt        # Sample input waypoints  
└── sample_output/  
    └── path.txt         # Output path from CLI  

🖥️ Run the CLI
--------------
```bash
python main.py
```

You’ll get something like:
```
Optimized Path: 1 -> 3 -> 9 -> ...
Total Fuel Cost: 28.52 units
```

🌐 Run the Web App
------------------
Install dependencies:

```bash
pip install flask flask-cors
```

Start the server:

```bash
python app.py
```

Then visit: [http://localhost:5000](http://localhost:5000)

Paste your waypoint data and hit "Optimize".

✏️ Waypoint Format
-------------------
Each waypoint must follow this format:
```
ID X Y Z
```

Example:
```
1 6.39 0.25 2.75
2 2.23 7.36 6.77
```

✅ Output
---------
- Path as a sequence of waypoint IDs  
- Total fuel cost (3D path length)  
- Detailed position info per waypoint  

📌 TODO / Ideas
---------------
- Add visualization of the optimized route  
- Support momentum-based cost modeling  
- Handle user-uploaded files in web UI  

🧪 Sample Data
--------------
See `waypoints.txt` for a 12-point sample scenario

🛠️ License
-----------
MIT – do whatever you want, just give credit!
