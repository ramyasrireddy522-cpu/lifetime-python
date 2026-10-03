from flask import Flask, send_from_directory

# The website files (HTML, CSS, jQuery, images) live in the "site" folder
app = Flask(__name__, static_folder="site", static_url_path="")


@app.route("/")
def home():
    return send_from_directory("site", "index.html")


if __name__ == "__main__":
    app.run(debug=True)
