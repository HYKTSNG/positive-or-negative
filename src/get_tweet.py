'''特定のアカウントのtweetを取ってくるファイル'''

import sys
import json
from define_client import define_client_proc
from datetime import datetime


# --------------------------------------------------------------------
def get_tweets_proc(client, screen_name):
    nnx = 3000
    url_base = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name='
    url = url_base + screen_name + "&count=" + str(nnx) + "&include_rts=False"
    array_aa = []
    response, data = client.request(url)
    if response.status == 200:
        json_str = data.decode('utf-8')
        array_aa = json.loads(json_str)
    else:
        sys.stderr.write("*** error *** get_ids_proc ***\n")
        sys.stderr.write("Error: %d\n" % response.status)
    return array_aa


def get_tweet():
    print("検索したい人のscreen_nameを@から入力してください")
    screen_name = str(input())
    sys.stderr.write("*** 開始 ***\n")
    client = define_client_proc()
    array_aa = get_tweets_proc(client, screen_name)
    print("user_id : ", screen_name)

    # json出力
    test_dict: dict = {}
    i = 0
    for unit_aa in array_aa:
        #  日本時間に直す
        tweet = {'create_at': unit_aa['created_at']}
        dt = datetime.strptime(tweet['create_at'], '%a %b %d %H:%M:%S %z %Y')
        dt = dt.astimezone()
        dst = datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')

        test_dict[dst] = unit_aa['text']
        i += 1

    with open(screen_name + ".json", "w", encoding="utf-8") as fp:
        json.dump(test_dict, fp, indent=4, ensure_ascii=False)

    sys.stderr.write("*** 取得完了 ***\n\n")


if __name__ == '__main__':
    get_tweet()
