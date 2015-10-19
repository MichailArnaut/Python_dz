import os
all_documents = 0                         # кол-во документов, в которых есть искомое слово
spisok = []                               # список документов с именем и кол-вом искомого слова
files = os.listdir('c:/papka')            # директория поиска
slovo = 'python'                          # слово для поиска
vsego_slov = 0                            # общее колличество найденных слов во всех файлах

for file in files:
    h = open('c:/papka/'+ file).read()       
    if h.count(slovo)>0 :      
        all_documents = all_documents+1        
        spisok.append(file + '\n'+'Колличество слов '+ slovo +' в документе - '+ str(h.count(slovo)))
        vsego_slov = vsego_slov + h.count(slovo)


for k in spisok:
    print(k, '\n')
print ('Документов включают cлово ', slovo, '-',all_documents)
print ('Всего слов',slovo, 'в документах - ', vsego_slov)


file = open('c:/python/result.txt', 'w')
for k in spisok:
    file.write(k + '\n\n')
file.write(str(all_documents) + ' - Документов включают cлово '+ slovo)
file.write('\n\nВсего слов в документах - '+ str(vsego_slov))
file.close()   
