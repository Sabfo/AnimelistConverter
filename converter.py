import json


with open('anime-list.json', encoding="utf-8") as json_file:
    data = json.load(json_file)
    for el in data:
        el['target_type'] = 'Anime'
        el['status'] = 'completed'
        el['rewatches'] = 0
        el['text'] = None
        del el['ya_id']
        del el['list_id']
        del el['updated_at']


with open('result_list.json', "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False)
