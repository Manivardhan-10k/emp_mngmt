import os
import sys
import django
import jwt

# 👇 Add this line to include the project directory in sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 👇 Set the correct settings module (no emp_management prefix!)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emp_management_project.settings')

django.setup()

from django.conf import settings
from datetime import datetime, timedelta

def generate_jwt(payload):
    payload["exp"] = datetime.utcnow() + timedelta(hours=1)
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return token

def decode_jwt(token):
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


print(generate_jwt({"name":"mani"}))