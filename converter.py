from flask import Flask, render_template, request

app = Flask(__name__) #flask app created

distance_units = {"millimeter": 0.001, "centimeter": 0.01, "meter": 1, "kilometer": 1000, "inch": 0.0254, "foot": 0.3048, "yard": 0.9144, "mile": 1609.344} #using metres as a base unit

weight_units = {"milligram": 0.001, "gram": 1, "kilogram": 1000, "ounce": 28.3495231, "pound": 453.59237}

def convert_length(old, new, num_value):
    meters = distance_units[old]*num_value
    converted_value = meters / distance_units[new]
    return converted_value

def convert_weight(old, new, num_value):
    grams = weight_units[old]*num_value
    converted_value = grams / weight_units[new]
    return converted_value


@app.route('/', methods=["GET", "POST"])
def length_converter():
    if request.method == "POST":
        old, new, num_value = request.form["oldunit"], request.form["newunit"], float(request.form["numvalue"]) #take requests from form
        
        converted_value = convert_length(old, new, num_value)
        return render_template("index.html", result=converted_value) #returns the page passing it the variable of the result of conversion

    return render_template('index.html') #render index page in templates folder

@app.route('/weight', methods=["GET", "POST"])
def weight():
    if request.method == "POST":
        old, new, num_value = request.form["oldunit"], request.form["newunit"], float(request.form["numvalue"]) #take requests from form
                
        converted_value = convert_weight(old, new, num_value)
        return render_template("weight.html", result=converted_value) #returns the page passing it the variable of the result of conversion

    return render_template('weight.html') #render index page in templates folder


if __name__ == '__main__':
    app.run(debug=True)