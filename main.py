from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

data = load_candidates_from_json()


@app.route("/")
def main_page():
    return render_template("list.html", candidates=data)


@app.route("/candidate/<int:id>")
def profile_page(id):
    candidate = get_candidate(id)
    return render_template("single.html", user=candidate)


@app.route("/search/<candidate_name>")
def name_page(candidate_name):
    name = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=name, candidate_len=len(name))


@app.route("/skill/<skill_name>")
def skill_page(skill_name):
    candidate = get_candidates_by_skill(skill_name)
    return render_template("skill.html", candidates=candidate, candidate_len=len(candidate), candidate_skill=skill_name)


app.run()
