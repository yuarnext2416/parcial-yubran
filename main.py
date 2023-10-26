
from flask import Flask, render_template,request
from flask_mail import Mail,Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'yukiljho0624millos@outlook.com'
app.config['MAIL_PASSWORD'] = 'help111111'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route("/",methods=['GET', 'POST'])
def index():
  if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']  
        msg = Message(name, sender = 'yukiljho0624millos@outlook.com', recipients = [email])
        msg.html= f"<html> <body> <br> {message} <br>   <br> {email} </body> </html>"
        mail.send(msg)
        return "Mensaje enviado!"
  return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)