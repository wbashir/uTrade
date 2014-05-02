from marshmallow import Serializer, fields


class ItemSerializer(Serializer):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()


class ItemsSerializer(Serializer):

    class Meta:
        additional = ('id', 'title')

