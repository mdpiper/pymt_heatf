"""Run the heatf model through its BMI in Python."""

import numpy as np
from pymt_heatf import HeatModelF


config_file = "test.cfg"
np.set_printoptions(formatter={"float": "{: 6.2f}".format})


# Instantiate and initialize the model.
m = HeatModelF()
print(m.get_component_name())
m.initialize(config_file)

# Get time information from the model.
print("Start time:", m.get_start_time())
print("End time:", m.get_end_time())
print("Current time:", m.get_current_time())
print("Time step:", m.get_time_step())
print("Time units:", m.get_time_units())

# List the model's exchange items.
print("Input vars:", m.get_input_var_names())
print("Output vars:", m.get_output_var_names())

# Get the grid_id for the plate_surface__temperature variable.
var_name = "plate_surface__temperature"
print("Variable {}".format(var_name))
grid_id = m.get_var_grid(var_name)
print(" - grid id:", grid_id)

# Get grid and variable info for plate_surface__temperature.
print(" - grid type:", m.get_grid_type(grid_id))
grid_rank = m.get_grid_rank(grid_id)
print(" - rank:", grid_rank)
grid_shape = np.empty(grid_rank, dtype=np.int32)
m.get_grid_shape(grid_id, grid_shape)
print(" - shape:", grid_shape)
grid_size = m.get_grid_size(grid_id)
print(" - size:", grid_size)
grid_spacing = np.empty(grid_rank, dtype=np.float64)
m.get_grid_spacing(grid_id, grid_spacing)
print(" - spacing:", grid_spacing)
grid_origin = np.empty(grid_rank, dtype=np.float64)
m.get_grid_origin(grid_id, grid_origin)
print(" - origin:", grid_origin)
print(" - variable type:", m.get_var_type(var_name))
print(" - units:", m.get_var_units(var_name))
print(" - itemsize:", m.get_var_itemsize(var_name))
print(" - nbytes:", m.get_var_nbytes(var_name))
print(" - location:", m.get_var_location(var_name))

# View default initial temperature values.
val = np.empty(grid_size, dtype=np.float32)
m.get_value(var_name, val)
print(" - initial values (flattened):")
print(val)
print(" - initial values (gridded):")
print(val.reshape(grid_shape, order="F"))
print(" -- total temperature:", val.sum())

# Set new initial temperature values.
new = np.zeros(grid_size, dtype=np.float32)
new[20] = 10.0
m.set_value(var_name, new)
val = np.empty(grid_size, dtype=np.float32)
m.get_value(var_name, val)
print(" - new initial values (flattened):")
print(val)
print(" - new initial values (gridded):")
print(val.reshape(grid_shape, order="F"))
print(" -- total temperature:", val.sum())

# Advance the model by one time step.
m.update()
print("Updated time:", m.get_current_time())
val = np.empty(grid_size, dtype=np.float32)
m.get_value(var_name, val)
print(" - updated values (gridded):")
print(val.reshape(grid_shape, order="F"))
print(" -- total temperature:", val.sum())

# Get a reference to the temperature values and check that it updates.
print(" - values (by ref, gridded) at time {}:".format(m.get_current_time()))
ref = m.get_value_ptr(var_name)
print(ref.reshape(grid_shape, order="F"))
m.update()
print(" - values (by ref, gridded) at time {}:".format(m.get_current_time()))
print(ref.reshape(grid_shape, order="F"))
print(" -- total temperature:", ref.sum())

# Advance the model until a later time.
m.update_until(5.0)
print("Later time:", m.get_current_time())
print(" - updated values (gridded):")
print(ref.reshape(grid_shape, order="F"))
print(" -- total temperature:", ref.sum())

# Get the grid_id for the plate_surface__thermal_diffusivity variable.
var_name = "plate_surface__thermal_diffusivity"
print("Variable {}".format(var_name))
grid_id = m.get_var_grid(var_name)
print(" - grid id:", grid_id)

# Get grid and variable info for plate_surface__thermal_diffusivity.
print(" - grid type:", m.get_grid_type(grid_id))
grid_rank = m.get_grid_rank(grid_id)
print(" - rank:", grid_rank)
print(" - size:", m.get_grid_size(grid_id))
grid_x = np.empty(max(grid_rank, 1), dtype=np.float64)
m.get_grid_x(grid_id, grid_x)
print(" - x:", grid_x)
grid_y = np.empty(max(grid_rank, 1), dtype=np.float64)
m.get_grid_y(grid_id, grid_y)
print(" - y:", grid_y)
grid_z = np.empty(max(grid_rank, 1), dtype=np.float64)
m.get_grid_z(grid_id, grid_z)
print(" - z:", grid_z)
print(" - variable type:", m.get_var_type(var_name))
print(" - units:", m.get_var_units(var_name))
print(" - itemsize:", m.get_var_itemsize(var_name))
print(" - nbytes:", m.get_var_nbytes(var_name))
print(" - location:", m.get_var_location(var_name))

# Get the diffusivity values.
val = np.empty(1, dtype=np.float32)
m.get_value(var_name, val)
print(" - values:")
print(val)

# Get the grid_id for the model__identification_number variable.
var_name = "model__identification_number"
print("Variable {}".format(var_name))
grid_id = m.get_var_grid(var_name)
print(" - grid id:", grid_id)

# Get grid and variable info for model__identification_number.
print(" - grid type:", m.get_grid_type(grid_id))
grid_rank = m.get_grid_rank(grid_id)
print(" - rank:", grid_rank)
print(" - size:", m.get_grid_size(grid_id))
grid_x = np.empty(max(grid_rank, 1), dtype=np.float64)
m.get_grid_x(grid_id, grid_x)
print(" - x:", grid_x)
grid_y = np.empty(max(grid_rank, 1), dtype=np.float64)
m.get_grid_y(grid_id, grid_y)
print(" - y:", grid_y)
grid_z = np.empty(max(grid_rank, 1), dtype=np.float64)
m.get_grid_z(grid_id, grid_z)
print(" - z:", grid_z)
print(" - variable type:", m.get_var_type(var_name))
print(" - units:", m.get_var_units(var_name))
print(" - itemsize:", m.get_var_itemsize(var_name))
print(" - nbytes:", m.get_var_nbytes(var_name))
print(" - location:", m.get_var_location(var_name))

# Get the model id.
val = np.empty(1, dtype=np.int32)
m.get_value(var_name, val)
print(" - values:")
print(val)

# Set new model id.
new = np.array(42, dtype=np.intc)
m.set_value(var_name, new)
check = np.empty(1, dtype=np.int32)
m.get_value(var_name, check)
print(" - new values (set/get):")
print(check)

# Finalize the model.
m.finalize()

# Check that number of instances can't exceed N_MODELS=3.
# a = Heatf()
# b = Heatf()
# c = Heatf()  # should fail with index=-1
