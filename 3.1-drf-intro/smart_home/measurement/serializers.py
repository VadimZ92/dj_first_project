from rest_framework import serializers
from measurement.models import Sensor, Measurement
# TODO: опишите необходимые сериализаторы

# для датчиков
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

# для измерений
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ["id_sensor", 'temperature', 'created_at']


# для конкретного датчика
class Measurement_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']

class SensorDetailSerializer(serializers.ModelSerializer):
    Measurement = Measurement_Serializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', "Measurement"]