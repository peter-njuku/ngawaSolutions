from device_detector import DeviceDetector

class DeviceDetectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        device = DeviceDetector(user_agent).parse()

        if device.is_mobile():
            request.device_type = 'mobile'
        elif device.device_type() == 'desktop':
            request.device_type = 'desktop'
        else:
            request.device_type = 'unknown'

        return self.get_response(request)
