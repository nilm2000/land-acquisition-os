# app/models/__init__.py
from app.database import Base  # re-export Base for create_all
from .user import User
# import the rest so metadata is complete:
# from .parcel import Parcel
# from .project import Project
# from .filter import Filter
# from .audit_log import AuditLog

