import traceback
import uuid
import sys

def create_new_GUID(*kwargs):
    log = open(error_log, 'w')
    try:
        GUID = str((uuid.uuid4()))
        print(GUID)
        return GUID

    except Exception:
        traceback.print_exc(file=log)

error_log = sys.argv[1]

if __name__ == '__main__':
    create_new_GUID(error_log)
