from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
with app.app_context():
    db.create_all()

# Model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

# Model for InsuranceClaim
class InsuranceClaim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    claim_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='Pending')

# Routes
@app.route('/')
def admin_homepage():
    return render_template('admin_homepage.html')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = User.query.filter_by(username=username, password=password).first()
        if admin:
            return redirect(url_for('view_registered_members'))
    return render_template('admin_login.html')

@app.route('/admin/view-members')
def view_registered_members():
    members = User.query.all()
    return render_template('view_members.html', members=members)

@app.route('/admin/approve-claims')
def approve_claims():
    claims = InsuranceClaim.query.all()
    return render_template('approve_claims.html', claims=claims)

@app.route('/admin/award-compensation/<int:claim_id>')
def award_compensation(claim_id):
    claim = InsuranceClaim.query.get(claim_id)
    if claim and claim.status == 'Pending':
        claim.status = 'Approved'
        db.session.commit()
        return f'Compensation awarded for user with claim ID {claim_id}.'
    return 'Claim not found or already approved.'

@app.route('/admin/logout')
def admin_logout():
    return redirect(url_for('admin_homepage'))

if __name__ == '__main__':
    app.run(debug=True)
