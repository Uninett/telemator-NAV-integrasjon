from django.http import JsonResponse


def render_api_index(request):
    return JsonResponse({'customer_circuits': 'http://localhost/telemator/api/1.0/customer_circuits/'})
