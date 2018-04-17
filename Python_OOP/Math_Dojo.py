# Math Dojo 

# Part I 

# class MathDojo(object):

#     def __init__(self):
#         self.value = 0 

#     def add(self, first, second = 0):
#         self.value += first + second 
#         return self 

#     def subtract(self, first, second = 0):
#         self.value -= (first + second)
#         return self 

#     def result(self):
#         return self.value

# md = MathDojo()
# print md.add(2).add(2,5).subtract(3,2).result() #Works 

# Part II 

# class MathDojo(object):

#     def __init__(self):
#         self.value = 0 


#     def add(self, *args):
#         for arg in args:
#             if isinstance(arg, list):
#                 for element in arg:
#                     self.value += element 
#             elif isinstance(arg, int) or isinstance(arg, float):
#                 self.value += arg 
#         return self


#     def subtract(self, *args):
#         temp_sum = 0
#         for arg in args: 
#             if isinstance(arg, list):
#                 for element in arg:
#                     temp_sum += element 
#             elif isinstance(arg, int) or isinstance(arg, float):
#                 temp_sum += arg 
#         self.value -= temp_sum
#         return self 


#     def result(self):
#         return self.value

# md = MathDojo()
# print md.add(2, [2,2]).add(2,5).subtract(3,[2,2,2]).result() #Works 

#Part III 

class MathDojo(object):

    def __init__(self):
        self.value = 0 


    def add(self, *args):
        for arg in args:
            if isinstance(arg, list) or isinstance(arg, tuple):
                for element in arg:
                    self.value += element 
            elif isinstance(arg, int) or isinstance(arg, float):
                self.value += arg 
        return self


    def subtract(self, *args):
        temp_sum = 0
        for arg in args: 
            if isinstance(arg, list) or isinstance(arg, tuple):
                for element in arg:
                    temp_sum += element 
            elif isinstance(arg, int) or isinstance(arg, float):
                temp_sum += arg 
        self.value -= temp_sum
        return self 

    def result(self):
        return self.value

md = MathDojo()
print md.add(2, [2,2]).add(2,5).subtract(3,(2,2,2)).result() #Works 