
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
class Article:
    def __init__(self, id, title):
        self.id = id
        self.title = title


some_list = []
for i in range(1, 5):
    some_list.append(Article(id=i, title="article{}".format(i)))
    print("id = {0} title = {1}".format(some_list[i - 1].id, some_list[i - 1].title))
FIND = 2

for i in some_list:
    print(i.title)