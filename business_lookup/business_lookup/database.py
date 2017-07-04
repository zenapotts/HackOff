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
