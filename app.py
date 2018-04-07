import mlab
from flask import *
from models.service import Service


app = Flask(__name__)
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
    all_services = Service.objects(gender=gender)
    return render_template('search.html', all_services =all_services )

@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template('admin.html',services = services)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is None:
        return 'Not Found'
    else:
        service_to_delete.delete()
        return redirect(url_for('/admin'))

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

        new_service = Service(name = name,yob = yob, gender = gender, height = height, phone = phone, address = address, status = status)
        new_service.save()

        return redirect(url_for('/admin'))

@app.route('/update_service/<service_id>', methods=['GET', 'POST'])
def update(service_id):
    service_to_update = Service.objects.with_id(service_id)
    if service_to_update is None:
        return "Not Found"
    if request.method == 'GET':
        return render_template("update_service.html", service=service_to_update)
    elif request.method == 'POST':
        service_to_modify.name = request.form['name']
        service_to_modify.yob = int(request.form['yob'])
        service_to_modify.address = request.form['address']
        service_to_modify.save()
        return redirect(url_for('admin'))

if __name__ == '__main__':
  app.run(debug=True)
