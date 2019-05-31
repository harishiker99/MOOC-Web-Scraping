from flask import Flask, flash, redirect, url_for
from flask import render_template, request
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField, SubmitField,IntegerField,SelectField
# from wtforms.validators import DataRequired
import sqlite3

app = Flask(__name__)
app.secret_key = 'development key'
conn = sqlite3.connect('scrap.db')
curs = conn.cursor()

'''
class LoginForm(FlaskForm):
    username = StringField('Student Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rollnumber = IntegerField('Student Roll Number', validators=[DataRequired()])
    divison = SelectField('Student Divison', choices = [('B', 'B'),
      ('A', 'A')],validators=[DataRequired()])
    submit = SubmitField('Add')
'''


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if form.validate_on_submit():  # POST request with valid input?
            username = form.username.data
            password = form.password.data
            rollnumber = form.rollnumber.data
            divison = form.divison.data

            sql = "insert into student (username,password,rollnumber,divison) values ('%s','%s','%s','%s');" % (
            username, password, rollnumber, divison)
            curs.execute(sql)
            conn.commit()

            return redirect(url_for('home'))
        else:
            flash('Ivalid data')

    sql = "select * from student "
    curs.execute(sql)
    results = curs.fetchall()
    print(results)
    return render_template('mysqlcrudComplete.html', form=form, studentsData=results)


@app.route('/update', methods=['GET', 'POST'])
def update(roll=None):
    updateform = LoginForm()

    if request.method == 'POST':
        if updateform.validate_on_submit():  # POST request with valid input?
            username = updateform.username.data
            password = updateform.password.data
            rollnumber = updateform.rollnumber.data
            divison = updateform.divison.data
            sql = "update student set username = '%s',password = '%s',divison = '%s' where rollnumber='%s'" % (
            username, password, divison, rollnumber)
            print(sql)
            curs.execute(sql)
            conn.commit()

            return redirect(url_for('home'))
        else:
            flash('Ivalid data')
            return redirect(url_for('updateRoll', roll=updateform.rollnumber.data))

    return redirect(url_for('home'))


@app.route('/update/<roll>')
def updateRoll(roll=None):
    updateform = LoginForm()
    sql = "select * from student where rollnumber = '%s';" % (roll)
    curs.execute(sql)
    student = curs.fetchall()
    print(student)
    sql = "select * from student;"
    curs.execute(sql)
    results = curs.fetchall()
    print(results)
    return render_template('mysqlcrudComplete.html', updateform=updateform, studentsData=results,
                           studentToUpdate=student)


@app.route('/delete/<roll>')
def delete(roll=None):
    if (roll != None):
        sql = "delete from student where rollnumber = '%s'" % (roll)
        curs.execute(sql)
        conn.commit()
        return redirect(url_for('home'))
    return redirect(url_for('home'))
