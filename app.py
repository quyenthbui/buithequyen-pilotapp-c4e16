import mlab
from flask import *
from models.service import Service
from models.user import User
from models.order import Order
import datetime

app = Flask(__name__)
app.secret_key = 'admin'

mlab.connect()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
    all_services = Service.objects(gender=gender)
    return render_template('search.html', all_services =all_services )

@app.route('/signin', methods = ['GET','POST'])
def signin():
    if request.method == 'GET':
        return render_template('signin.html')
    elif request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        email = form['email']
        fullname = form['fullname']
        new_user = User(username = username, password = password, email = email, fullname = fullname)

        new_user.save()
        return 'You have been registered for our website'

@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template('admin.html',services = services)

@app.route('/servicepage')
def servicepage():
    all_services = Service.objects()
    return render_template('servicepage.html',all_services = all_services)

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']

        user = User.objects.get(username = username, password = password)
        if user is None:
            return 'Failed'
        else:
            session['user_id'] = str(user.id)
            return redirect(url_for('servicepage'))

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is None:
        return 'Not Found'
    else:
        service_to_delete.delete()
        return redirect(url_for('admin'))

@app.route('/new-service', methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('new-service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        gender = form['gender']
        height = form['height']
        phone = form['phone']
        address = form['address']
        status = form['status']
        description = form['description']
        measurement = form['measurement']
        new_service = Service(name = name,yob = yob, gender = gender, height = height, phone = phone,
                            address = address, status = status, description = description, measurement = measurement)
        new_service.save()

        return redirect(url_for('admin'))

@app.route('/detail/<service_id>')
def detail(service_id):
    if 'user_id' in session:
        service_to_detail = Service.objects.with_id(service_id)
        if service_to_detail is None:
            return "not found"
        else:
            return render_template('detail.html', service=service_to_detail)
    else:
        return redirect(url_for('login'))


@app.route('/update/<service_id>', methods=['GET', 'POST'])
def update(service_id):
    service_to_update = Service.objects.with_id(service_id)
    if service_to_update is None:
        return "Not Found"
    if request.method == 'GET':
        return render_template("update.html", service=service_to_update)
    elif request.method == 'POST':
        service_to_update.name = request.form['name']
        service_to_update.gender = request.form['gender']
        service_to_update.yob = int(request.form['yob'])
        service_to_update.phone = request.form['phone']
        service_to_update.height = request.form['height']
        service_to_update.address = request.form['address']
        service_to_update.status = request.form['status']
        service_to_update.description = request.form['description']
        service_to_update.measurement = request.form['measurement']
        service_to_update.save()
        return redirect(url_for('admin'))

@app.route('/order<serviceid>')
def order(serviceid):
    order = Order(user_id=session['user_id'], service_id=serviceid, time=datetime.datetime.now(), is_accepted=False)
    order.save()
    return 'request sent'

if __name__ == '__main__':
  app.run(debug=True)
