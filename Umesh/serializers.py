from datetime import date
from rest_framework import serializers
import re
from passlib.hash import pbkdf2_sha256

class EligibilitySerializer(serializers.Serializer):

    date_of_birth = serializers.DateField()
    Aadharcard = serializers.CharField()
    password = serializers.CharField()
    def validate_date_of_birth(self, dob):
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if (not(18 < age < 100)):
            raise serializers.ValidationError("You are not eligible for Vote")

        return age

    def isValidAadharNumber(str):
        # Regex to check valid
        # Aadhar number.
        regex = ("^[2-9]{1}[0-9]{3}\\" +
                 "s[0-9]{4}\\s[0-9]{4}$")

        # Compile the ReGex
        p = re.compile(regex)

        # If the string is empty
        # return false
        if (str == None):
            return False

        # Return if the string
        # matched the ReGex
        if (re.search(p, str)):
            return "Aadhar is Valid"
        else:
            return "Aadhar is invalid"


    def validatePassword(self,password):
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"

        # compiling regex
        pat = re.compile(reg)

        # searching regex
        mat = re.search(pat, password)

        # validating conditions
        if mat:
            self.password = pbkdf2_sha256.hash(password)
            return self.password
        else:
            return "Password invalid !!"


