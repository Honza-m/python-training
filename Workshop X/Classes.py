#definition
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def get_info(self):
        return "Brand: {}, color: {}".format(self.brand, self.color)

#GA_QUERY

#install tools before this
from tools import ga_query
q = ga_query.Get(ignore_no_permission_error=True)
print(len(q.bodies))

q.add_one_to_batch()
print(len(q.bodies))

q.add_one_to_batch()
print(len(q.bodies))

print(q.executed)
r = q.get_handled_data()
print(q.executed)

print(r)
print(q.results)
