# Introduction

Le script **watermarker** fournit un moyen pratique de **watermarker** une image. Il a été créé pour faciliter le filigrane des images. Vous avez même ma possibilité de watermarker plusieurs images à la fois.

# Installation

1. Installer **python**
2. Installer **python dependencies** avec
   ```
   pip install pillow
   ```
3. Téléchargez **repository** et enregistrez-le où vous voulez.
4. Executer le scrpt avec:
   ```
   python watermarker.py <arguments>
   ```

# Exemples d'utilisation des arguments

Voici quelques exemples qui vous aideront à démarrer. Notez qu'il y a plusieurs façons d'appeler le script **watermarker**.

## Arguments

|              **Argument**              | **Description**                                                                                                                                                                                                                        |
| :------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|               -h,--help                | Afficher l'aide                                                                                                                                                                                                                        |
|              -V,--version              | Afficher la version version                                                                                                                                                                                                            |
|              -v,--verbose              | Activer le verbose mode                                                                                                                                                                                                                |
|      -i `<path>`,--input=`<path>`      | Chemin du fichier input (ou répertoire)                                                                                                                                                                                                |
|     -o `<path>`,--output=`<path>`      | Chemin du fichier output (ou répertoire), Si le input est un fichier, alors la sortie doit être un fichier aussi. même chose pour un répertoire                                                                                        |
|             -O,--overwrite             | Réécriture automatique des fichiers existants                                                                                                                                                                                          |
| --allowext=`<extension1>,<extension2>` | Sélectionner l'extension des fichiers qui seront watermarker. Par défaut c'est png et jpg.                                                                                                                                             |
|         --width=`<new width>`          | Redimensionne l'image sur une nouvelle largeur.                                                                                                                                                                                        |
|        --height=`<new height>`         | Redimensionne l'image sur une nouvelle hauteur.                                                                                                                                                                                        |
|               --preview                | Afficher l'image avant de la sauvegarder.                                                                                                                                                                                              |
|             --ask-to-save              | Demander si nous voulons que l'image soit sauvegarder.                                                                                                                                                                                 |
|           --wpos=`<corner>`            | Sélectionner le coin sur lequel le filigrane sera, les positions disponibles sont: LU - LeftUpperCorner,L - LeftCorner, LD - LeftDownCorner,RU - RightUpperCorner,R - RightCorner,RD - RightDownCorner, U - UpperCorner,D - DownCorner |
|         --wposm=`<margin_px>`          | Définir la marge de la bordure pour le logo en px, à utiliser avec `--wpos`                                                                                                                                                            |
|         --wposx=`<x_coord_px>`         | Coordonnée X de la position du filigrane                                                                                                                                                                                               |
|         --wposy=`<y_coord_px>`         | Coordonnée Y de la position du filigrane                                                                                                                                                                                               |
|        --wimage=`<image_path>`         | Chemin de l'image du filigrane                                                                                                                                                                                                         |
|         --wwidth=`<new width>`         | Redimensionner le filigrane à une nouvelle largeur                                                                                                                                                                                     |
|        --wheight=`<new height>`        | Redimensionner le filigrane à une nouvelle Hauteur                                                                                                                                                                                     |
|       --wtext=`<watermark text>`       | Le texte du filigrane                                                                                                                                                                                                                  |
|        --wcolor=`<text color>`         | La couleur du texte, les formats valides sont `#rrggbb`,`rgb(r,g,b)`,`#rgb`,`hsl(hue,saturation%,lightness%)`,`color_name`                                                                                                             |
|        --wfont=`<path_to_ttf>`         | Chemin du fichier de police                                                                                                                                                                                                            |
|       --wfsize=`<font size pt>`        | Taille de police du texte                                                                                                                                                                                                              |

## Afficher la version

```
watermarker --version
```

## Obtenir de l'aide

```
watermarker --help
```

## Appliquer du watermark avec image (exemple de base - choisir un coin)

Voici un exemple de base. Nous définissons le fichier d'entrée et le fichier de sortie qui peut être omis, alors il écrasera le fichier d'entrée. Nous définissons également le filigrane qui peut être une image (`--wimage`) ou un texte (`--wtext`). Nous devons également spécifier la position du filigrane. Nous définissons dans quel coin le filigrane doit être avec `--wpos` et les marges des frontières avec `--wposm`. Les images du filigrane doivent être des PNG au format RGBA si possible.

```
watermarker --input=input_image.jpg --output=output_image.jpg --wimage watermark_image.png --wpos=LD --wposm 10 --verbose
```

## Appliquer du watermark avec image (exemple étendu - choisir la position)

Ce qui est différent de l'exemple précédent est qu'ici nous spécifions la position absolue du filigrane avec `--wposx` et `--wposy`. Notez que x=0,y=0 est dans le coin supérieur gauche.

```
watermarker --input=input_image.jpg --output=output_image.jpg --wimage watermark_image.png --wposx=10 --wposy=10 --verbose
```

## Appliquer du watermark avec du texte (exemple de base)

Ici, nous filtrons les images avec du texte au lieu des images. Nous utilisons `--wtext`. Nous pouvons aussi changer la couleur du texte avec `--wcolor`. Nous pouvons spécifier la couleur dans différents formats, par exemple `rouge`, `#ff0000`, `rgb(255,0,0)` et plus encore. Il y a aussi une option pour changer la taille du texte `--wfsize`.

```
watermarker --input=input_image.jpg --output=output_image.jpg --wtext Test --wpos U --wposm 100 --wcolor=red --wfsize=32 --verbose
```

## Appliquer du watermark avec du texte (exemple étendu)

Par défaut, le programme utilise la police **Roboto**, mais vous pouvez spécifier un autre fichier **TTF** à l'aide de la commande
`--wfont`.

```
watermarker --input=input_image.jpg --output=output_image.jpg --wtext Test --wpos U --wposm 100 --wcolor=red --wfsize=32 --wfont="fonts/Roboto-Regular.ttf" --verbose
```

## Filigrane des images dans un répertoire

Quelle est la différence ? Il suffit de spécifier des répertoires au lieu de fichiers, le script recherchera récursivement des images et les filtrera selon les paramètres que vous aurez définis.
