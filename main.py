
import hashlib

textual_password = "securepassword123"  
graphical_password = "1234" 
fingerprint_data = "fingerprint123"  
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def level_1_authentication(input_password):
    return hash_password(input_password) == hash_password(textual_password)


def level_2_authentication(input_sequence):
    return input_sequence == graphical_password


def level_3_authentication(input_fingerprint):
    return input_fingerprint == fingerprint_data


def authenticate_user():
    print("Level 1: Enter your textual password:")
    input_password = input("Password: ")
    if not level_1_authentication(input_password):
        print("Level 1 Authentication Failed")
        return False

    print("Level 1 Authentication Successful")

    print("Level 2: Enter your graphical password sequence (e.g., 1234):")
    input_sequence = input("Graphical Password: ")
    if not level_2_authentication(input_sequence):
        print("Level 2 Authentication Failed")
        return False

    print("Level 2 Authentication Successful")

    print("Level 3: Enter your fingerprint data (simulated input):")
    input_fingerprint = input("Fingerprint Data: ")
    if not level_3_authentication(input_fingerprint):
        print("Level 3 Authentication Failed")
        return False

    print("Level 3 Authentication Successful")
    return True


if authenticate_user():
    print("Access Granted")
else:
    print("Access Denied")
