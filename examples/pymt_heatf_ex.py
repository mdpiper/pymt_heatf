"""Run the heatf model in pymt."""

import numpy as np
from pymt.models import HeatModelF


np.set_printoptions(formatter={"float": "{: 6.2f}".format})


# Instantiate the component and get its name.
m = HeatModelF()
print(m.name)

# Call setup, then initialize the model.
args = m.setup(".")
m.initialize(*args)

# Get time information from the model.
print("Start time:", m.start_time)
print("End time:", m.end_time)
print("Current time:", m.time)
print("Time step:", m.time_step)
print("Time units:", m.time_units)

# List the model's exchange items.
print("Number of input vars:", len(m.input_var_names))
for var in m.input_var_names:
    print(" - {}".format(var))
print("Number of output vars:", len(m.output_var_names))
for var in m.output_var_names:
    print(" - {}".format(var))

# Get variable info.
var_name = m.output_var_names[0]
print("Variable {}".format(var_name))
print(" - variable type:", m.var[var_name].type)
print(" - units:", m.var[var_name].units)
print(" - itemsize:", m.var_itemsize(var_name))
print(" - nbytes:", m.var_nbytes(var_name))
print(" - location:", m.var[var_name].location)

# Get grid info for variable.
grid_id = m.var[var_name].grid
print(" - grid id:", grid_id)
print(" - grid type:", m.grid_type(grid_id))
print(" - rank:", m.grid_ndim(grid_id))
grid_size = m.grid_node_count(grid_id)
print(" - size:", grid_size)
print(" - shape:", m.grid_shape(grid_id))

# Get the initial values of the variable.
print("Get initial values of {}...".format(var_name))
print(" - values, flattened:")
print(m.var[var_name].data)
print(" - values, redimensionalized:")
print(m.var[var_name].data.reshape(m.grid_shape(grid_id), order="F"))

# Set new values.
print("Set new values of {}...".format(var_name))
new = np.zeros(grid_size, dtype=np.float32)
new[20] = 10.0
m.set_value(var_name, new)
print(" - values, flattened:")
print(m.var[var_name].data)
print(" - values, redimensionalized:")
print(m.var[var_name].data.reshape(m.grid_shape(grid_id), order="F"))

# Advance the model by one time step.
m.update()
print("Update: current time:", m.time)
print(" - values at time {}:".format(m.time))
print(m.var[var_name].data.reshape(m.grid_shape(grid_id), order="F"))

# Advance the model until a later time.
m.update_until(5.0)
print("Update: current time:", m.time)
print(" - values at time {}:".format(m.time))
print(m.var[var_name].data.reshape(m.grid_shape(grid_id), order="F"))

# Get the grid_id for the plate_surface__thermal_diffusivity variable.
var_name = "plate_surface__thermal_diffusivity"
print("Variable {}".format(var_name))
grid_id = m.var_grid(var_name)
print(" - grid id:", grid_id)

# Get grid and variable info for plate_surface__thermal_diffusivity.
print(" - grid type:", m.grid_type(grid_id))
grid_rank = m.grid_ndim(grid_id)
print(" - rank:", grid_rank)
print(" - size:", m.grid_node_count(grid_id))
print(" - x:", m.grid_x(grid_id))
print(" - y:", m.grid_y(grid_id))
print(" - z:", m.grid_z(grid_id))
print(" - variable type:", m.var_type(var_name))
print(" - units:", m.var_units(var_name))
print(" - itemsize:", m.var_itemsize(var_name))
print(" - nbytes:", m.var_nbytes(var_name))
print(" - location:", m.var_location(var_name))

# Get the diffusivity values.
val = m.get_value(var_name)
print(" - values:")
print(val)

# Get the grid_id for the model__identification_number variable.
var_name = "model__identification_number"
print("Variable {}".format(var_name))
grid_id = m.var_grid(var_name)
print(" - grid id:", grid_id)

# Get grid and variable info for model__identification_number.
print(" - grid type:", m.grid_type(grid_id))
grid_rank = m.grid_ndim(grid_id)
print(" - rank:", grid_rank)
print(" - size:", m.grid_node_count(grid_id))
print(" - x:", m.grid_x(grid_id))
print(" - y:", m.grid_y(grid_id))
print(" - z:", m.grid_z(grid_id))
print(" - variable type:", m.var_type(var_name))
print(" - units:", m.var_units(var_name))
print(" - itemsize:", m.var_itemsize(var_name))
print(" - nbytes:", m.var_nbytes(var_name))
print(" - location:", m.var_location(var_name))

# Get the model id.
val = m.get_value(var_name)
print(" - values:")
print(val)

# Set new model id.
new = 42
m.set_value(var_name, new)
check = m.get_value(var_name)
print(" - new values (set/get):")
print(check)

# Finalize the model.
m.finalize()
