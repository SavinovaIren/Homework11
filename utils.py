import json


# load_candidates_from_json() – возвращает список всех кандидатов
def load_candidates_from_json():
    global _data
    with open('candidates.json', 'r', encoding='utf-8') as file:
        _data = json.load(file)
        return _data


# get_candidate(candidate_id) – возвращает одного кандидата по его id
def get_candidate(candidate_id):
    for candidate in _data:
        if candidate["id"] == candidate_id:
            return {
                "name": candidate["name"],
                "position": candidate["position"],
                "picture": candidate["picture"],
                "skills": candidate["skills"],
            }


# get_candidates_by_name(candidate_name) – возвращает кандидатов по имени
def get_candidates_by_name(candidate_name):
    return [candidate for candidate in _data if candidate_name in candidate["name"].lower()]


# get_candidates_by_skill(skill_name) – возвращает кандидатов по навыку
def get_candidates_by_skill(skill_name):
    list_of_skills = []
    for candidate in _data:
        list = candidate["skills"].lower().split(", ")
        if skill_name in list:
            list_of_skills.append(candidate)
    return list_of_skills
