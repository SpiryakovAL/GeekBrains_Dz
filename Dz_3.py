#Урок 3

print ('Задача №1 Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.')

def num_translate ():
    translate_val = input ('Введите на английском числительное от 0 до 10: ')
    print(my_dict.get(translate_val))

my_dict = {'one':'один', 'two':'два', 'three':'три', 'four':'четыре', 'five':'пять', 'six':'шесть', 'seven':'семь',
           'eight':'восемь', 'nine':'девять', 'ten':'десять'}

num_translate()

print ('\nЗадача №3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников\n'
       'и возвращающую словарь,в котором ключи — первые буквы имён, а значения — списки, содержащие имена,\n'
       'начинающиеся с соответствующей буквы.\n\n')

def thesaurus(*args):
    namelst = list(map(str,args))
    n_dict = {}
    for name in namelst:
        one_sign = name[0]
        n_dict[one_sign]=n_dict.get(one_sign,[])+[name]
    print (n_dict)

thesaurus("Иван", "Мария", "Петр", "Илья")

print ('\n\nЗадача №5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,\n'
       'взятых из трёх списков (по одному из каждого)\n\n')

from random import randrange

def get_jokes(new):
    joke_lst = []
    for joke in range(new):
        joke = ' '.join([nouns[randrange(len(nouns))], adverbs[randrange(len(adverbs))], adjectives[randrange(len(adjectives))]])
        joke_lst.append(joke)
    print (*joke_lst, sep = ', ')
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(3)
