from rest_framework.serializers import ModelSerializer
from app1.models import books
class herosSerializer(ModelSerializer):
    class Meta:
        model=books
        fields='__all__'