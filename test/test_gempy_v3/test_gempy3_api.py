﻿from pprint import pprint

import gempy as gp
import gempy_viewer
from gempy import GeoModel


def test_api_create_data():
    geo_data = _create_data()

    pprint(geo_data)
    return geo_data


def _create_data():
    data_path = 'https://raw.githubusercontent.com/cgre-aachen/gempy_data/master/'
    geo_data: GeoModel = gp.create_data(
        project_name='horizontal',
        extent=[0, 1000, 0, 1000, 0, 1000],
        resolution=[50, 50, 50],
        path_o=data_path + "/data/input_data/jan_models/model1_orientations.csv",
        path_i=data_path + "/data/input_data/jan_models/model1_surface_points.csv"
    )
    return geo_data


def test_map_stack_to_surfaces():
    geo_data = _create_data()
    
    gp.map_stack_to_surfaces(
        gempy_model=geo_data,
        mapping_object={"Strat_Series": ('rock2', 'rock1')}
    )
    
    pprint(geo_data.structural_frame)


def test_api_compute_model():
    geo_data = _create_data()
    
    gp.map_stack_to_surfaces(
        gempy_model=geo_data,
        mapping_object={"Strat_Series": ('rock2', 'rock1')}
    )
    
    gempy_viewer.plot_2d(geo_data, direction=['y'])