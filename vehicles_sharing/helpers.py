import re

from django.core.validators import RegexValidator
from django.db.models import Q
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class PomMethods:
    @staticmethod
    def get_user_from_token(request):
        token = request.META.get('HTTP_AUTHORIZATION').split(" ")[1]
        if token:
            user_id = Token.objects.get(key=token).user_id
            return User.objects.get(id=user_id)
        else:
            return None

    @staticmethod
    def get_user_from_username(username):
        return User.objects.get(username=username)

    @staticmethod
    def get_token_from_user_id(user_id):
        return Token.objects.get(user_id__exact=user_id)

    @staticmethod
    def check_if_params_correct(self, params):
        """TODO"""
        pass

    @staticmethod
    def normalize_query(query_string,
                        findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                        normspace=re.compile(r'\s{2,}').sub):
        return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

    @staticmethod
    def get_query(query_string, search_fields):
        query = None
        terms = PomMethods.normalize_query(query_string)
        for term in terms:
            or_query = None
            for field_name in search_fields:
                q = Q(**{"%s__icontains" % field_name: term})
                if or_query is None:
                    or_query = q
                else:
                    or_query = or_query | q
            if query is None:
                query = or_query
            else:
                query = query & or_query
        return query


class VehicleFilteringParams:
    MIN_PRICE = 'min_price'
    MAX_PRICE = 'max_price'
    MIN_POWER = 'min_power'
    MAX_POWER = 'max_power'
    CITY = 'city'
    BRAND = 'brand'
    MODEL = 'model'
    MIN_PRODUCTION_YEAR = 'min_production_year'
    MAX_PRODUCTION_YEAR = 'max_production_year'
    MIN_CAPACITY = 'min_capacity'
    MAX_CAPACITY = 'max_capacity'
    DRIVE_TRAIN = 'drive_train'


class Validators:
    brand = RegexValidator(regex=r'^[A-Za-z \-]*$', message='Only alphanumeric characters and - are allowed.')
    only_letters = RegexValidator(regex=r'^[A-Za-z]*$', message='Only alphanumeric characters and - are allowed.')
    alphanumeric = RegexValidator(regex=r'^[a-zA-Z0-9]*$', message='Only letters, digits and - are allowed.')
    numeric = RegexValidator(regex=r'^[0-9]*$', message='Only digits are allowed.')
    drive_train = RegexValidator(regex=r'RWD|AWD|FWD', message='Only digits are allowed.')
    city_street = RegexValidator(regex=r'^[A-Za-z \-]*$', message='Only alphanumeric characters and - are allowed.')
