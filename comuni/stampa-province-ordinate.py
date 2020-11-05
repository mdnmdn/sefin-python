
# esercizio 5 : Leggere il file di comuni e stampare tutti i nomi delle province ordinate

# f = open('listacomuni.txt')
# file_comuni = f.readlines()
# f.close()

with open('listacomuni.txt') as f:
  file_comuni = f.readlines()

#print(file_comuni)


#  ----------    soluzione 1 ----------------

list_province = []
for riga in file_comuni[1:] :
  campi = riga.split(';')
  if not len(campi) > 1 : 
    continue
  provincia = campi[2]

  provincia_presente = False

  for pr_in_lista in list_province:
    if pr_in_lista == provincia:
      provincia_presente = True
      break

  if not provincia_presente:
    list_province.append(provincia)
    #print(list_province)

#list_province = sorted(list_province) # crea una nuova lista ordinata
list_province.sort() #ordina la lista stessa
print(list_province)

exit()

# ----------  soluzione 2 - list ottimizzata ----------------

list_province = []
for riga in file_comuni[1:] :
  campi = riga.split(';')
  if not len(campi) > 1 : 
    continue
  #provincia = campi[2]
  # estra i dati di un array in variabili, quelle che non ho specificato
  # vengono estratta in un'altra lista "rest" con i valori rimanenti
  [codice, comune, provincia, *rest] = campi

  if provincia in list_province:
    continue

  list_province.append(provincia)


#list_province = sorted(list_province) # crea una nuova lista ordinata
list_province.sort() #ordina la lista stessa
# print(list_province)

# ----------  soluzione 2 - dictionary ----------------

dict_province = {}
for riga in file_comuni[1:]:
  campi = riga.split(';')
  if not len(campi) > 1 : 
    continue
  [codice, comune, provincia, *rest] = campi

  dict_province[provincia] = True

elenco_chiavi = dict_province.keys()
risultato = sorted(elenco_chiavi)

#print('\nelenco_chiavi:\n', elenco_chiavi)
#print('\nrisultato:\n', risultato)


# print('\n', sorted('supercalifragilistichespiralidoso'))





