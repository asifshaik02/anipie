from flask import Flask
from tracker import Anilist, Anime, Character, User, Manga, get_shedule

app = Flask(__name__)

@app.route('/')
def index():
    return ""

@app.route("/user/<name>")
def profile(name):
    user = User(name)
    return user.__dict__

@app.route('/<name>/<type>/<status>/<int:page>')
def get_watch_list(name,type,status,page):
    user = User(name)
    return user.get_watch_list(type.upper(),status.upper(),page)

@app.route("/anime/<int:id>")
def get_anime_details(id):
    return Anime(id).__dict__

@app.route("/manga/<int:id>")
def get_manga_details(id):
    return Manga(id).__dict__

@app.route("/character/<int:id>")
def get_char_details(id):
    return Character(id).__dict__

@app.route("/shedule")
def shedule():
    return get_shedule()

@app.route("/search/<query>/<int:page>")
def search(query,page):
    return Anilist().searchMedia(query,page)

@app.route("/search/<query>")
def search_first(query):
    return search(query,1)

if __name__ == "__main__":
    app.run(debug=True)