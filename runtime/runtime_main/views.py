import os

import h2o
from django.shortcuts import render

from RunTime.runtime.runtime.settings import BASE_DIR


def predict_health(data_dict):
    """
    age, height, weight, comfort_rating
    """
    h2o.init()
    h2o_model = h2o.load_model(os.path.join(BASE_DIR, os.path.join('h2o_models', 'xgboost-health')))
    data_row = h2o.H2OFrame(data_dict, column_names=['age', 'height', 'weight', 'comfort_rating'])
    data_prediction = h2o_model.predict(data_row)
    return data_prediction


def predict_activities(data_dict):
    """
    food_hours,	food_calories,	active_hours,	active_rating,	sleep_hours,	sleep_duration,	comfort_rating

    """
    h2o.init()
    h2o_model = h2o.load_model(os.path.join(BASE_DIR, os.path.join('h2o_models', 'xgboost-activities')))
    data_row = h2o.H2OFrame(data_dict,
                            column_names=['food_hours', 'food_calories', 'active_hours', 'active_rating', 'sleep_hours',
                                          'sleep_duration', 'comfort_rating'])
    data_prediction = h2o_model.predict(data_row)
    return data_prediction


def predict_weather(data_dict):
    """
    weather_temperature	weather_humidity	weather_wind
    """
    h2o.init()
    h2o_model = h2o.load_model(os.path.join(BASE_DIR, os.path.join('h2o_models', 'xgboost-weather')))
    data_row = h2o.H2OFrame(data_dict, column_names=['weather_temperature', 'weather_humidity', 'weather_wind'])
    data_prediction = h2o_model.predict(data_row)
    return data_prediction


def calc_bmr(data_dict):
    bmr = 10 * float(data_dict['weight']) + 6.25 * float(data_dict['height']) + 5 * float(data_dict['age']) - 130
    return bmr


def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')
