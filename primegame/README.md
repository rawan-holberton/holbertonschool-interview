# Prime Game

## Description

**Prime Game** est un exercice algorithmique dans lequel deux joueurs, **Maria** et **Ben**, jouent plusieurs manches en retirant des nombres premiers et leurs multiples d'un ensemble d'entiers.

L'objectif est de déterminer quel joueur remporte le plus de manches, en supposant que les deux jouent de manière optimale.

---

## Règles du jeu

Pour chaque manche :

- On dispose d'un ensemble d'entiers allant de **1 à n**.
- **Maria** joue toujours en premier.
- À son tour, un joueur choisit un **nombre premier** encore présent dans l'ensemble.
- Ce nombre premier ainsi que **tous ses multiples** sont supprimés de l'ensemble.
- Les joueurs jouent alternativement jusqu'à ce qu'il ne reste plus de nombre premier.
- Le joueur qui ne peut plus effectuer de coup perd la manche.

Après avoir joué toutes les manches, la fonction doit retourner le nom du joueur ayant remporté le plus de victoires.

---

## Prototype

```python
def isWinner(x, nums)
```

### Paramètres

- `x` : nombre de manches jouées.
- `nums` : liste contenant la valeur de `n` pour chaque manche.

### Retour

- `"Maria"` si Maria remporte le plus de manches.
- `"Ben"` si Ben remporte le plus de manches.
- `None` en cas d'égalité ou si le gagnant ne peut être déterminé.

---

## Exemple

```python
x = 3
nums = [4, 5, 1]

print(isWinner(x, nums))
```

Résultat :

```text
Ben
```

---

## Approche

Pour résoudre efficacement le problème :

1. Générer tous les nombres premiers jusqu'au plus grand `n` à l'aide du **crible d'Ératosthène**.
2. Calculer le nombre de nombres premiers présents jusqu'à chaque valeur de `n`.
3. Observer que :
   - si le nombre de nombres premiers est **impair**, Maria gagne la manche ;
   - s'il est **pair**, Ben gagne.
4. Compter les victoires sur l'ensemble des manches.

Cette approche permet d'éviter de simuler chaque partie, ce qui améliore considérablement les performances.

---

## Contraintes

- Ubuntu 14.04 LTS
- Python 3.4.3
- Aucun package externe autorisé
- Respect de la norme **PEP 8**
- Tous les fichiers doivent être exécutables.

---

## Structure du projet

```
primegame/
│
├── 0-prime_game.py    # Implémentation de isWinner()
└── README.md
```

---

## Auteur

Projet réalisé dans le cadre du programme **Holberton School**.
