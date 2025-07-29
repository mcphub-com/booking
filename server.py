import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/apidojo/api/booking'

mcp = FastMCP('booking')

@mcp.tool()
def currency_get_exchange_rates(base_currency: Annotated[str, Field(description='One of the followings : en|en-us|ar|bg|ca|cs|da|de|el|es|es-ar|et|fi|fr|he|hr|hu|id|is|it|ja|ko|lt|lv|ms|nl|no|pl|pt|pt-br|ro|ru|sk|sl|sr|sv|th|tl|tr|uk|vi|zh|zh-tw')],
                                languagecode: Annotated[Union[str, None], Field(description='The language code of specific country')] = None) -> dict: 
    '''Get currency exchange rates between different countries'''
    url = 'https://apidojo-booking-v1.p.rapidapi.com/currency/get-exchange-rates'
    headers = {'x-rapidapi-host': 'apidojo-booking-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'base_currency': base_currency,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def locations_auto_complete(text: Annotated[str, Field(description='Name of cities, districts, places')],
                            languagecode: Annotated[Union[str, None], Field(description='One of the followings en|en-us|ar|bg|ca|cs|da|de|el|es|es-ar|et|fi|fr|he|hr|hu|id|is|it|ja", "ko|lt|lv|ms|nl|no|pl|pt|pt-br|ro|ru|sk|sl|sr|sv|th|tl|tr|uk|vi|zh|zh-tw')] = None) -> dict: 
    '''List suggested locations by countries, cities, districts, places name'''
    url = 'https://apidojo-booking-v1.p.rapidapi.com/locations/auto-complete'
    headers = {'x-rapidapi-host': 'apidojo-booking-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'text': text,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def filters_list(room_qty: Annotated[Union[int, float], Field(description='The number of rooms Default: 2')],
                 departure_date: Annotated[str, Field(description='The check-out date')],
                 dest_ids: Annotated[Union[int, float], Field(description="Value of dest_id or city_ufi field from locations/auto-complete API (Don't pass this if you use latlong as search_type) Default: -3712125")],
                 guest_qty: Annotated[str, Field(description='The number of adults')],
                 arrival_date: Annotated[str, Field(description='The check-in date at hotel')],
                 search_type: Annotated[str, Field(description='Value of dest_type returned by locations/auto-complete API')],
                 languagecode: Annotated[Union[str, None], Field(description='One of the followings : en|en-us|ar|bg|ca|cs|da|de|el|es|es-ar|et|fi|fr|he|hr|hu|id|is|it|ja|ko|lt|lv|ms|nl|no|pl|pt|pt-br|ro|ru|sk|sl|sr|sv|th|tl|tr|uk|vi|zh|zh-tw')] = None,
                 categories_filter: Annotated[Union[str, None], Field(description='The id returned by .../filters/list API')] = None,
                 children_qty: Annotated[Union[str, None], Field(description='The number of children')] = None,
                 children_age: Annotated[Union[str, None], Field(description='The year old of each child that separated by comma')] = None,
                 longitude: Annotated[Union[int, float, None], Field(description="106.686102 - Don't pass this param if you DON'T use latlong as search_type Default: 0")] = None,
                 price_filter_currencycode: Annotated[Union[str, None], Field(description='The base currency to calculate exchange rate')] = None,
                 latitude: Annotated[Union[int, float, None], Field(description="10.838039 - Don't pass this param if you DON'T use latlong as search_type Default: 0")] = None) -> dict: 
    '''A list of filter options to pass in categories_filter field. Pass params and values are as same as .../properties/list API'''
    url = 'https://apidojo-booking-v1.p.rapidapi.com/filters/list'
    headers = {'x-rapidapi-host': 'apidojo-booking-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'room_qty': room_qty,
        'departure_date': departure_date,
        'dest_ids': dest_ids,
        'guest_qty': guest_qty,
        'arrival_date': arrival_date,
        'search_type': search_type,
        'languagecode': languagecode,
        'categories_filter': categories_filter,
        'children_qty': children_qty,
        'children_age': children_age,
        'longitude': longitude,
        'price_filter_currencycode': price_filter_currencycode,
        'latitude': latitude,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def review_filters_list(hotel_id: Annotated[Union[int, float], Field(description='The value of hotel_id field from properties/list API Default: 1790664')],
                        languagecode: Annotated[Union[str, None], Field(description='One of the followings : en|en-us|ar|bg|ca|cs|da|de|el|es|es-ar|et|fi|fr|he|hr|hu|id|is|it|ja|ko|lt|lv|ms|nl|no|pl|pt|pt-br|ro|ru|sk|sl|sr|sv|th|tl|tr|uk|vi|zh|zh-tw')] = None,
                        filter_language: Annotated[Union[str, None], Field(description='One of the followings (separated by comma for multiple values): en|en-us|ar|bg|ca|cs|da|de|el|es|es-ar|et|fi|fr|he|hr|hu|id|is|it|ja|ko|lt|lv|ms|nl|no|pl|pt|pt-br|ro|ru|sk|sl|sr|sv|th|tl|tr|uk|vi|zh|zh-tw')] = None,
                        filter_customer_type: Annotated[Union[str, None], Field(description='One of the followings (separated by comma for multiple values) : couple|family_with_children|review_category_group_of_friends|solo_traveller')] = None,
                        user_sort: Annotated[Union[str, None], Field(description='One of the followings : sort_most_relevant|sort_recent_desc|sort_recent_asc|sort_score_desc|sort_score_asc')] = None) -> dict: 
    '''List supported options metadata for filtering reviews'''
    url = 'https://apidojo-booking-v1.p.rapidapi.com/review-filters/list'
    headers = {'x-rapidapi-host': 'apidojo-booking-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'languagecode': languagecode,
        'filter_language': filter_language,
        'filter_customer_type': filter_customer_type,
        'user_sort': user_sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def reviews_list(hotel_ids: Annotated[Union[int, float], Field(description='The value of hotel_id field from properties/list API Default: 2536126')],
                 languagecode: Annotated[Union[str, None], Field(description='One of the followings : en|en-us|ar|bg|ca|cs|da|de|el|es|es-ar|et|fi|fr|he|hr|hu|id|is|it|ja|ko|lt|lv|ms|nl|no|pl|pt|pt-br|ro|ru|sk|sl|sr|sv|th|tl|tr|uk|vi|zh|zh-tw')] = None,
                 user_sort: Annotated[Union[str, None], Field(description='One of the followings : sort_most_relevant|sort_recent_desc|sort_recent_asc|sort_score_desc|sort_score_asc')] = None,
                 rows: Annotated[Union[int, float, None], Field(description='The number of items per page Default: 25')] = None,
                 offset: Annotated[Union[int, float, None], Field(description='The number of items to ignore as offset for paging Default: 0')] = None,
                 filter_language: Annotated[Union[str, None], Field(description='One of the followings (separated by comma for multiple values): en|en-us|ar|bg|ca|cs|da|de|el|es|es-ar|et|fi|fr|he|hr|hu|id|is|it|ja|ko|lt|lv|ms|nl|no|pl|pt|pt-br|ro|ru|sk|sl|sr|sv|th|tl|tr|uk|vi|zh|zh-tw')] = None,
                 filter_customer_type: Annotated[Union[str, None], Field(description='One of the followings (separated by comma for multiple values) : couple|family_with_children|review_category_group_of_friends|solo_traveller')] = None) -> dict: 
    '''List reviews of stayed guests'''
    url = 'https://apidojo-booking-v1.p.rapidapi.com/reviews/list'
    headers = {'x-rapidapi-host': 'apidojo-booking-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_ids': hotel_ids,
        'languagecode': languagecode,
        'user_sort': user_sort,
        'rows': rows,
        'offset': offset,
        'filter_language': filter_language,
        'filter_customer_type': filter_customer_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def reviews_get_scores(hotel_ids: Annotated[Union[int, float], Field(description='The value of hotel_id field from properties/list API Default: 264831')],
                       languagecode: Annotated[Union[str, None], Field(description='One of the followings : en|en-us|ar|bg|ca|cs|da|de|el|es|es-ar|et|fi|fr|he|hr|hu|id|is|it|ja|ko|lt|lv|ms|nl|no|pl|pt|pt-br|ro|ru|sk|sl|sr|sv|th|tl|tr|uk|vi|zh|zh-tw')] = None) -> dict: 
    '''Get reviewing scores'''
    url = 'https://apidojo-booking-v1.p.rapidapi.com/reviews/get-scores'
    headers = {'x-rapidapi-host': 'apidojo-booking-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_ids': hotel_ids,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
