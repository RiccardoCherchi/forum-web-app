from django.contrib.auth.mixins import UserPassesTestMixin

class StaffMixing(UserPassesTestMixin):
    """ lo scopo di questo mixin e permettere solo allo staff di creare nuove sezioni """

    def test_func(self):
        return self.request.user.is_staff