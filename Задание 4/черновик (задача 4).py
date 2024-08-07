import requests
import pandas as pd

def get_tracker_list(api_key):
    # Получение списка всех трекеров
    list_url = 'https://api.navixy.com/v2/tracker/list'
    list_data = {
        "hash": api_key
    }

    list_response = requests.post(list_url, headers={'Content-Type': 'application/json'}, json=list_data)
    trackers = list_response.json().get('list', [])
    return trackers

def get_tracker_states(api_key, tracker_ids):
    # Получение состояний для всех трекеров
    states_url = 'https://api.navixy.com/v2/tracker/get_states'
    states_data = {
        "hash": api_key,
        "trackers": tracker_ids,
        "allow_not_exist": True,
        "list_blocked": True
    }

    states_response = requests.post(states_url, headers={'Content-Type': 'application/json'}, json=states_data)
    return states_response.json().get('states', {})

def main():
    api_key = "feed000000000000000000000000cafe"
    
    # Получение списка трекеров
    trackers = get_tracker_list(api_key)
    
    # Извлечение ID трекеров
    tracker_ids = [tracker['id'] for tracker in trackers]

    # Получение состояний трекеров
    tracker_states = get_tracker_states(api_key, tracker_ids)
    
    # Формирование данных с информацией о статусе каждой машины
    detailed_info = []
    
    for tracker in trackers:
        tracker_id = tracker['id']
        state = tracker_states.get(str(tracker_id), {})
        connection_status = state.get('connection_status', 'unknown')
        movement_status = state.get('movement_status', 'unknown')
        
        tracker_data = {
            "ID": tracker_id,
            "Label": tracker.get('label', ''),
            "Blocked": tracker.get('source', {}).get('blocked', False),
            "Connection Status": connection_status,
            "Movement Status": movement_status
        }
        
        detailed_info.append(tracker_data)

    # Создание DataFrame и вывод в виде таблицы
    df = pd.DataFrame(detailed_info)
    print(df)

if __name__ == "__main__":
    main()
