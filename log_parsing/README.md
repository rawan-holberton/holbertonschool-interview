# Log Parsing

## Description

Ce projet consiste à créer un script capable de lire des logs serveur depuis l'entrée standard (`stdin`) et de calculer des statistiques en temps réel.

Le programme analyse chaque ligne de log afin d'extraire :

* La taille totale des fichiers demandés.
* Le nombre d'apparitions de chaque code de statut HTTP.

Les statistiques sont affichées automatiquement après chaque groupe de **10 lignes traitées** et également lorsqu'une interruption clavier (`CTRL + C`) est détectée.

## Fichier principal

Le script demandé est :

```text
0-stats.py
```

## Format des logs attendu

Chaque ligne doit respecter le format suivant :

```text
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

Exemple :

```text
192.168.1.10 - [2026-07-07] "GET /projects/260 HTTP/1.1" 200 512
```

Les lignes ne correspondant pas à ce format sont ignorées.

## Fonctionnement

Le programme :

1. Lit les lignes une par une depuis `stdin`.
2. Extrait :

   * Le code de statut HTTP.
   * La taille du fichier.
3. Additionne toutes les tailles de fichiers valides.
4. Compte le nombre d'occurrences de chaque code HTTP.
5. Affiche les statistiques :

   * Après chaque 10 lignes.
   * Lorsqu'une interruption `CTRL + C` est envoyée.

## Codes HTTP supportés

Les codes analysés sont :

* `200`
* `301`
* `400`
* `401`
* `403`
* `404`
* `405`
* `500`

Les codes qui n'apparaissent pas ne sont pas affichés.

Les codes sont toujours affichés dans l'ordre croissant.

## Exemple

Commande :

```bash
./0-generator.py | ./0-stats.py
```

Sortie possible :

```text
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
```

Après une interruption :

```text
^C
File size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

## Exécution

Rendre les fichiers exécutables :

```bash
chmod +x 0-stats.py
```

Lancer le programme :

```bash
./0-stats.py
```

Ou avec un générateur de logs :

```bash
./0-generator.py | ./0-stats.py
```

## Contraintes techniques

* Compatible avec **Ubuntu 14.04 LTS**.
* Utilise **Python 3.4.3**.
* Le fichier commence obligatoirement par :

```python
#!/usr/bin/python3
```

* Respect du style **PEP 8**.
* Le code ne doit pas être exécuté lors d'un import du module.

## Algorithme

Le script utilise :

* Une lecture continue avec `sys.stdin`.
* Des expressions régulières pour valider et extraire les informations des logs.
* Un dictionnaire pour stocker le nombre d'occurrences des codes HTTP.
* Une gestion d'exception `KeyboardInterrupt` pour afficher les statistiques finales avant l'arrêt du programme.


## Auteur

Projet réalisé dans le cadre du cursus Holberton School par Rawan.

