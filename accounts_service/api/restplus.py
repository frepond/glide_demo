import logging
import traceback

from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound


log = logging.getLogger(__name__)

api = Api(version='0.1', title='Accounts API',
          description='A simple accounts API')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    return {'message': message}, 500


@api.errorhandler(NoResultFound)
def resource_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'Resource not found.'}, 404


@api.errorhandler(AssertionError)
def invalid_data_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': str(e)}, 400
