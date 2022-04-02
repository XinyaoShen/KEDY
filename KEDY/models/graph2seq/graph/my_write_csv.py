import json
import csv
import jieba

f = open('../data/all_clean_data.txt')
text = f.read().split('\n')
field_names = ['label', 'content', 'concepts', 'title']
train_csv_writer = csv.DictWriter(open('../data/train_graph_data.csv', 'w'), fieldnames=field_names,
                                  delimiter='|', quotechar='\"', quoting=csv.QUOTE_ALL)
dev_csv_writer = csv.DictWriter(open('../data/dev_graph_data.csv', 'w'), fieldnames=field_names, delimiter='|',
                                quotechar='\"', quoting=csv.QUOTE_ALL)
test_csv_writer = csv.DictWriter(open('../data/test_graph_data.csv', 'w'), fieldnames=field_names, delimiter='|',
                                 quotechar='\"', quoting=csv.QUOTE_ALL)
train_csv_writer.writeheader()
dev_csv_writer.writeheader()
test_csv_writer.writeheader()

cnt = 0

for line in text:
    if(cnt >= 820000):
        break
    data = json.loads(line)
    querys = data['query']
    content = ' '.join(data['content'])
    title = data['title']
    concepts = jieba.analyse.textrank(content, topK=8, withWeight=False, allowPOS=(‘ns’, ‘n’, ‘vn’, ‘v’))
    concepts_cut = []
    for concept in concepts:
        concepts_cut.append(' '.join(jieba.cut(concept)))
    if cnt < 10000:
        test_csv_writer.writerow({'label': '$$'.join([' '.join(jieba.cut(query)) for query in querys]), 'content': ' '.join(jieba.cut(content)),
                                       'concepts': ','.join(concepts_cut),
                                       'title': ' '.join(jieba.cut(title))})
    elif cnt < 20000:
        dev_csv_writer.writerow(
            {'label': '$$'.join([' '.join(jieba.cut(query)) for query in querys]),
             'content': ' '.join(content), 'concepts': ','.join(concepts_cut),
             'title': ' '.join(jieba.cut(title))})
    else:
        train_csv_writer.writerow(
            {'label': ' '.join(jieba.cut(query)),
             'content': ' '.join(content), 'concepts': ','.join(concepts_cut),
             'title': ' '.join(jieba.cut(title))})
    cnt = cnt + 1