from flask import Flask, render_template, flash, request

app = Flask(__name__)





@app.route("/")
def hello():           
 
    return render_template('disform.html')

@app.route("/result",methods=['GET','POST'])
def result():
     if request.method == 'POST':
        name=request.form['name']
        password=request.form['password']
        email=request.form['email']
        
        return render_template('disform1.html',name=name,password=password,email=email)
 
if __name__ == "__main__":
    app.run()
