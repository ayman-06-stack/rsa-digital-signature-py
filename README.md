# Flask Digital Signature TP

>Une implémentation pratique de la **signature électronique** et de la **vérification** utilisant Python, Flask et la cryptographie RSA.

---

## Sommaire
* [Objectifs](#-objectifs)
* [Architecture](#-architecture)
* [Installation](#-installation)
* [Utilisation](#-utilisation)
* [Théorie](#-théorie)

---

## Objectifs
[cite_start]Ce projet permet de maîtriser les concepts suivants:
- [x] Génération de paires de clés RSA (Privée/Publique).
- [x] Hachage de documents avec SHA-256.
- [x] Signature numérique avec clé privée.
- [x] Vérification d'intégrité avec clé publique.

---

## 🏗️ Architecture
L'organisation du projet suit une structure Flask standard:

| Dossier/Fichier | Description |
| :--- | :--- |
| `app.py` | Serveur Flask et logique métier (Sign/Verify). |
| `generate_keys.py` | Script de création des clés PEM. |
| `keys/` | Stockage sécurisé des clés RSA. |
| `templates/` | Interfaces utilisateur HTML. |
| `uploads/` | Stockage temporaire pour les signatures générées. |

---

## 🛠️ Installation

1. **Cloner le projet**
   ```bash
   git clone [https://github.com/VOTRE_NOM/py-signature-rsa.git](https://github.com/VOTRE_NOM/py-signature-rsa.git)
   cd py-signature-rsa
2. **Installer les dépendances**
   ```bash
   pip install flask cryptography
3. **Générer les clés**
   ```bash
   python generate_keys.py
4. **Lancer le serveur**
   ```bash
   python app.py
**Rendez-vous sur http://127.0.0.1:5000, uploadez un fichier et récupérez son fichier de signature .bin**
