from marshmallow import Schema, fields
from schema.accelerometer_schema import AccelerometerSchema
from schema.gps_schema import GpsSchema
from schema.ground_clearance_schema import GroundClearanceSchema
class AggregatedDataSchema(Schema):
    accelerometer = fields.Nested(AccelerometerSchema)
    gps = fields.Nested(GpsSchema)
    ground_clearance = fields.Nested(GroundClearanceSchema)
    timestamp = fields.DateTime('iso')
