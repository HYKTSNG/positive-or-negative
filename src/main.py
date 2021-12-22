import get_tweet
import judge
import period_judge
import analysis_json


def main():

    get_tweet.get_tweet()

    # 新しいファイルを作成 → judge.pyかperiod_judge.py かどっちかを実行する

    # period_judge.period_judge()
    judge.judge()
    # analysis_json.analysis_json()


main()

# 実行
# poetry run task main
# @MpYcgEiS8peCbqq
