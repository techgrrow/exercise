# Prova pratica

### l’obiettivo della prova e’ quello di creare un’applicazione in Python eseguibile da linea di comando per la gestione di una todo list. Le azioni permesse all’utente sono le seguenti:

**h** >>> mostra tutti le possibili action  
**ls** >>> mostra tutti i todos ordinati per data di inserimento decrescente  
**a (params: title)** >>> aggiunge un todo  
**e (params: id, title)** >>> edita un todo  
**d (params: id)** >>> cancella un todo  
**t (params: id)** >>> fa il toggle del todo (done: true VS done: false)  
**s (params: il termine da cercare)** >>> cerca tra i todos e ritorna i todos
contenenti il termine ricercato nel titolo  

**Esempi d’uso:**  
$ todo_manager a “Titolo1”  
$ todo_manager a “Titolo2”  
$ todo_manager s “Titolo”  
[{id: 0, title: “Titolo1”, done: False, timestamp: 1568799307}, {id: 1,
title: “Titolo2”, done: False}]  
$ todo_manager t 0  
$ todo_manager s “Titolo”  
[{id: 0, title: “Titolo1”, done: True, timestamp: 1568799308}, {id: 1,
title: “Titolo2”, done: False}]  
$ todo_manager e 0 “Titolanza”  
$ todo_manager s “Titolo”  
[{id: 1, title: “Titolo2”, done: False, timestamp: 1568799308}]  
$ todo_manager d 0  
$ todo_manager s “Titolo”  
[]  

I vari todos dovranno essere persistiti in **un file di testo** usando una
struttura a piacere e congeniale al design adottato e che comunque preveda,
per ognuno dei todo presenti nel sistema, le seguenti proprietà:

- titolo
- timestamp creazione
- done (not done)

#### E’ richiesta l’implementazione di un semplice layer di validazione in cui viene verificato che il titolo abbia una lunghezza di almeno 5 caratteri.

#### Bonus: unit testing delle principali classi progettate per la gestione dei diversi layers dell’applicazione (es: parsing dell’input, validazione, actions, persistenza).


