import datetime
import requests
from flask import Flask,render_template

app = Flask(__name__)


def getAge(name):
    response = requests.get(url=f"https://api.agify.io?name={name}")
    age = response.json()['age']
    return age


def getGender(name):
    response = requests.get(url=f"https://api.genderize.io?name={name}")
    gender_response = response.json()
    return gender_response['gender']

@app.route("/guess/<name>")
def get_blog(name):
    response_age = requests.get(url=f"https://api.agify.io?name={name}")
    age = response_age.json()['age']
    response_gender = requests.get(url=f"https://api.genderize.io?name={name}")
    gender = response_gender.json()['gender']
    return render_template("jinjaApi.html",name = str(name).title(),gender=gender,age = age)



if __name__ == '__main__':
    app.run(debug=True)