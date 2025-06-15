# 📸 Instagram Reel Downloader API (Python + Flask + Instaloader)

This project is a simple backend API built with **Flask** that fetches the direct video URL, thumbnail, and caption (if available) of a given **Instagram post or reel**.

---

## 🚀 Features

- 🔗 Accepts a public Instagram post or reel URL
- 🎞 Returns:
  - Direct `video_url`
  - `thumbnail_url`
  - `title` (caption, if available)
- 🌐 Deployable to **Google Cloud Run**
- 🔐 Optional: Login support for private post metadata (like captions)

---

## 🧩 Technologies Used

| Tech           | Purpose                          |
|----------------|----------------------------------|
| **Flask**      | Lightweight Python web framework |
| **Instaloader**| Extract post metadata & video URL|
| **Gunicorn**   | WSGI server for production        |
| **Docker**     | Containerize the app             |
| **Google Cloud Run** | Deploy and host the API   |

---

## 🛠 How It Works

1. You send a `GET` request to the `/get-instagram-video` endpoint with a query param:
2. The backend:
- Parses the shortcode from the URL
- Uses `instaloader` to fetch the post
- Extracts the `video_url`, `thumbnail_url`, and `caption` (if available)

3. Responds with JSON like:

```json
{
  "video_url": "https://...",
  "thumbnail_url": "https://...",
  "title": "Your caption here"
}
