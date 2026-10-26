from flask import Flask, render_template, request

app = Flask(__name__) #flask app created

@app.route('/', methods=["GET", "POST"])
def length_converter():
    if request.method == "POST":
        old, new, num_value = request.form["oldunit"], request.form["newunit"], float(request.form["numvalue"]) #take requests from form
        
        converted_value = convert(old, new, num_value)
        return render_template("index.html", result=converted_value) #returns the page passing it the variable of the result of conversion

    return render_template('index.html') #render index page in templates folder

units = {"millimeter": 0.001, "centimeter": 0.01} #using metres as a base unit

def convert(old, new, num_value):
    meters = units[old]*num_value
    print(meters)
    converted_value = meters / units[new]
    print(converted_value)
    return converted_value

if __name__ == '__main__':
    app.run(debug=True)