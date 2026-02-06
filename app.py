from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy


#Creating object
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///employee.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False

db=SQLAlchemy(app)
app.app_context().push()

# Create tables if they don't exist
with app.app_context():
    db.create_all()

class Employee(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(500),nullable=False)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name=request.form.get('name', '').strip()
        email=request.form.get('email', '').strip()
        
        # Server-side validation
        if name and email:
            employee=Employee(name=name,email=email)
            db.session.add(employee)
            db.session.commit()
    allemployee=Employee.query.all()
    return render_template("index.html",allemployee=allemployee)

@app.route("/about")
def about(): 
    return render_template("about.html")

@app.route("/delete/<int:sno>")
def delete(sno):
    employee=Employee.query.filter_by(sno=sno).first()
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    employee=Employee.query.filter_by(sno=sno).first()
    if request.method == 'POST':
        name=request.form.get('name', '').strip()
        email=request.form.get('email', '').strip()
        
        # Server-side validation
        if name and email:
            employee.name=name
            employee.email=email
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("update.html",employee=employee)

@app.route("/delete_multiple", methods=['POST'])
def delete_multiple():
    employee_ids = request.form.getlist('employee_ids')
    if employee_ids:
        for emp_id in employee_ids:
            employee = Employee.query.filter_by(sno=int(emp_id)).first()
            if employee:
                db.session.delete(employee)
        db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)