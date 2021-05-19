import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rareapi.models import RareUser
from rest_framework.decorators import api_view


@csrf_exempt
def login_user(request):
    '''Handles the authentication of a rare user

    Method arguments:
      request -- The full HTTP request object
    '''

    req_body = json.loads(request.body.decode())

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        # Use the built-in authenticate method to verify
        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, respond with their token
        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            data = json.dumps({"valid": True, "token": token.key})
            return HttpResponse(data, content_type='application/json')

        else:
            # Bad login details were provided. So we can't log the user in.
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')


@csrf_exempt
def register_user(request):
    '''Handles the creation of a new gamer for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
        username=req_body['username'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name'],
        email=req_body['email'],
        password=req_body['password']
    )

    # Now save the extra info in the levelupapi_gamer table
    rare_user = RareUser.objects.create(
        bio=req_body['bio'],
        profile_image=req_body['profile_image_url'],
        user=new_user
    )
    #Give user default permissions
    permissions = [48]
    new_user.user_permissions.set(permissions)

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=new_user)

    # Return the token to the client
    data = json.dumps({"valid": True, "token": token.key})
    return HttpResponse(data, content_type='application/json')

@api_view()
def check_active(request):
    '''Handles the creation of a new gamer for authentication

    Method arguments:
    request -- The full HTTP request object
    '''

    data = json.dumps({"valid": request.auth.user.is_active, "is_admin": request.auth.user.is_staff})
    return HttpResponse(data, content_type='application/json')