from datetime import date
from rest_framework import Modelserializer
import re
from passlib.hash import pbkdf2_sha256

class EligibilitySerializer(serializers.Modelserializer):
    class Meta:
        model = 'RegistrationPerson'
        fields = '__all__'

    # def validate_date_of_birth(self, dob):
    #     today = date.today()
    #     age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    #     if (not(18 < age < 100)):
    #         raise serializers.ValidationError("You are not eligible for Vote")
    #     return age

    def validate(self, data):

        #aadhar
        aadhar = data['aadhar_no']
        regex = ("^[2-9]{1}[0-9]{3}\\" +
                 "s[0-9]{4}\\s[0-9]{4}$")
        p = re.compile(regex)
        if (aadhar == None):
            return False
        if (re.search(p, str)):
            return "Aadhar is Valid"
        else:
            return "Aadhar is invalid"

        #password
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, password)
        if mat:
            self.password = pbkdf2_sha256.hash(password)
            return self.password
        else:
            return "Password invalid !!"

            return data
