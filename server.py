from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    Customer_name = request.form['first_name']
    count = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    now = datetime.now()
    date = now.strftime("%b %d, %Y, %H:%M:%S")
    print(f"Charging {Customer_name} for {count}")
    return render_template("checkout.html", count=count, date=date)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)