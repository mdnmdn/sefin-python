# Corso Sefin Python

## Day 1 - Introduzione 

* Notebook [01_tipi_di_dato.ipynb](nb/01_tipi_di_dato.ipynb)
* Notebook [02_strutture_dati.ipynb](nb/02_strutture_dati.ipynb)
* Notebook [03_strutture_complesse_e_ordinamenti.ipynb](nb/03_strutture_complesse_e_ordinamenti.ipynb)


## Day 2 - Funzioni, controlle del flusso e file

* Notebook [04_functions.ipynb](nb/04_functions.ipynb)
* Notebook [05_controllo_del_flusso.ipynb](nb/05_controllo_del_flusso.ipynb)
* Notebook [06_file.ipynb](nb/06_file.ipynb)
* Esercizi [06_esercizi.md](nb/06_esercizi.md)




## Note turbogear


### Prima installazione

Installano le dipendenze di turbogear all'interno di python.

* TurboGears2: framework turbogear
* kajiki: motore di template
* webhelpers2: librerie per semplificare la costruzione di html/web
* tg.devtools: tools di sviluppo di turboger (gearbox)

```
pip install TurboGears2
pip install kajiki
pip install webhelpers2
pip install tg.devtools
```


### Creazione di un nuovo progetto

Da riga di comando nella cartella in cui si vuole creare il nuovo progetto:

```
gearbox quickstart <nome progetto>
```

esempio:

```
gearbox quickstart filmwebapp
```

Crea un nuovo progetto nella cartella "filmwebapp".

```
cd filmwebapp
pip install -e .
```

L'ultima istruzione (pip install -e .) configuta python per poter leggere correttamente le librerie e i moduli interni del nuovo progetto.


### Per avviare il progetto in modalità sviluppo

Dall'interno della cartella del progetto (es filmwebapp)

```
gearbox serve --reload --debug
```