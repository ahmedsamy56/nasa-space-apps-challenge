from flask import Flask, render_template
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)

def create_planet_plot():
    # Define the coordinates, sizes, and colors of the celestial bodies
    bodies = {
        "Sun": (0, 0, 0, 20, 'yellow'),
        "Earth": (100, 0, 0, 7, 'blue'),
        "Proxima Centauri b": (4300, 0, 0, 6, 'green'),
        "Barnard's Star b": (5800, 0, 100, 5, 'purple'),
        "Lalande 21185 b": (8200, 0, -100, 6, 'pink'),
        "Luyten b": (12000, 100, 0, 5, 'cyan'),
        "Teegarden's Star b": (12300, 0, -200, 6, 'magenta'),
        "Wolf 1061c": (14200, -100, 100, 7, 'darkred'),
        "Kapteyn b": (13000, 200, 200, 5, 'lime'),
        "Ross 128 b": (10800, -200, -100, 6, 'teal'),
        "Gliese 667 Cc": (23000, -300, 100, 7, 'blueviolet'),
        "YZ Ceti b": (12200, 300, -200, 5, 'lightgreen'),
        "Gliese 411 b": (8700, 0, 300, 5, 'lightcoral'),
        "GJ 1061 d": (11800, 200, 300, 6, 'slategray'),
        "Gliese 832 c": (16000, -200, 200, 7, 'khaki'),
        "HD 219134 b": (21000, 300, -300, 5, 'plum'),
        "Groombridge 34 A b": (11700, -400, 0, 6, 'yellowgreen'),
        "Wolf 1069 b": (9100, 400, 100, 5, 'chocolate'),
        "Gliese 876 d": (15000, -500, 200, 7, 'goldenrod'),
        "Gliese 581 g": (20000, 500, -100, 7, 'lavender'),
        "Tau Ceti e": (11800, -600, 300, 6, 'navy'),
        "LHS 1140 b": (12400, 600, -200, 6, 'olive'),
        "Gliese 273 b": (12000, -700, 100, 5, 'palegreen'),
        "HD 85512 b": (23000, 700, 0, 6, 'indigo'),
        "Gliese 436 b": (17000, -800, -300, 5, 'peachpuff'),
        "Gliese 667 Cf": (24000, 800, 200, 6, 'coral'),
        "TRAPPIST-1e": (39000, 0, 400, 5, 'orchid')
    }

    # Create the 3D scatter plot with Plotly
    data = []
    for body, (x, y, z, size, color) in bodies.items():
        trace = go.Scatter3d(
            x=[x], y=[y], z=[z],
            mode='markers',
            marker=dict(
                size=size,
                color=color
            ),
            name=body
        )
        data.append(trace)

    layout = go.Layout(
        title="3D Plot of Planets and Exoplanets",
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z",
        ),
        margin=dict(l=0, r=0, b=0, t=40)
    )

    fig = go.Figure(data=data, layout=layout)

    # Render the plot as a JSON representation
    return pio.to_json(fig)

@app.route('/')
def home():
    graphJSON = create_planet_plot()
    return render_template('planet_plot.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True)