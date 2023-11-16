from sqlalchemy import Column
from sqlalchemy import String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Auth_User(Base):
    __tablename__ = "auth_user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(150))
    password = Column(String(128))
    
    # Define la relación con la clase Aceite
    aceite = relationship("Aceite", back_populates="usuario")

    def __repr__(self):
        return f'Auth_User({self.username}, {self.password})'

    def __str__(self):
        return self.username

class Aceite(Base):
    __tablename__ = "aceite"
    id = Column(Integer, primary_key=True, autoincrement=True)
    cantidad = Column(Integer)
    
    # Define la relación inversa con la clase Auth_User
    usuario_id = Column(Integer, ForeignKey("auth_user.id"))
    usuario = relationship("Auth_User", back_populates="aceite")

    def __repr__(self):
        return f'Aceite({self.id}, {self.cantidad})'

    def __str__(self):
        return f'Aceite ID: {self.id}, Cantidad: {self.cantidad}'
