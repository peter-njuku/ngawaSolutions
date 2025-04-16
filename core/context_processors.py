import datetime

def current_year():
    return {
        'current_year':datetime.datetime.now().year
    }
# context_processors.py
def device_type(request):
    return {'device_type': getattr(request, 'device_type', 'unknown')}
