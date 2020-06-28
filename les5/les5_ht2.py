'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''
file = open('les5_ht2_test.txt', 'r')
content = file.readlines()

for idx, item in enumerate(content, 1):
    line = item.split()
    words = len(line)
    print('В строке ({}) - {} слов(а)'.format(item, words))
print('\n В файле всего {} строк.'.format(len(content)))
file.close()