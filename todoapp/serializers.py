from rest_framework import serializers
from todoapp import models

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields =('id', 'name', 'email', 'password')
      

        def create(self, validated_data):
           
            user = models.UserProfile.objects.create_user(
                email = self.validated_data['email'],
                name = self.validated_data['name'],
                password = self.validated_data['password']
               
                )
            
            return user

class UserTodoItemsSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.UserTodoList
        fields = ('user', 'todo', 'guide_lines', 'created_on')
        extra_kwargs = {'user':{'read_only':True}}
        