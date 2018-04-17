from operator import attrgetter

#Hospital 

#Class Patient
class Patient(object):

    def __init__(self, identification, name, allergies):

        self.identification = identification
        self.name = name 
        self.allergies = allergies
        self.bed = None 

#Class Hospital 
class Hospital(object):

    #Constructor 
    def __init__(self, name, capacity):

        self.patients = []
        self.name = name
        self.capacity = capacity 

    #Admit Method 
    def admit(self, patient):
        
        if len(self.patients) >= self.capacity:
            return "Hospital is full."

        #If no patients are currently in the hospital, give them bed 1.
        if len(self.patients) == 0:
            patient.bed = 1
            self.patients.append(patient)
            return self

        #Create a list of beds already occupied. 
        bed_list = []
        for i in range(0, len(self.patients)):
            bed_list.append(self.patients[i].bed)
        bed_list.sort()
        print bed_list

        #If there are patients in the hospital, give them the lowest number bed available.
        for i in range(1, len(bed_list)+2):
            if i not in bed_list:
                patient.bed = i
                self.patients.append(patient)
                return self


    #Discharge Method 
    def discharge(self, remove_id):
        for i in range(0, len(self.patients)):
            if remove_id == self.patients[i].identification:
                self.patients[i].bed = None
                del self.patients[i]
                break
        return self


patient_1 = Patient('patient_1', 'dude', 'allergies')
patient_2 = Patient('patient_2', 'dude', 'allergies')
patient_3 = Patient('patient_3', 'dude', 'allergies')
patient_4 = Patient('patient_4', 'dude', 'allergies')
patient_5 = Patient('patient_5', 'dude', 'allergies')

test_hospital = Hospital('test_name', 30)

test_hospital.admit(patient_1).admit(patient_2).admit(patient_3).discharge('patient_2').admit(patient_4)
print patient_2.bed 
print patient_4.bed

