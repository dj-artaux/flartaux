from flask import Flask, request, render_template, jsonify
from multi_select_form import MigrateUsersForm

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/migrate', methods = ["GET", "POST"])
def migrate_users():
    form = MigrateUsersForm()
    if request.method == "POST" and form.validate_on_submit():
        multiselect = ', '.join(form.multiselect.data)
        multiselect_to = ', '.join(form.multiselect_to.data)
        posted_data = {
            "multiselect": multiselect,
            "multiselect_to": multiselect_to
        }
        return jsonify(posted_data)
    return render_template('multi_select.html', form=form)