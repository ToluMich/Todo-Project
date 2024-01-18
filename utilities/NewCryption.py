from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings

key = b'qUFYBumQ6yBQnDCxxHtoIkffqRmxa1oJdQ-DW8d1gxc='

def encrypt(pas: any) -> str:
    try:        
        pas = str(pas)
        # ekey = base64.b64encode(settings.ENCRYPT_KEY)
        # ekey = settings.ENCRYPT_KEY.encode("ascii")
        cipher_pass = Fernet(key)
        encrypt_pass = cipher_pass.encrypt(pas.encode('ascii'))
        encrypt_pass = base64.urlsafe_b64encode(encrypt_pass).decode("ascii") 
        return encrypt_pass
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None



def decrypt(pas: str) -> any:
    try:
        pas = base64.urlsafe_b64decode(pas)
        cipher_pass = Fernet(key)
        decod_pass = cipher_pass.decrypt(pas).decode("ascii")     
        return decod_pass
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


# print(Fernet.generate_key())

# encResult = encrypt("""Tolu na Man mehn. That gyu conquers a lot of Huge Battles Silently and you  cant Suspect him.
#         It can only be God that has been fighting his battles for him. God is Good!!!""")
# print(encResult)
# print("Enc Result DataType: ", type(encResult))

# decResult = decrypt("""Z0FBQUFBQmxxTWktQ3I3QUZIaF9yZjFDemJhYjVSMlM3YlZXeFRUQnZxVUxWbWRKcGNFbUwwX0tPNlR0Wkh4ZmNTRC1GTFhjN21VYWMyck5sY1JHdm42OFc0QkJlb0I3S0FkdmxYbUxlMnBIQThVN1NaWGxTc2tKdE9UQ1EzMFRSeF85TnJWTFA5NERQc1poN3JOWExpa0wwaWw2Sy1mTEg0Qms3V1JScGtaUU8xRWlvZmxGaUIxMm5QVXVESF9EeWVpREw3QmpobmhHUjJQUExBS3dRemdZdkpqdWtDMUFnNzBDOW40R1FIOTczRm00aVdFREk2ZHJSMEdkbEdSM1p2eldZQXBfTmFOUXpCSUUwdkhQVUhGd3JjYW9GdUI4RnhKRkVaaUZGUG1LNUpmYXA0NVFmelQwclJhMnlaM3kzai1MYjdGclJLOVY=""")
# print(decResult)
# print("Dec Result DataType: ", type(decResult))


