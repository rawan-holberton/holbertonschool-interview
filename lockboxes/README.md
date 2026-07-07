# Lockboxes

## Description

Ce projet consiste à résoudre le problème des **boîtes verrouillées** (*Lockboxes*).

On dispose de `n` boîtes numérotées de `0` à `n - 1`. Chaque boîte peut contenir des clés permettant d'ouvrir d'autres boîtes. La première boîte (`boxes[0]`) est toujours ouverte.

L'objectif est de déterminer si toutes les boîtes peuvent être ouvertes en utilisant uniquement les clés disponibles dans les boîtes déjà ouvertes.

## Prototype

```python
def canUnlockAll(boxes)
```

## Contraintes

* `boxes` est une liste de listes.
* Chaque clé correspond au numéro d'une boîte.
* Les clés sont des entiers positifs.
* Certaines clés peuvent correspondre à des boîtes inexistantes.
* La première boîte (`boxes[0]`) est toujours déverrouillée.
* La fonction retourne :

  * `True` si toutes les boîtes peuvent être ouvertes.
  * `False` sinon.

## Exemple

```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))
```

Résultat :

```
True
```

Explication :

* La boîte 0 contient la clé de la boîte 1.
* La boîte 1 contient la clé de la boîte 2.
* La boîte 2 contient la clé de la boîte 3.
* La boîte 3 contient la clé de la boîte 4.
* Toutes les boîtes peuvent donc être ouvertes.

Autre exemple :

```python
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
```

Résultat :

```
False
```

Certaines boîtes restent inaccessibles.

## Algorithme

La solution utilise un parcours de graphe :

1. La boîte `0` est considérée comme déjà ouverte.
2. On parcourt les clés trouvées dans les boîtes ouvertes.
3. Lorsqu'une clé correspond à une boîte valide qui n'a pas encore été ouverte, on ajoute cette boîte à la liste des boîtes accessibles.
4. À la fin du parcours, on vérifie si toutes les boîtes ont été ouvertes.

Cette approche permet d'explorer toutes les boîtes atteignables depuis la première boîte.

## Exécution

Le fichier principal contient la fonction :

```
0-lockboxes.py
```

Pour tester le programme :

```bash
./main_0.py
```

Exemple de sortie :

```
True
True
False
```

## Auteur

Projet réalisé dans le cadre du cursus Holberton School par Rawan

