
# 🌐 Tâche 0 : Les bases de HTTP/HTTPS

## ✅ Objectifs
- Comprendre la différence entre HTTP et HTTPS
- Connaître la structure d'une requête et réponse HTTP
- Identifier les méthodes HTTP principales
- Retenir les codes de statut HTTP courants

---

## 1. 🔐 HTTP vs HTTPS

| Protocole | Sécurisé ? | Fonctionnement |
|-----------|------------|----------------|
| HTTP      | ❌ Non     | Communication en texte clair |
| HTTPS     | ✅ Oui     | Utilise SSL/TLS pour chiffrer les échanges |

➡️ **HTTPS est obligatoire** pour les sites sensibles (banque, e-commerce, connexions, etc.)

---

## 2. 📨 Structure d'une requête HTTP (exemple)

### Requête :
```
GET /index.html HTTP/1.1
Host: www.exemple.com
User-Agent: Mozilla/5.0
```

### Réponse :
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 345

<html>...</html>
```

---

## 3. 🔨 Méthodes HTTP courantes

| Méthode | Description | Exemple |
|--------|-------------|---------|
| GET    | Récupérer une ressource | Lire un article |
| POST   | Créer une nouvelle ressource | Envoyer un formulaire |
| PUT    | Mettre à jour une ressource complète | Modifier un profil |
| DELETE | Supprimer une ressource | Supprimer un compte |

---

## 4. ⚠️ Codes de statut HTTP

| Code | Signification           | Quand ?                              |
|------|--------------------------|--------------------------------------|
| 200  | OK                       | Tout s'est bien passé                |
| 201  | Created                  | Une ressource a été créée            |
| 400  | Bad Request              | Requête malformée                    |
| 404  | Not Found                | Ressource introuvable                |
| 500  | Internal Server Error    | Erreur côté serveur                  |

---

## 5. 💡 Astuce pratique

➡️ Utiliser les outils de développement (F12 > "Network") pour observer les requêtes HTTP sur n’importe quel site web.

➡️ Ou essayer en ligne de commande :
```bash
curl -i https://jsonplaceholder.typicode.com/posts/1
```

---

## 📌 Résumé
- HTTP = communication non chiffrée, HTTPS = sécurisé
- Requête = méthode + chemin + en-têtes
- Réponse = code de statut + contenu
- Bien connaître les méthodes et les codes les plus fréquents
