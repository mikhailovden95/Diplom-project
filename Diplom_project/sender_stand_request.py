import requests
import configuration
import data

def create_order(body):
    """Функция для создания заказа"""
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body,
        headers={"Content-Type": "application/json"}
    )

def get_order_by_track(track_number):
    """Функция для получения заказа по треку"""
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
        params={"t": track_number}
    )