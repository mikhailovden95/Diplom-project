import sender_stand_request
import data

def test_create_and_get_order():
    """Полный тест: создание заказа и получение по треку"""
    
    # Шаг 1: Создание заказа
    create_response = sender_stand_request.create_order(data.order_body)
    
    # Проверка успешного создания заказа
    assert create_response.status_code == 201, f"Ошибка создания заказа: {create_response.status_code}"
    
    # Шаг 2: Получение трек-номера
    track_number = create_response.json().get("track")
    assert track_number is not None, "Трек-номер не получен"
    print(f"Создан заказ с трек-номером: {track_number}")
    
    # Шаг 3: Получение заказа по треку
    get_response = sender_stand_request.get_order_by_track(track_number)
    
    # Шаг 4: Проверка кода ответа
    assert get_response.status_code == 200, f"Ожидался код 200, получен {get_response.status_code}"
    