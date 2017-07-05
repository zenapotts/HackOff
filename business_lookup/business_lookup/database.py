from flask_sqlalchemy import SQLAlchemy
from business_lookup.error import DatabaseError
from sqlalchemy import event, exc
from sqlalchemy.pool import Pool
import logging


db = SQLAlchemy()
log = logging.getLogger(__name__)


@event.listens_for(Pool, 'checkout')
def ping_connection(dbapi_connection, connection_record, connection_proxy):
    """
    Because business_lookup sometimes goes many hours without a request
    we need to gracefully handle MySQL killing our connections.
    While the pool_recycle catches most of this, it misses an annoying case
    where the we get 0 requests for longer than the pool_recycle + timeout
    length.
    """
    cursor = dbapi_connection.cursor()
    try:
        cursor.execute('SELECT 1')
        cursor.close()
    except:
        log.info('Connection in pool has timed out and will be reconnected.')
        # The connection died before it was recycled.
        # Raise an exception force a reconnection.
        raise exc.DisconnectionError()

def search_database(city, country, profession):
    response_list = []

    command = "select * from system where lower (city) = '" + city.lower() + \
        "' and lower(country) = '" + country.lower() + \
        "' and lower(profession) = '" + profession.lower() + "' and active = '1'"
    with db.engine.connect() as con:
        rs = con.execute(command)
        for row in rs:
            new_dict = {}
            new_dict['name'] = row['name']
            new_dict['street'] = row['street']
            new_dict['city'] = row['city']
            new_dict['province'] = row['province']
            new_dict['country'] = row['country']
            new_dict['bus_phone'] = row['bus_phone']
            new_dict['info_email'] = row['info_email']
            new_dict['profession'] = row['profession']
            response_list.append(new_dict)

    return response_list

def save(instance):
    db.session.add(instance)
    db.session.flush()
    return instance


def commit_request_transaction(response):
    try:
        db.session.commit()
    except:
        raise DatabaseError
    return response


db.Model.save = save
