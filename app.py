from email import message
from flask import Flask, flash, redirect, render_template,url_for,request
import flask
from sqlalchemy import false
app = Flask(__name__)
from forms import contactForm
from flask_mail import Message,Mail

mail= Mail()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact',methods=["GET","POST"])
def contact():
    form=contactForm()
    if request.method =="POST":
        if form.validate()==false:
            flash('All fields are required')
            return render_template('contact.html', form=form)

        else:
            msg = Message(form.subject.data, sender='satyajeetkadu42@gmail.com', recipients=['satyajeetkadu74@gmail.com'])
            msg.body = """
                        From    : %s <%s>
                            %s
                        """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            flash('Message sent, I will contact  you soon','success')
            return redirect(url_for('contact'))
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

    else:
        return render_template('contact.html', form=form)

@app.route('/weightlifting')
def weightlifting():
    return render_template('weightlifting.html')

@app.route('/football')
def football():
    return render_template('football.html')
    
@app.route('/reading')
def reading():
    return render_template('reading.html')

@app.route('/technology')
def technology():
    return render_template('technology.html')



app.secret_key = "Spkballer27"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'addyouremail@gmail.com'
app.config["MAIL_PASSWORD"] = 'yourpassword.com'
 
mail.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
