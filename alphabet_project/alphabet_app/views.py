from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
import string

@api_view(['GET'])
def get_letter_detail(request, letter):
    if request.method == 'GET':
        if letter.lower() in string.ascii_lowercase:  # Check if provided letter is valid
            data = {
                "uppercase": letter.upper(),
                "lowercase": letter.lower()
            }
            return Response(data)
        else:
            return Response({"error": "Invalid letter"}, status=400)
