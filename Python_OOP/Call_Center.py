from operator import attrgetter

# Call Center 

class Call(object):

    #Constructor 
    def __init__(self, unique_id, name, number, time, reason):

        self.unique_id = unique_id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason

    #Display 
    def display(self):

        print "Caller ID:", self.unique_id
        print "Caller Name:", self.name
        print "Caller Number:", self.number
        print "Time of Call:", self.time
        print "Reason for Call:", self.reason

class CallCenter(object):

    #Constructor 
    def __init__(self):

        self.calls = []
        self.size = len(self.calls)

    #Add Call 
    def add_call(self, call):

        self.calls.append(call)
        return self 
    
    #Remove Call from Front 
    def remove_first_call(self):

        self.calls.pop(0)
        return self 

    #Ninja Level 
    def remove_number(self, number):
        storage = None
        for i in range(0, len(self.calls)):
            if number == self.calls[i].number:
                storage = i 
        del self.calls[storage]
            
        return self

    #Hacker Level
    def sort(self):

        self.calls.sort(key = attrgetter('number'))
        return self

    #Returns Info
    def info(self):

        print "Queue length:", len(self.calls)
        for element in self.calls:
            print element.name
            print element.number



call_center = CallCenter() #Create Call Center 

#Creating Calls 
call_1 = Call('123', 'Lowest', 1, 2, 'Why not')
call_2 = Call('1234', 'Low-Med', 2, 5, 'Because I said so')
call_3 = Call('1234', 'Highest', 8, 10, 'Because I said so')
call_4 = Call('1234', 'Med-High', 6, 10, 'Because I said so')

#Add calls to list and sort. 
call_center.add_call(call_1).add_call(call_2).add_call(call_3).sort().add_call(call_4).sort() #Works 
print call_center.info()
