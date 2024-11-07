"""An example of calling a Fortran BMI through Cython."""

import numpy as np
from pymt_heatf import HeatModelF


config_file = "test.cfg"


# Instantiate a model and get its name.
m = HeatModelF()
print(m.get_component_name())

# Initialize the model.
m.initialize(config_file)

# Get the grid_id for the plate_surface__temperature variable.
var_name = "plate_surface__temperature"
print("Variable {}".format(var_name))
grid_id = m.get_var_grid(var_name)
print(" - grid id:", grid_id)

# Get grid and variable info for plate_surface__temperature.
# All should raise RuntimeError because they're not implemented.
node_count = m.get_grid_node_count(grid_id)
edge_count = m.get_grid_edge_count(grid_id)
face_count = m.get_grid_face_count(grid_id)
print(" - node count:", node_count)
print(" - edge count:", edge_count)
print(" - face count:", face_count)

nodes_per_face = np.empty(face_count, dtype=np.int32)
m.get_grid_nodes_per_face(grid_id, nodes_per_face)
print(" - nodes per face:", nodes_per_face)

edge_nodes = np.empty(2 * edge_count, dtype=np.int32)
m.get_grid_edge_nodes(grid_id, edge_nodes)
print(" - edge nodes:", edge_nodes)

face_edges = np.empty(np.sum(nodes_per_face), dtype=np.int32)
m.get_grid_face_edges(grid_id, face_edges)
print(" - face edges:", face_edges)

face_nodes = np.empty(np.sum(nodes_per_face), dtype=np.int32)
m.get_grid_face_nodes(grid_id, face_nodes)
print(" - face nodes:", face_nodes)

# Finalize the model.
m.finalize()
