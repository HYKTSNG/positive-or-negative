'''tweetのポジネガ判定'''

import oseti
import analysis_json


def judge():

    analyzer = oseti.Analyzer()
    tweets = analysis_json.analysis_json()
    positive_or_negative = 0

    print("\n-----------------------------\n")

    for t in tweets:
        print(t)
        print(analyzer.analyze_detail(t))
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
    judge()
