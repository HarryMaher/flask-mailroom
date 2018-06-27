import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donor, Donation 

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/create_donations/', methods=['GET', 'POST'])
def create():
	if request.method == "GET":
		return render_template('create_donations.jinja2')
	elif request.method == "POST":
		donor_name = request.form['donor_name']
		donation_amt = request.form['donation']

		curr_donor = Donor(name=donor_name)
		curr_donor.save()
		Donation(donor=curr_donor, value=int(donation_amt)).save()

		## somehow post to stuff
		## do something to try posting donor name
		## elif donor name is not unique, then return text informing user.
		donations = Donation.select()
		return render_template('donations.jinja2', donations = donations)

@app.route('/save', methods = ['POST'])
def save():
	total = session.get('total', 0)
	saved_total = SavedTotal(value= total, code = code)
	saved_total.save()

	return render_template('save.jinja2', code=code)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port, debug=True)

