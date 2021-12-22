'''
期間指定があった時のtweetのポジネガ判定

まだ何もしてない。

'''

import oseti
import analysis_json


def period_judge():

    analyzer = oseti.Analyzer()
    tweets = analysis_json.analysis_json()
    positive_or_negative = 0

    print("\n-----------------------------\n")

    for i, t in enumerate(tweets):
        print(i, ":", t)
        # print(analyzer.analyze_detail(t))
        positive_or_negative += sum(analyzer.analyze(t))

    print("\n", positive_or_negative)

    if 0 < positive_or_negative:
        print("positive")
    elif 0 > positive_or_negative:
        print("negative")
    else:
        print("neutral")

    print("\n-----------------------------")


if __name__ == '__main__':
    period_judge()
