**Jeu de Quiz sur les Capitales**
==============================

Ce code permet de jouer à un jeu de quiz sur les capitales des pays. Le jeu tire au hasard 5 pays parmi un fichier JSON contenant des informations sur les pays et leurs capitales.

**Fonctionnement**
---------------

1. Le code charge le fichier JSON `pays.json` qui contient des informations sur les pays et leurs capitales.
2. Il sélectionne au hasard 5 pays parmi la liste des pays.
3. Pour chaque pays sélectionné, le code demande à l'utilisateur de saisir la capitale du pays.
4. Si l'utilisateur répond correctement, le code affiche un message de félicitations et incrémente le score.
5. Si l'utilisateur répond incorrectement, le code affiche la bonne réponse et ne modifie pas le score.
6. À la fin du jeu, le code affiche le score final de l'utilisateur.

**Fichier JSON**
--------------

Le fichier JSON `pays.json` doit contenir des informations sur les pays et leurs capitales sous la forme suivante :
```json
{
  "pays": [
    {
      "nom": "Afghanistan",
      "capitale": "Kaboul"
    },
    {
      "nom": "Afrique du Sud",
      "capitale": "Pretoria, Le Cap, Bloemfontein"
    },
    {
      "nom": "Albanie",
      "capitale": "Tirana"
    },
  ]
}
```

**Résultat**
------------

Le code affichera le score final de l'utilisateur sous la forme suivante :
```
Votre score est de X/5
```
où X est le nombre de réponses correctes.
