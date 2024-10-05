from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Response
import requests
from planet_plot import create_planet_plot
from middlechat import get_space_response 


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/mainelementry')
def mainelementry():
    return render_template('mainelementry.html')

@app.route('/mainmiddle')
def mainmiddle():
    return render_template('mainmiddle.html')

@app.route('/mainhigh')
def mainhigh():
    return render_template('mainhigh.html')


@app.route('/exostory')
def exostory():
    return render_template('exostory.html')


@app.route('/kidgame')
def kidgame():
    return render_template('kidgame.html')


@app.route('/kidvid')
def kidvid():
    return render_template('kidvid.html')

@app.route('/kidsim')
def kidsim():
    return render_template('kidsim.html')


@app.route('/kidchat')
def kidchat():
    return render_template('kidchat.html')



@app.route('/3Dkids')
def d3Dkid():
    return render_template('3Dkids.html')

@app.route('/3Dmid')
def d3Dmid():
    return render_template('3Dmid.html')

@app.route('/systems')
def systems():
    return render_template('systems.html')

@app.route('/habitability')
def habitability():
    return render_template('habitability.html')

@app.route('/lessons')
def lesson():
    return render_template('lessons.html')

@app.route('/lessonsmid')
def lessonmid():
    return render_template('lessonsmid.html')

@app.route('/lesson-1')
def lesson1():
    return render_template('lesson-1.html')
@app.route('/lesson-2')
def lesson2():
    return render_template('lesson-2.html')
@app.route('/lesson-3')
def lesson3():
    return render_template('lesson-3.html')
@app.route('/lesson-4')
def lesson4():
    return render_template('lesson-4.html')
@app.route('/lesson-5')
def lesson5():
    return render_template('lesson-5.html')
@app.route('/lessonm')
def lessonm():
    return render_template('lessonm.html')

@app.route('/lessonm1')
def lessonm1():
    return render_template('lessonm1.html')
@app.route('/lessonm2')
def lessonm2():
    return render_template('lessonm2.html')
@app.route('/lessonm3')
def lessonm3():
    return render_template('lessonm3.html')
@app.route('/lessons')
def lessonm4():
    return render_template('lessonm4.html')
@app.route('/lessonm5')
def lessonm5():
    return render_template('lessonm5.html')


@app.route('/55 Cancri System')
def Cancri():
    return render_template('55 Cancri System.html')

@app.route('/Centauri')
def Centauri():
    return render_template('Centauri.html')

@app.route('/HD 209458 b (Osiris)')
def Osiris():
    return render_template('HD 209458 b (Osiris).html')

@app.route('/Kepler-20')
def Kepler():
    return render_template('Kepler-20.html')

@app.route('/Kepler-62')
def Keplers():
    return render_template('Kepler-62.html')

@app.route('/Kepler-186')
def Keplerss():
    return render_template('Kepler-186.html')

@app.route('/TRAPPIST-1 System')
def TRAPPISTSystem():
    return render_template('TRAPPIST-1 System.html')

@app.route('/WASP-12 System')
def WASPSystem():
    return render_template('WASP-12 System.html')

@app.route('/LHS1140')
def LHS():
    return render_template('LHS1140.html')

@app.route('/LKCa 15')
def LKCa():
    return render_template('LKCa 15.html')

@app.route('/51 Pegasi b')
def Pegas ():
    return render_template('51 Pegasi b.html')

@app.route('/GJ 1214b')
def GJ ():
    return render_template('GJ 1214b.html')



@app.route('/visualize')
def visualize():
    return render_template('visualize.html')


@app.route('/dash')
def dash():
    return render_template('dash.html')

@app.route('/compare')
def compare():
    return render_template('compare.html')

@app.route('/chart')
def chart():
    return render_template('kchart.html')



@app.route('/exoplanet_page')
def exoplanet_page():
    return render_template('exoplanet_page.html')

# Route for the exoplanet details page
@app.route('/exoplanet-details')
def exoplanet_details():
    exoplanet_id = request.args.get('id')
    return render_template('exoplanet-details.html', exoplanet_id=exoplanet_id)


@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/puzzle')
def puzzle():
    return render_template('puzzle.html')

@app.route('/build')
def build():
    return render_template('build.html')

@app.route('/color')
def color():
    return render_template('color.html')

@app.route('/detict')
def detict():
    return render_template('detict.html')

@app.route('/sim')
def sim():
    return render_template('sim.html')

@app.route('/distance')
def distance():
    return render_template('distance.html')

@app.route('/cards')
def cards():
    return render_template('matchcards.html')

@app.route('/find life')
def find_life():
    return render_template('find life.html')

@app.route('/Cosmic Voyage')
def Cosmic():
    return render_template('Cosmic Voyage.html')


@app.route('/protect the earth')
def protect():
    return render_template('protect the earth.html')





@app.route('/quize')
def quize():
    return render_template('quize.html')

@app.route('/Guess')
def guess():
    return render_template('guess.html')

@app.route('/facts')
def facts():
    return render_template('Match facts.html')


@app.route('/Quizee')
def Quizee():
    return render_template('Quizee.html')


@app.route('/vr')
def vr():
    return render_template('vr.html')




@app.route('/nasasearch')
def index():
    return render_template('nasa.html')

@app.route('/search')
def search():
    query = request.args.get('q')
    if not query:
        return jsonify([])

    nasa_api_url = f"https://images-api.nasa.gov/search?q={query}&media_type=image"
    response = requests.get(nasa_api_url)
    data = response.json()
    return jsonify(data['collection']['items'])

@app.route('/detail/<nasa_id>')
def detail(nasa_id):
    nasa_api_url = f"https://images-api.nasa.gov/search?nasa_id={nasa_id}"
    response = requests.get(nasa_api_url)
    data = response.json()
    if data['collection']['items']:
        item = data['collection']['items'][0]
        return render_template('detail.html', item=item)
    return "Image not found", 404



@app.route('/exobot')
def exobot():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    response = get_space_response(msg)
    return jsonify({"response": response})



@app.route('/view_planet_plot')
def view_planet_plot():
    graphJSON = create_planet_plot()
    return render_template('planet_plot.html', graphJSON=graphJSON)





if __name__ == '__main__':
    app.run(debug=True)