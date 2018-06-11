from rest_framework import serializers

from zrc.datamodel.models import Status, Zaak, ZaakObject


class ZaakSerializer(serializers.HyperlinkedModelSerializer):
    status = serializers.HyperlinkedRelatedField(
        source='current_status_pk', read_only=True,
        view_name='status-detail',
        help_text="Indien geen status bekend is, dan is de waarde 'null'"
    )

    class Meta:
        model = Zaak
        fields = (
            'url',
            'zaakidentificatie',
            'zaaktype',
            'registratiedatum',
            'toelichting',
            'status'
        )


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = (
            'url',
            'zaak',
            'status_type',
            'datum_status_gezet',
            'statustoelichting'
        )


class ZaakObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZaakObject
        fields = (
            'url',
            'zaak',
            'object',
            'relatieomschrijving'
        )
