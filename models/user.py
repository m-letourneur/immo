import uuid
from app_backend import db


class User(db.Model):
    """
    User model

    A user is described by his first and last names, and his date of birth
    The three attributes are mandatory for instantiation

    String fields are all lowercased at creation 
    """
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True,
                   default=lambda: uuid.uuid4().hex)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)

    def __init__(self, first_name, last_name, birth_date):
        """
        Initialization of the attributes when one instance is created

        Parameters
        ----------
        first_name: str
            First name
        last_name: str
            Last name
        birth_date: str, (format 'yyyy-mm-dd')
            Date of birth

        Attributes
        ----------
        id: int
            UUID
        first_name: str
            First name
        last_name: str
            Last name
        birth_date: str, (format 'yyyy-mm-dd')
            Date of birth
        """
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()
        self.birth_date = birth_date

    def __repr__(self):
        """
        Representation of the object

        Returns
        -------
        _ : str
            User's uuid, first name, last name, date of birth
        """
        return ('<User: uuid = %s, First Name = %s, Last Name = %s, '
                + 'Birth date = %s>') % (self.id, self.first_name,
                                         self.last_name, self.birth_date)
