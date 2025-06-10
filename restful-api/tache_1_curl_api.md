
# 📡 Tâche 1 : Consommer des données d'une API avec curl

## ✅ Objectifs
- Utiliser `curl` en ligne de commande pour interagir avec une API REST
- Envoyer des requêtes GET et POST
- Lire les entêtes HTTP

---

## 1. 📥 Vérification de l'installation de `curl`

### Commande :
```bash
curl --version
```

### Résultat attendu (exemple) :
```
curl 7.68.0 (x86_64-pc-linux-gnu) libcurl/7.68.0 OpenSSL/1.1.1f zlib/1.2.11
...
```

---

## 2. 🌍 Récupération d'une page web simple

### Commande :
```bash
curl http://example.com
```

### Résultat attendu :
- Code HTML de la page `example.com`

---

## 3. 🔎 Récupération de données via API (GET)

### Commande :
```bash
curl https://jsonplaceholder.typicode.com/posts
```

### Résultat attendu (extrait) :
```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit..."
  },
  ...
]
```

---

## 4. 🧾 Obtenir uniquement les entêtes HTTP

### Commande :
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

### Résultat attendu (exemple) :
```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 29200
...
```

---

## 5. 📝 Envoyer des données avec une requête POST

### Commande :
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

### Résultat attendu :
```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```

---

## 📌 Résumé
- `curl` permet de simuler des requêtes HTTP simples depuis le terminal
- `GET` = lire des données, `POST` = envoyer des données
- `-I` = ne récupère que les en-têtes de réponse
- Très utile pour tester des API REST rapidement
