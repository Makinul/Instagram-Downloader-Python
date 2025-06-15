from flask import Flask, request, jsonify
import instaloader

app = Flask(__name__)

@app.route('/get-instagram-video', methods=['GET'])
def get_instagram_video():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "Missing 'url' parameter"}), 400

    try:
        # Extract shortcode from URL
        if "instagram.com" in url:
            parts = url.strip("/").split("/")
            shortcode = parts[-1] if parts[-1] else parts[-2]
        else:
            shortcode = url

        # Load post
        L = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(L.context, shortcode)

        if post.is_video:
            return jsonify({
                "video_url": post.video_url,
                "caption": post.caption,
                "thumbnail_url": post.url
            })
        else:
            return jsonify({"error": "Not a video post"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)