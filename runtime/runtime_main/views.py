import os
import requests
import json
import h2o
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.views import generic
from . import models
from .serializers import UserInfoSerializer, PredictionSerializer, MultiSerializerViewSet

from runtime.settings import BASE_DIR


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

def get_weather(cords):
    API_key = '4e9e25660657a41a100167b6ba0035ce'
    pass

class UserInfoViewSet(MultiSerializerViewSet):

    queryset = models.UserInfo.objects.all()
    serializer_class = {
        'create': UserInfoSerializer,
        # 'list': PredictionSerializer
    }

    def create(self, request, *args, **kwargs):
        import pdb
        pdb.set_trace()

        super(UserInfoViewSet, self).create(request, *args, **kwargs)

        last_item = models.UserInfo.objects.latest('created')
        last_item = {'values': 5}
        # value = predykcje(last_item)

        data = PredictionSerializer(last_item).data
        return Response(data)

    # def list(self, request, *args, **kwargs):
    #     data = models.UserInfo.objects.latest('created')
    #
    #     funkcja(data)
    #
    #
    #     data = PredictionSerializer(data).data
    #     return data


