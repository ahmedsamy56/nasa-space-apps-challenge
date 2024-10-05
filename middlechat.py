from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Space facts
space_facts = [
    "Hi, how are you!"  ,

]

# Exoplanet information with 25 entries
exoplanet_info = {
    "Kepler-22b": {
        "description": "Kepler-22b is a planet about 600 light-years away. It’s in the 'Goldilocks zone,' where it’s not too hot or too cold for liquid water. It’s bigger than Earth but smaller than Neptune.",
        "type": "Super-Earth",
        "mass": "2.4 times Earth's mass",
        "radius": "2.4 times Earth's radius",
        "distance": "600 light-years",
        "discovery_year": 2011
    },
    "TRAPPIST-1e": {
        "description": "TRAPPIST-1e is one of seven Earth-sized planets orbiting a small, cool star 39 light-years away. It might have the right conditions for life.",
        "type": "Terrestrial",
        "mass": "0.69 times Earth's mass",
        "radius": "0.91 times Earth's radius",
        "distance": "39 light-years",
        "discovery_year": 2017
    },
    "HD 189733b": {
        "description": "HD 189733b is a gas giant located 63 light-years away. It is known for its deep blue color and extreme weather conditions, like glass rain.",
        "type": "Hot Jupiter",
        "mass": "1.13 times Jupiter's mass",
        "radius": "1.14 times Jupiter's radius",
        "distance": "63 light-years",
        "discovery_year": 2005
    },
    "Proxima Centauri b": {
        "description": "Proxima Centauri b is the closest known exoplanet, orbiting the star Proxima Centauri, only 4.24 light-years from Earth.",
        "type": "Terrestrial",
        "mass": "1.17 times Earth's mass",
        "radius": "Unknown",
        "distance": "4.24 light-years",
        "discovery_year": 2016
    },
    "WASP-12b": {
        "description": "WASP-12b is a hot Jupiter that is so close to its star that it is being stretched into an egg shape due to tidal forces.",
        "type": "Hot Jupiter",
        "mass": "1.41 times Jupiter's mass",
        "radius": "1.79 times Jupiter's radius",
        "distance": "1,400 light-years",
        "discovery_year": 2008
    },
    "GJ 1214b": {
        "description": "GJ 1214b is a water world located 48 light-years away. Its atmosphere is thick and cloudy, possibly composed of water vapor.",
        "type": "Mini-Neptune",
        "mass": "6.55 times Earth's mass",
        "radius": "2.68 times Earth's radius",
        "distance": "48 light-years",
        "discovery_year": 2009
    },
    "Kepler-10c": {
        "description": "Kepler-10c is a rocky planet much bigger than Earth, sometimes called a 'mega-Earth.'",
        "type": "Mega-Earth",
        "mass": "17 times Earth's mass",
        "radius": "2.35 times Earth's radius",
        "distance": "564 light-years",
        "discovery_year": 2011
    },
    "HD 209458b": {
        "description": "HD 209458b, nicknamed 'Osiris,' is the first exoplanet detected transiting its star and also one of the first to have its atmosphere studied.",
        "type": "Hot Jupiter",
        "mass": "0.69 times Jupiter's mass",
        "radius": "1.38 times Jupiter's radius",
        "distance": "159 light-years",
        "discovery_year": 1999
    },
    "55 Cancri e": {
        "description": "55 Cancri e is an ultra-short period super-Earth that orbits its star every 18 hours. It may have lava oceans on its surface.",
        "type": "Super-Earth",
        "mass": "7.99 times Earth's mass",
        "radius": "1.87 times Earth's radius",
        "distance": "41 light-years",
        "discovery_year": 2004
    },
    "LHS 1140b": {
        "description": "LHS 1140b is a rocky super-Earth in the habitable zone of its star, with conditions possibly suitable for life.",
        "type": "Super-Earth",
        "mass": "6.6 times Earth's mass",
        "radius": "1.43 times Earth's radius",
        "distance": "41 light-years",
        "discovery_year": 2017
    },
    "Kepler-452b": {
        "description": "Kepler-452b is often called Earth’s 'older cousin' because it orbits in the habitable zone of a star similar to our Sun.",
        "type": "Super-Earth",
        "mass": "5 times Earth's mass",
        "radius": "1.63 times Earth's radius",
        "distance": "1,400 light-years",
        "discovery_year": 2015
    },
    "K2-18b": {
        "description": "K2-18b is a super-Earth with water vapor detected in its atmosphere, making it a candidate for further habitability studies.",
        "type": "Super-Earth",
        "mass": "8.6 times Earth's mass",
        "radius": "2.6 times Earth's radius",
        "distance": "124 light-years",
        "discovery_year": 2015
    },
    "Gliese 667 Cc": {
        "description": "Gliese 667 Cc is located in the habitable zone of its star system and could potentially support life.",
        "type": "Super-Earth",
        "mass": "4.5 times Earth's mass",
        "radius": "Unknown",
        "distance": "23.6 light-years",
        "discovery_year": 2011
    },
    "Kepler-186f": {
        "description": "Kepler-186f is the first Earth-sized planet found in the habitable zone of another star, where liquid water could exist.",
        "type": "Terrestrial",
        "mass": "1.32 times Earth's mass",
        "radius": "1.1 times Earth's radius",
        "distance": "582 light-years",
        "discovery_year": 2014
    },
    "HD 40307g": {
        "description": "HD 40307g is a super-Earth located in the habitable zone, with the potential to host liquid water.",
        "type": "Super-Earth",
        "mass": "7.1 times Earth's mass",
        "radius": "Unknown",
        "distance": "42 light-years",
        "discovery_year": 2008
    },
    "Kepler-1649c": {
        "description": "Kepler-1649c is a potentially habitable planet only slightly larger than Earth, located in its star's habitable zone.",
        "type": "Terrestrial",
        "mass": "Unknown",
        "radius": "1.06 times Earth's radius",
        "distance": "300 light-years",
        "discovery_year": 2020
    },
    "Wolf 1061c": {
        "description": "Wolf 1061c is a rocky super-Earth located in the habitable zone of a red dwarf star, about 13.8 light-years from Earth.",
        "type": "Super-Earth",
        "mass": "4.3 times Earth's mass",
        "radius": "1.5 times Earth's radius",
        "distance": "13.8 light-years",
        "discovery_year": 2015
    },
    "Ross 128b": {
        "description": "Ross 128b is one of the closest Earth-like planets and orbits a quiet red dwarf star, making it a prime target for life searches.",
        "type": "Terrestrial",
        "mass": "1.35 times Earth's mass",
        "radius": "Unknown",
        "distance": "11 light-years",
        "discovery_year": 2017
    },
    "Kepler-62e": {
        "description": "Kepler-62e is a super-Earth located in the habitable zone of its star. It may be covered in oceans.",
        "type": "Super-Earth",
        "mass": "Unknown",
        "radius": "1.61 times Earth's radius",
        "distance": "1,200 light-years",
        "discovery_year": 2013
    },
    "Tau Ceti e": {
        "description": "Tau Ceti e is an Earth-like planet located just 11.9 light-years away, with a possible habitable environment.",
        "type": "Super-Earth",
        "mass": "4.3 times Earth's mass",
        "radius": "Unknown",
        "distance": "11.9 light-years",
        "discovery_year": 2012
    }
}


# Exoplanet statistics
exoplanet_statistics = {
    "total_discovered": 5000,
    "total_systems": 4000,
    "total_terrestrial": 1000,
    "total_gas_giants": 2000,
    "total_super_earths": 800,
}

def get_statistics_response():
    stats = (
        f"As of now, there have been over {exoplanet_statistics['total_discovered']} exoplanets discovered, "
        f"located in approximately {exoplanet_statistics['total_systems']} different star systems. "
        f"There are around {exoplanet_statistics['total_terrestrial']} terrestrial planets, "
        f"{exoplanet_statistics['total_gas_giants']} gas giants, and about {exoplanet_statistics['total_super_earths']} super-Earths!"
    )
    return stats

def get_space_response(msg):
    # Check for statistics question
    if "statistics" in msg.lower() or "how many" in msg.lower():
        return get_statistics_response()

    # Check if the question is about a specific exoplanet
    for planet, info in exoplanet_info.items():
        if planet.lower() in msg.lower():
            response = f"{planet}: {info['description']} It is a {info['type']}. "
            response += f"It has a mass of {info['mass']} and a radius of {info['radius']}. "
            response += f"It is {info['distance']} away and was discovered in {info['discovery_year']}."
            return response
    
    # Check for specific questions about exoplanets
    if "biggest" or "big" or "largest"in msg.lower():
        return "The biggest exoplanet known is Kepler-10c, which is about 2.35 times the size of Earth!"
    elif "smallest" in msg.lower():
        return "The smallest known exoplanet is Kepler-37b, which is about the size of the Moon!"
    elif "farthest" in msg.lower():
        return "The farthest known exoplanet is OGLE-2005-BLG-390Lb, located about 21,500 light-years away!"
    elif "nearest" in msg.lower():
        return "The nearest known exoplanet is Proxima Centauri b, which is only 4.24 light-years away from Earth!"
    elif "darkest" in msg.lower():
        return "WASP-12b is one of the darkest known exoplanets due to its light-absorbing atmosphere!"
    elif "lightest" in msg.lower():
        return "WASP-17b is one of the lightest exoplanets for its size!"


    for fact in space_facts:
        if any(word in msg.lower() for word in fact.lower().split()[:3]):
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