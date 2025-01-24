from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return render(request,'test.html' )

def home(request):
    return HttpResponse("Hello, Django!")

def process_inputs(request):
    input1 = request.GET.get('latitude', '')
    input2 = request.GET.get('longitude', '')

    response_data = {
        'latitude': input1,
        'longitude': input2,
        'message': 'Inputs received successfully'
    }

    return JsonResponse(response_data)

def update_location(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        print(f"Received latitude: {latitude}, longitude: {longitude}")

        return JsonResponse({'status': 'success', 'latitude': latitude, 'longitude': longitude})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)