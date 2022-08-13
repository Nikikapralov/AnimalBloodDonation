import math
from datetime import date

from rest_framework.exceptions import ValidationError
from dateutil import parser


def validate_over_LIMIT_AGE(given_date):
    LIMIT_AGE = 16
    current_year = str(date.today())
    current_year = parser.parse(current_year)
    given_date = parser.parse(str(given_date))
    difference = current_year - given_date
    result = math.floor(difference.days / 365.242199)
    if result < LIMIT_AGE:
        raise ValidationError("Too young to register, im sorry, please speak with a parent or legal guardian.")