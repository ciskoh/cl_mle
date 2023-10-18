"""
    Test module for predict function
"""

import sys
sys.path.append(".")

from src.models.predict_model import robust_predict
import pandas as pd

model_path="/home/matt/CL/california-housing-prediction_01/src/models/trained_model.pkl"

test_input=pd.DataFrame([{'longitude': -122.29,
 'latitude': 37.89,
 'housing_median_age': 52.0,
 'total_rooms': 979.0,
 'population': 374.0,
 'households': 153.0,
 'median_income': 5.1675}])

def test_output_type(model_to_test=model_path, test_input=test_input, expected=float):
    """
    Tests that output values are float
    """
    output=robust_predict(model_to_test, test_input)[0]
    assert isinstance(output, expected)


def test_output_range(model_to_test=model_path, test_input=test_input, expected=[0,1e10]):
    """
        tests that output is expected range
    """
    output= robust_predict(model_to_test,test_input)[0]
    assert expected[0]<= output <=expected[1]

