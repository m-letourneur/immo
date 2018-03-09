import uuid
import db


class Estate(db.Model):
    """
    Estate model
    """
    __tablename__ = 'estates'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True,
                   default=lambda: uuid.uuid4().hex)
    creator_uuid = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(255), nullable=False)
    nb_rooms = db.Column(db.Integer, nullable=False)
    rooms_description = db.Column(db.String(255), nullable=True)
    owner = db.Column(db.String(255), nullable=True)

    def __init__(self, creator_uuid, description='', city, nb_rooms=0, rooms_description=None, owner=None):
        """
        Initialization of the attributes when one instance is created

        Parameters
        ----------
        creator_uuid: int
            UUID of the user creating the estate entry
        description: str (optional, default None)
            Description of the estate
        city: str
            City location
        nb_rooms: int
                Number of rooms
        rooms_description: str
                Description of the rooms
        owner: str
                Owner of the estate

        Attributes
        ----------
        id: int
                UUID
        creator_uuid: int
            UUID of the user creating the estate entry
        description: str (optional, default None)
            Description of the estate
        city: str
            City location
        nb_rooms: int
                Number of rooms
        rooms_description: str
                Description of the rooms
        owner: str
                Owner of the estate

        """
        self.creator_uuid = creator_uuid
        self.description = description
        self.city = city
        self.nb_rooms = nb_rooms
        self.rooms_description = rooms_description
        self.owner = owner

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
                + '= %s>') % (self.id, self.creator_uuid, self.description,
                              self.city, self.nb_rooms, self.rooms_description,
                              self.owner)
