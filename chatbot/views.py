import google.generativeai as genai
from  rest_framework.decorators import api_view
from  rest_framework.response import Response
from  rest_framework import status
import os
from django.shortcuts import render

# Create your views here.
genai.configure(api_key="AIzaSyBh7GpFtHegqJP5edgq3wh6U7NJQQRPEG0")

model=genai.GenerativeModel("gemini-2.0-flash")

@api_view(['POST'])
def chat_with_gemini(request):
    user_input=request.data.get('message',"")

    if not user_input:
        return Response({'error':'message is required'},
    status = status.HTTP_400_BAD_REQUEST)

    try:
        gemini_response = model.generate_content(user_input)
        return Response({'response': gemini_response.text},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def chat_page(request):
    return render(request,'chat.html')