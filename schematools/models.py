from sqlalchemy import (
    ARRAY,
    Column,
    DateTime,
    ForeignKey,
    ForeignKeyConstraint,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

__all__ = ["Base", "Dataset", "Table", "Field"]

Base = declarative_base()


class Dataset(Base):
    __tablename__ = "meta_dataset"
    id = Column(String, primary_key=True)
    type = Column(String)
    title = Column(String)
    description = Column(String)
    date_created = Column(DateTime)
    auth = Column(String)
    date_modified = Column(DateTime)
    license = Column(String)
    homepage = Column(String)
    language = Column(String)
    status = Column(String)
    version = Column(String)
    objective = Column(String)
    temporal_unit = Column(String)
    spatial = Column(String)
    legal_basis = Column(String)
    contact_point = Column(String)  # struct with name/email
    accrual_periodicity = Column(String)
    spatial_description = Column(String)
    spatial_coordinates = Column(String)
    theme = Column(ARRAY(String))
    publisher = Column(String)
    owner = Column(String)
    authorization_grantor = Column(String)
    keywords = Column(ARRAY(String))
    has_beginning = Column(DateTime)
    has_end = Column(DateTime)
    crs = Column(String)


class Table(Base):
    __tablename__ = "meta_table"
    id = Column(String, primary_key=True)
    dataset_id = Column(String, ForeignKey("meta_dataset.id"), primary_key=True)
    type = Column(String)
    title = Column(String)
    description = Column(String)
    display = Column(String)
    required = Column(ARRAY(String))
    date_created = Column(DateTime)
    auth = Column(String)
    date_modified = Column(DateTime)
    license = Column(String)
    schema = Column(String)
    schema_version = Column(String)

    dataset = relationship("Dataset", backref="tables")


class Field(Base):
    __tablename__ = "meta_field"
    name = Column(String, primary_key=True)
    table_id = Column(String, primary_key=True)
    ref = Column(String)
    dataset_id = Column(String)
    type = Column(String)
    title = Column(String)
    description = Column(String)
    format = Column(String)
    uri = Column(String)
    relation = Column(String)
    auth = Column(String)
    unit = Column(String)
    enum = Column(ARRAY(String))

    table = relationship("Table", backref="fields")

    __table_args__ = (
        ForeignKeyConstraint(
            ["table_id", "dataset_id"], ["meta_table.id", "meta_table.dataset_id"]
        ),
    )
