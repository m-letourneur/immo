import uuid
from app_backend import db


class Estate(db.Model):
    """
    Estate model

    An estate is described by its mandatory fields - creator, the city location, 
    the number of rooms - and non mandatory fields - description, description
    of rooms, owner

    String fields are all lowercased at creation
    """
    __tablename__ = 'estates'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True,
                   default=lambda: uuid.uuid4().hex)
    creator_uuid = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(255), nullable=False)
    nb_rooms = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    rooms_description = db.Column(db.String(255), nullable=True)
    owner = db.Column(db.String(255), nullable=True)

    def __init__(self, creator_uuid, city, nb_rooms, description=None,
                 rooms_description=None, owner=None):
        """
        Initialization of the attributes when one instance is created

        Parameters
        ----------
        creator_uuid: int
            UUID of the user creating the estate entry
        city: str
            City location
        nb_rooms: int
            Number of rooms
        description: str (optional, default None)
            Description of the estate
        rooms_description: str (optional, default None)
            Description of the rooms
        owner: str (optional, default None)
            Owner of the estate

        Attributes
        ----------
        id: int
            UUID
        creator_uuid: int
            UUID of the user creating the estate entry
        city: str
            City location
        nb_rooms: int
            Number of rooms
        description: str (optional, default None)
            Description of the estate
        rooms_description: str (optional, default None)
            Description of the rooms
        owner: str (optional, default None)
            Owner of the estate

        """
        self.creator_uuid = creator_uuid
        self.city = city.lower()
        self.nb_rooms = nb_rooms
        self.description = description.lower()
        self.rooms_description = rooms_description.lower()
        self.owner = owner.lower()

    def __repr__(self):
        """
        Representation of the object

        Returns
        -------
        _ : str
            Estate's uuid, creator's uuid, description, city, number of rooms, 
            rooms' description, owner
        """
        return ('<Estate uuid = %s, creator_uuid = %s, description = %s, '
                + 'city = %s, nb_rooms = %s, rooms_description = %s, owner '
                + '= %s>') % (self.id, self.creator_uuid, self.city,
                              self.description, self.nb_rooms,
                              self.rooms_description, self.owner)
