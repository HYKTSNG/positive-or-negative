import oseti

analyzer = oseti.Analyzer()

text = '遅刻したけど楽しかったし嬉しかった。すごく充実した！'
print(analyzer.analyze(text))
# print(analyzer.analyze('遅刻したけど楽しかったし嬉しかった。すごく充実した！'))
# # => [0.3333333333333333, 1.0]

# print(analyzer.count_polarity('遅刻したけど楽しかったし嬉しかった。すごく充実した！'))
# # => [{'positive': 2, 'negative': 1}, {'positive': 1, 'negative': 0}])
# print(analyzer.count_polarity('そこにはいつもと変わらない日常があった。'))
# # => [{'positive': 0, 'negative': 0}]

# print(analyzer.analyze_detail('お金も希望もない！'))
# # => [{'positive': [], 'negative': ['お金-NEGATION', '希望-NEGATION'], 'score': -1.0}])
# print(analyzer.analyze_detail('お金がないわけではない'))
# # => [{'positive': ['お金'], 'negative': [], 'score': 1.0}]
