from models.customer import Customer
import mlab

mlab.connect()

# all_services = Service.objects()
#
# print(all_services[10].name)

id_to_find ='5ac4e37a0e961727086293bd'

# khachhang = Customer.objects(id=id_to_find)[0]

# khachhang = Customer.objects.get(id=id_to_find)

khachhang = Customer.objects.with_id(id_to_find)

if khachhang is None:
    print('Customer not found')
else:
    # print(khachhang.to_mongo()
    # khachhang.delete()
    khachhang.update(set__name='Abigaile Johnson')
    khachhang.reload()
    print(khachhang.name)
