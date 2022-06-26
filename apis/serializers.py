from rest_framework import serializers

from info_doctor.models import LineOfAction, Doctor


class LineOfActionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LineOfAction
        fields = ('url', 'title', 'slug')


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    line_of_action = LineOfActionSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ('url', 'full_name', 'line_of_action', 'slug', 'description', 'date_of_birth',
                  'work_experience')
