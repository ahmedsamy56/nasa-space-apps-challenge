from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Space facts and exoplanet information
space_facts = [
    "The Sun is a star at the center of our Solar System.",

]

exoplanet_info = {
    "Kepler-22b": "Kepler-22b is an exoplanet discovered by NASA's Kepler space telescope. It's located about 600 light-years from Earth and orbits in the habitable zone of its star, where liquid water could exist on the surface. It's often referred to as a 'super-Earth' because it's larger than our planet but smaller than gas giants like Neptune.",
    "TRAPPIST-1e": "TRAPPIST-1e is one of seven Earth-sized planets orbiting the ultra-cool dwarf star TRAPPIST-1, about 39 light-years from Earth. It's considered one of the most promising candidates for potential habitability, as it's in the star's habitable zone and has a density suggestive of a rocky composition.",
}

def get_space_response(question):
    # Check if the question is about a specific exoplanet
    for planet, info in exoplanet_info.items():
        if planet.lower() in question.lower():
            return info
    
    # Check if the question is about a specific topic in space_facts
    for fact in space_facts:
        if any(word in question.lower() for word in fact.lower().split()[:3]):
            return fact
    
    # If no specific match, return a random fact
    return "I don't have specific information about that, but here's an interesting space fact: " + random.choice(space_facts)


@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    response = get_space_response(msg)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)