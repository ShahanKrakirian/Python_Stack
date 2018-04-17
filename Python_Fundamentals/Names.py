# Names

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

#Part I

# def names(my_dict):
#     for i in range(0, len(my_dict)):
#         first_name = my_dict[i]['first_name']
#         last_name = my_dict[i]['last_name']
#         print first_name, last_name


# names(students)

#Part II

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def nicer_names(my_dict):
     for keys,values in my_dict.iteritems():
         print keys
         for i in range(0, len(values)):
             print i+1, "-", values[i]['first_name'], values[i]['last_name'], '-', len(values[i]['first_name']) + len(values[i]['last_name'])


nicer_names(users)