from schema.gps_schema import GpsSchema
from marshmallow import Schema, fields

class GroundClearanceSchema(Schema):
    length = fields.Number()
    gps = fields.Nested(GpsSchema)