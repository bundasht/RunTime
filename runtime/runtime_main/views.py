import os
import requests
import json
import h2o
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.views import generic
from .models import *


from .serializers import UserInfoSerializer, UserSerializer
from rest_framework.decorators import api_view


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


def get_weather(cords):
    API_key = '4e9e25660657a41a100167b6ba0035ce'
    pass


class UserInfoViewSet(viewsets.ModelViewSet):

    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


@api_view(['GET', 'POST'])
def prediction(request):

    if request.method == 'POST':
        import pdb
        pdb.set_trace()
        user_id = request.data['user']
        user_info = UserInfo.objects.filter(user=user_id).latest('created')


        age = user_info.age
        weight = user_info.weight
        age = user_info.age
        age = user_info.age
        age = user_info.age
        age = user_info.age

        data = ['predykcje']
        return Response({"result": data})
    return Response({"result": 'Dawaj'})

    # def list(self, request, *args, **kwargs):
    #     data = models.UserInfo.objects.latest('created')
    #
    #     funkcja(data)
    #
    #
    #     data = PredictionSerializer(data).data
    #     return data


