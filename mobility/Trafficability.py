import numpy as np

max_slope = 0.4
no_go_threshold = 700
no_go = 5000  # for borders to avoid taking paths along borders
resistivity_vegetation_grassland = 30
resistivity_vegetation_shrubland = 100
resistivity_vegetation_woodland = 200
resistivity_vegetation_medium_density_forest = 400
resistivity_vegetation_high_density_forest = 600
resistivity_vegetation_unknown = resistivity_vegetation_woodland  # unknown vegetation is considered woodland as default
resistivity_vegetation_empty = 65  # empty areas taken as in between grassland and shrubland
resistivity_building = 1000
resistivity_road = 1
resistivity_bridge = 1
resistivity_water = 10000
resistivity_heavy_slope = 800
offset = 10  # default


def get_trafficability_grid(all_overlays_grid, is_building, is_elevation, is_roads, is_vegetation, is_water):
    trafficability_grid = np.zeros((all_overlays_grid.shape[0], all_overlays_grid.shape[1]))
    go_no_go_grid = np.zeros((all_overlays_grid.shape[0], all_overlays_grid.shape[1]))
    row_id = 0
    elevation_min = np.min(all_overlays_grid[:, :, 2])
    for rows in all_overlays_grid:
        column_id = 0
        for column in rows:
            trafficability_grid[row_id, column_id], go_no_go_grid[row_id, column_id] \
                = trafficability_of_cell(column, is_building, is_elevation, is_roads, is_vegetation, is_water,
                                         elevation_min)
            column_id = column_id + 1
        row_id = row_id + 1
    # trafficability_grid[0, :] = no_go
    # trafficability_grid[:, 0] = no_go
    # trafficability_grid[trafficability_grid.shape[0] - 1, :] = no_go
    # trafficability_grid[:, trafficability_grid.shape[1] - 1] = no_go
    # go_no_go_grid[0, :] = 0
    # go_no_go_grid[:, 0] = 0
    # go_no_go_grid[trafficability_grid.shape[0] - 1, :] = 0
    # go_no_go_grid[:, trafficability_grid.shape[1] - 1] = 0
    return trafficability_grid, go_no_go_grid


def trafficability_of_cell(cell, is_building, is_elevation, is_roads, is_vegetation, is_water, elevation_min):
    elevation = cell[2] - elevation_min
    slope = cell[3]
    vegetation = cell[4]
    building = cell[5]
    water = cell[6]
    road = cell[7]
    bridge = water == 1 and road == 1
    resistivity_of_cell = offset
    if slope > max_slope:
        resistivity_of_cell = resistivity_of_cell + resistivity_heavy_slope
    if is_elevation == 1:
        resistivity_of_cell = resistivity_of_cell + elevation

    # no road, building, water, vegetation coincide on a cell,
    # if so, priority of availability is road > building > water > vegetation
    if is_roads == 1 and road == 1:  # road on cell
        resistivity_of_cell = elevation + resistivity_road
    elif bridge:  # bridge must be considered even if road not needed
        resistivity_of_cell = elevation + resistivity_bridge
    elif is_building == 1 and 1000 <= building <= 5000:  # building on cell
        resistivity_of_cell = resistivity_of_cell + resistivity_building
    elif is_water == 1 and water == 1:  # water on cell
        resistivity_of_cell = resistivity_of_cell + resistivity_water
    elif is_vegetation == 1:
        if vegetation == 1:  # grassland
            resistivity_of_cell = resistivity_of_cell + resistivity_vegetation_grassland
        elif vegetation == 2:  # shrubland
            resistivity_of_cell = resistivity_of_cell + resistivity_vegetation_shrubland
        elif vegetation == 3:  # woodland
            resistivity_of_cell = resistivity_of_cell + resistivity_vegetation_woodland
        elif vegetation == 4:  # medium density forest
            resistivity_of_cell = resistivity_of_cell + resistivity_vegetation_medium_density_forest
        elif vegetation == 5:  # high density forest
            resistivity_of_cell = resistivity_of_cell + resistivity_vegetation_high_density_forest
        elif vegetation == 5:  # unknown
            resistivity_of_cell = resistivity_of_cell + resistivity_vegetation_unknown
        else:
            resistivity_of_cell = resistivity_of_cell + resistivity_vegetation_empty

    go_no_go_val = 0  # unrestricted
    # as elevation does not effect no go, its only effect cost for path elevation must be added to threshold
    if 50000 > resistivity_of_cell > (no_go_threshold + elevation):
        go_no_go_val = 1
    return resistivity_of_cell, go_no_go_val

# def trafficability_of_cell_levels(cell):
#     slope = cell[3]
#     vegetation = cell[4]
#     building = cell[5]
#     water = cell[6]
#     road = cell[7]
#     # mobility levels = {1, 2, 3, 4, 5, 6, 7}
#     trafficability = None
#     if slope <= 0.05 or vegetation == 1:  # grassland
#         trafficability = 2
#     if slope > 0.05 or vegetation == 2 or vegetation == 6:  # shrubland, unknown vegetation
#         trafficability = 3
#     if slope > 0.1 or vegetation == 3:  # woodland
#         trafficability = 4
#     if slope > 0.15 or vegetation == 4 or water == 1:  # medium density forest
#         trafficability = 5
#     if slope > 0.2 or vegetation == 5:  # high density forest, deep water
#         trafficability = 6
#     if building == 1:
#         trafficability = 7
#     if road == 1:  # roads
#         trafficability = 1
#     return trafficability
