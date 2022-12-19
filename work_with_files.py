var = input('Write something')
fw = open('doc/file.txt', 'a')
fw.write(var)
fw.close()

a - запись новых данных в конец старых
w - запись новых данных (удаляя старые данные)
