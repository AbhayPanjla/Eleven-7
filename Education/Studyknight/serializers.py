
from rest_framework import serializers
from .models import SSC,GD
class students(serializers.ModelSerializer):
    class Meta:
        model = SSC
        fields = "__all__"    

class teachers(serializers.ModelSerializer):
    class Meta:
        models = GD 
        fields = "__all__"       

        