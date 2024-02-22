from .models import customer, rocket, payload, launch
from rest_framework import serializers

class customerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = customer
        fields = '__all__'
        
class rocketSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = rocket
        fields = '__all__'
        
class payloadSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = payload
        fields = '__all__'
        
class launchSerializer(serializers.HyperlinkedModelSerializer):
    
    rockets = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = launch
        fields = '__all__'