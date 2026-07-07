# Pascal's Triangle

## Description

Ce projet consiste à générer le **triangle de Pascal** sous forme d'une liste de listes d'entiers.

Le triangle de Pascal est une suite de nombres organisée en lignes où chaque nombre intérieur est obtenu en additionnant les deux nombres situés directement au-dessus de lui. Les bords du triangle sont toujours composés de `1`.

## Prototype

```python
def pascal_triangle(n)
```

## Contraintes

* `n` est toujours un entier.
* La fonction retourne une liste de listes représentant les `n` premières lignes du triangle de Pascal.
* Si `n <= 0`, la fonction retourne une liste vide.

## Exemple

Entrée :

```python
pascal_triangle(5)
```

Sortie :

```python
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
```

Affichage :

```text
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

## Algorithme

Pour construire le triangle :

1. Si `n <= 0`, retourner une liste vide.
2. Créer la première ligne contenant uniquement `1`.
3. Pour chaque nouvelle ligne :

   * Ajouter un `1` au début et à la fin.
   * Calculer les valeurs intermédiaires en additionnant les deux nombres adjacents de la ligne précédente.
4. Retourner la liste complète du triangle.

## Exécution

Le fichier principal de test utilise :

```python
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle
```

Pour lancer le test :

```bash
./0-main.py
```

Exemple de résultat :

```text
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

## Fichier principal

La fonction demandée se trouve dans :

```text
0-pascal_triangle.py
```

## Auteur

Projet réalisé dans le cadre du cursus Holberton School par Rawan.

