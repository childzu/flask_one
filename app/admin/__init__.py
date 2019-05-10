from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import employee_views
from . import department_views
from . import role_views
