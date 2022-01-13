import json

def status(list_id):
    if list_id == 1:
        return 'watching'
    elif list_id == 2:
        return 'planned'
    elif list_id == 3:
        return 'completed'
    elif list_id == 4:
        return 'completed'
    elif list_id == 5:
        return 'dropped'

with open('anime-list.json', encoding="utf-8") as json_file:
    data = json.load(json_file)
    for el in data:
        el['target_title'] = el['title']
        el['target_type'] = 'Anime'
        el['status'] = status(el['list_id'])
        el['rewatches'] = 0
        el['text'] = None
        del el['ya_id']
        del el['list_id']
        del el['title']
        del el['updated_at']


with open('result_list.json', "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False)
