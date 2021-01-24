from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from account.models import Customer, User

class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ['user', 'created_date']
        extra_kwargs = {"photo": {"required": False}}
        depth = 2

class CustomerListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='account-api:profile', lookup_field='user')
    wish_list = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        exclude = ['user']

    def get_wish_list(self, obj):
        return obj.wish_list.all().count()

    def get_favorites(self, obj):
        return obj.favorites.all().count()

class CustomerCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=250)
    email = serializers.EmailField(label='Email please')
    password = serializers.CharField(style={'input_type':'password', 'placeholder': 'The Password please'})
    password_conf = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Repeat Password please'}, label="Confirm Password")

    class Meta:
        fields = '__all__'
        read_only_fields = ['user']
        model = Customer

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        customer = Customer.objects.create(user=user,
                                first_name=validated_data['first_name'],
                                last_name=validated_data['last_name'],
                                birth_date=validated_data['birth_date'],
                                photo=validated_data['photo'])
        customer.wish_list.set(validated_data['wish_list'])
        customer.favorites.set(validated_data['favorites'])
        return validated_data

    def validate(self, data):
        username = data['username']
        password = data['password']
        password2 = data['password_conf']
        user_qs = User.objects.filter(Q(username=username)).distinct()
        if password != password2:
            raise ValidationError("Passwords don't match")
        elif user_qs is not None:
            raise ValidationError("Such user already exists")
        return data