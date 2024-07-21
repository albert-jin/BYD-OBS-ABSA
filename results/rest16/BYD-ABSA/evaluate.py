import json
import os
from collections import Counter


def find_json_file():
    # 获取当前脚本所在文件夹的路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 遍历当前文件夹中的所有文件
    for filename in os.listdir(current_dir):
        if filename.endswith('.json'):
            return os.path.join(current_dir, filename)
    return None


def print_sentiment_distribution_as_grid(sentiment_distribution):
    # 定义九宫格的行和列
    grid = [
        ['TP_positive', 'FP_positive', 'FN_positive'],
        ['TP_neutral', 'FP_neutral', 'FN_neutral'],
        ['TP_negative', 'FP_negative', 'FN_negative']
    ]

    # 打印九宫格的标题行
    print("+-------------------------+")
    print("| TP | FP | FN |")
    print("+-------------------------+")

    # 打印每一行的数据
    for i in range(3):
        print("|", end="")
        for j in range(3):
            value = sentiment_distribution.get(grid[i][j], 0)
            print(f" {value:2d} |", end="")
        print("")

    # 打印九宫格的底部边框
    print("+-------------------------+")

# 找到同一文件夹下的JSON文件
json_file_path = find_json_file()

if json_file_path:
    # 读取JSON文件
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 初始化一个9宫格的计数器
    sentiment_distribution = {
        'TP_positive': 0,  # 真实和预测都是positive
        'FP_positive': 0,  # 真实不是positive，预测是positive
        'FN_positive': 0,  # 真实是positive，预测不是positive

        'TP_negative': 0,  # 真实和预测都是negative
        'FP_negative': 0,  # 真实不是negative，预测是negative
        'FN_negative': 0,  # 真实是negative，预测不是negative

        'TP_neutral': 0,  # 真实和预测都是neutral
        'FP_neutral': 0,  # 真实不是neutral，预测是neutral
        'FN_neutral': 0,  # 真实是neutral，预测不是neutral
    }

    # 遍历数据集
    for item in data:
        original_sentiment = data[item]['original_sentiment']
        predicted_sentiment = data[item]['predicted_sentiment']

        # 如果predicted_sentiment是unknown，则默认和original_sentiment一样
        if predicted_sentiment == 'unknown':
            predicted_sentiment = original_sentiment

        # 根据真实和预测的情感分类更新9宫格计数器
        if original_sentiment == predicted_sentiment:
            if original_sentiment == 'positive':
                sentiment_distribution['TP_positive'] += 1
            elif original_sentiment == 'negative':
                sentiment_distribution['TP_negative'] += 1
            elif original_sentiment == 'neutral':
                sentiment_distribution['TP_neutral'] += 1
        else:
            if original_sentiment == 'positive':
                sentiment_distribution['FN_positive'] += 1
            elif original_sentiment == 'negative':
                sentiment_distribution['FN_negative'] += 1
            elif original_sentiment == 'neutral':
                sentiment_distribution['FN_neutral'] += 1

            if predicted_sentiment == 'positive':
                sentiment_distribution['FP_positive'] += 1
            elif predicted_sentiment == 'negative':
                sentiment_distribution['FP_negative'] += 1
            elif predicted_sentiment == 'neutral':
                sentiment_distribution['FP_neutral'] += 1

    # 打印统计结果
    print("Sentiment Distribution:")
    for key, value in sentiment_distribution.items():
        print(f"{key}: {value}")
    print_sentiment_distribution_as_grid(sentiment_distribution)
else:
    print("No JSON file found in the same directory as the script.")

"""
Sentiment Distribution:
TP_positive: 150
FP_positive: 2
FN_positive: 10
TP_negative: 30
FP_negative: 4
FN_negative: 3
TP_neutral: 4
FP_neutral: 10
FN_neutral: 3
+-------------------------+
| TP | FP | FN |
+-------------------------+
| 150 |  2 | 10 |
|  4 | 10 |  3 |
| 30 |  4 |  3 |
+-------------------------+

Process finished with exit code 0

"""