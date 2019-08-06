# Homework Python advanced 1.1 (Iterators. Generators. Yield)

##### Задание: 
https://github.com/netology-code/py-homework-advanced/tree/master/1.2.Iterators.Generators.Yield

## В данной работе:

#### Модуль ***wiki.py***
Класс итератора ```WikiUrls```:
* Считывает содержимое файла ```source/countries.json```
* При каждой итерации получет wiki-ссылку для страны из содержимого файла ```countries.json``` и записывает в файл ```output/wiki_urls.txt``` строку вида: Наименование страны - wiki-ссылка.
 

#### Модуль ***hash.py***
* Генератор ```mdfive_string()```. На вход принимает путь к файлу.
* При каждой итерации возвращает md5 хеш каждой строки файла.
* Для примера выводится хэш строк файла ```output/wiki_urls.txt```
