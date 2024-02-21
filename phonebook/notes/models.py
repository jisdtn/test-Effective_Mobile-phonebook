
class Contact:
    """The model of Contact"""
    def __init__(self, last_name, first_name,
                 middle_name, organization,
                 work_phone, personal_phone):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.organization = organization
        self.work_phone = work_phone
        self.personal_phone = personal_phone

    def __str__(self):
        return f"{self.last_name} " \
               f"{self.first_name} " \
               f"{self.middle_name} - " \
               f"{self.organization} - " \
               f"{self.work_phone} - " \
               f"{self.personal_phone}"
