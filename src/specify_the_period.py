'''
jsonファイルにアクセスし整形する
'''

import json
from collections import defaultdict
import text_shaping


def clear_text_list_and_time_list():
    '''
    jsonファイルを取得。
    text_shaping.pyに渡す。
    整形されたテキストlistと
    整形された時間のlistを取得。
    '''
    user_tweets = "@MpYcgEiS8peCbqq.json"
    f = open(user_tweets, "r", encoding="utf-8")

    data = json.load(f)
    clear_text_list = []
    time_list = []

    for v in data.values():
        clear_text = text_shaping.format_text(v)
        if clear_text != "":
            clear_text_list.append(clear_text)
    # print(clear_text_list)

    for k in data.keys():
        temp_time = k.split()[0]
        time_list.append(temp_time)

    return clear_text_list, time_list


def json_to_dict():

    clear_text_list = clear_text_list_and_time_list()[0]
    time_list = clear_text_list_and_time_list()[1]
    # -----------------------------
    time_and_text_dict = defaultdict(list)

    for a in range(len(clear_text_list)):
        time_and_text_dict[time_list[a]].append(clear_text_list[a])

    # print(type(time_and_text_dict))
    # print(time_and_text_dict)

    print("\n以下が取得した期間です")
    print("\n-----------------------------")

    for i, tatd in enumerate(time_and_text_dict):
        print(i, ":", tatd)

    for tatd in time_and_text_dict:
        # print(time_and_text_dict[tatd])
        pass

    return time_and_text_dict


if __name__ == '__main__':
    json_to_dict()
