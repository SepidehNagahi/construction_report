from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text, MetaData
from sqlalchemy.orm import relationship
from pymysql import *


from construction_report.model.tools.validator import Validator

from construction_report.model.entity.base import Base
from construction_report.model.entity.user import User
