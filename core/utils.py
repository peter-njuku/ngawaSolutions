from device_detector import DeviceDetector

def get_device_type(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device = DeviceDetector(user_agent).parse()

    if device.is_mobile():
        return 'mobile'
    elif device.device_type() == 'desktop':
        return 'desktop'
    else:
        return 'unknown'
