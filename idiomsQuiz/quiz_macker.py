#!/usr/bin/env python3

from bs4 import BeautifulSoup as bs
import requests
import random
import idioms_gui
def quiz_maker(Q=5):
  category = 'common-english-idioms'
  # category = 'Common-English-Idioms'
  # category = 'Familiar-English-Idioms'
  # category = 'Idioms-About-Age'
  # category = 'Idioms-About-Art'
  # print(category)
  website = requests.get(f'https://www.wordscoach.com/idioms?category={category}').text
  soup  = bs(website,'lxml')

  idioms_list = soup.find_all('div', class_ = 'list-content')
  idioms = {}

  for idiom in idioms_list:
    for index, element in enumerate(idiom.p):
      if index == 1:
        idioms[idiom.a['title'].strip()] = element.strip()

  keys = list(idioms.keys())
  dict_values = list(idioms.values())
  quiz = {}
  for _ in range(Q):
    item = random.randrange(len(keys))
    options = {}
    values = []
    answer = idioms[keys[item]]
    while len(values) != 3:
      value = random.choice(dict_values)
      if value != answer:
        values.append(value)
    values.append(answer)
    random.shuffle(values)
    for index, letter in enumerate('ABCD'):
      options.update({letter:values[index]})
    quiz.update({keys[item]:options})
    del keys[item]
  return quiz

print(quiz_maker())