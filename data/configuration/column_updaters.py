"""
/***************************************************************************
Name                 : column_updater
Description          : Functions for updating columns in the database based
                        on type.
Date                 : 27/December/2015
copyright            : (C) 2015 by UN-Habitat and implementing partners.
                       See the accompanying file CONTRIBUTORS.txt in the root
email                : stdm@unhabitat.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import logging

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Integer,
    Numeric,
    String,
    Table,
    Text
)
from sqlalchemy.exc import ProgrammingError

from migrate.changeset import *

from geoalchemy2 import Geometry

from stdm.data.configuration.db_items import DbItem

LOGGER = logging.getLogger('stdm')


def _base_col_attrs(col):
    """
    Extracts the base attributes of a column.
    :param col: Base column
    :type col: BaseColumn
    :returns: Dictionary of name-values for an SQLAlchemy column.
    :rtype: dict
    """
    col_attrs = {}
    #col_attrs['index'] = col.index
    col_attrs['nullable'] = not col.mandatory
    #col_attrs['unique'] = col.unique

    return col_attrs


def _update_col(column, table, data_type, columns):
    """
    Update the column based on the database operation.
    :param column: Base column.
    :type column: BaseColumn
    :returns: SQLAlchemy column object.
    :rtype: Column
    :param columns: Existing column names in the database for the given table.
    :type columns: list
    """
    alchemy_column = Column(column.name, data_type, **_base_col_attrs(column))

    idx_name = None
    if column.index:
        idx_name = u'idx_{0}_{1}'.format(column.entity.name, column.name)

    unique_name = None
    if column.unique:
        unique_name = u'unq_{0}_{1}'.format(column.entity.name, column.name)

    if column.action == DbItem.CREATE:
        #Ensure the column does not exist otherwise an exception will be thrown
        if not column.name in columns:
            alchemy_column.create(
                table=table,
                index_name=idx_name,
                unique_name=unique_name
            )

    elif column.action == DbItem.ALTER:
        #Ensure the column exists before altering
        if column.name in columns:
            col_attrs = _base_col_attrs(column)
            col_attrs['table'] = table
            alchemy_column.alter(**col_attrs)

    elif column.action == DbItem.DROP:
        #Ensure the column exists before dropping
        if column.name in columns:
            _clear_ref_in_entity_relations(column)
            alchemy_column.drop(table=table)

    #Ensure column is added to the table
    if alchemy_column.table is None:
        alchemy_column._set_parent(table)

    return alchemy_column


def _clear_ref_in_entity_relations(column):
    #Check if the column is referenced by entity relation objects and delete.
    child_relations = column.child_entity_relations()
    parent_relations = column.parent_entity_relations()

    referenced_relations = child_relations + parent_relations

    #Flag profile to remove entity relations that reference the given column
    for er in referenced_relations:
        column.profile.remove_relation(er.name)

def base_column_updater(base_column, table, columns):
    """
    Generic function to be implemented by a BaseColumn object for updating
    the table column in the database using SQLAlchemy.
    This is a default implementation which does nothing.
    :param base_column: BaseColumn or its subclass object.
    :type base_column: BaseColumn
    :param table: SQLAlchemy table object
    :type table: Table
    :param columns: Existing column names in the database for the given table.
    :type columns: list
    """
    pass


def serial_updater(column, table, columns):
    """
    Updater for a serial column.
    :param serial_column: Serial column.
    :type serial_column: SerialColumn
    :param columns: Existing column names in the database for the given table.
    :type columns: list
    """
    col = Column(column.name, Integer, primary_key=True)

    if col.name in columns:
        return col

    if column.action == DbItem.CREATE:
        col.create(table=table)

    return col


def varchar_updater(column, table, columns):
    """
    Updater for a character varying column.
    :param varchar_column: Character varying column.
    :type varchar_column: VarCharColumn
    :param columns: Existing column names in the database for the given table.
    :type columns: list
    """
    return _update_col(column, table, String(column.maximum), columns)


def text_updater(column, table, columns):
    """
    Updater for a text column.
    :param column: Text column.
    :type column: TextColumn
    :param columns: Existing column names in the database for the given table.
    :type columns: list
    """
    return _update_col(column, table, Text, columns)


def integer_updater(column, table, columns):
    """
    Updater for an integer column.
    :param column: Integer column
    :type column: IntegerColumn
    :param columns: Existing column names in the database for the given table.
    :type columns: list
    """
    return _update_col(column, table, Integer, columns)


def double_updater(column, table, columns):
    """
    SQLAlchemy does not have a corresponding float type so NUMERIC type will be used.
    :param column: Double column
    :type column: DoubleColumn
    :param columns: Existing column names in the database for the given table.
    :type columns: list
    """
    return _update_col(column, table, Numeric, columns)


def date_updater(column, table, columns):
    """
    Updater for a date column.
    :param column: Date column
    :type column: DateColumn
    :param columns: Existing column names in the database for the given table.
    :type columns: list
    """
    return _update_col(column, table, Date, columns)


def datetime_updater(column, table, columns):
    """
    Updater for a date-time column.
    :param column: Date time column
    :type column: DateTimeColumn
    :param columns: Existing column names in the database for the given table.
    :type columns: list
    """
    return _update_col(column, table, DateTime, columns)


def geometry_updater(column, table, columns):
    """
    Updater for a geometry column.
    :param column: Geometry column
    :type column: GeometryColumn
    :param columns: Existing column names in the database for the given table.
    :type columns: list
    """
    geom_type = column.geometry_type()

    return _update_col(column, table, Geometry(geometry_type=geom_type,
                                               srid=column.srid),
                       columns)


def yes_no_updater(column, table, columns):
    """
    Updater for Yes/No column.
    :param column: Yes/No column.
    :type column: BooleanColumn
    :param table: SQLAlchemy table
    :type table: Table
    :param columns: Existing column names in the database for the given table.
    :type columns: list
    """
    return _update_col(column, table, Boolean, columns)
