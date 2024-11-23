from rest_framework.throttling import UserRateThrottle

class LocationRateThrottle(UserRateThrottle):
    rate = '100/hour'
    scope = 'locations'

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            ident = request.user.pk
        else:
            ident = self.get_ident(request)

        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        } 