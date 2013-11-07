from datetime import datetime, date

import arrow
from flask.json import JSONEncoder as FlaskJSONEncoder

from app.models.base import BaseModel


class JSONEncoder(FlaskJSONEncoder):
    """JSON Encoder. An extension of the Flask JSONEncoder that handles better
    datetime/date conversions.
    """
    def default(self, o):
        """Perform conversions from datetime/date to timestamp"""
        if isinstance(o, BaseModel):
            return o.to_dict()
        if isinstance(o, datetime):
            return arrow.Arrow.fromdatetime(o).timestamp
        if isinstance(o, date):
            return arrow.Arrow.fromdate(o).timestamp
        if isinstance(o, arrow.Arrow):
            return o.timestamp
        return FlaskJSONEncoder.default(self, o)
