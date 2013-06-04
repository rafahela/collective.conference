from plone.app.users.browser.personalpreferences import UserDataPanelAdapter

class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    def get_fullname(self):
        return self.context.getProperty('fullname', '')

    def set_fullname(self, value):
        return self.context.setMemberProperties({'fullname': value})
    fullname = property(get_fullname, set_fullname)

    def get_identity_document(self):
        return self.context.getProperty('identity_document', '')

    def set_identity_document(self, value):

        return self.context.setMemberProperties({'identity_document': value})
    identity_document = property(get_identity_document, set_identity_document)

    def get_issuing_authority(self):
        return self.context.getProperty('issuing_authority', '')

    def set_issuing_authority(self, value):
        return self.context.setMemberProperties({'issuing_authority': value})
    issuing_authority = property(get_issuing_authority, set_issuing_authority)

    def get_cpf(self):
        return self.context.getProperty('cpf', '')

    def set_cpf(self, value):
        return self.context.setMemberProperties({'cpf': value})
    cpf = property(get_cpf, set_cpf)

    def get_gender(self):
        return self.context.getProperty('gender', '')

    def set_gender(self, value):
        return self.context.setMemberProperties({'gender': value})
    gender = property(get_gender, set_gender)

    def get_passaport_number(self):
        return self.context.getProperty('passaport_number', '')

    def set_passaport_number(self, value):
        return self.context.setMemberProperties({'passaport_number': value})
    passaport_number = property(get_passaport_number, set_passaport_number)

    def get_passaport_name(self):
        return self.context.getProperty('passaport_name', '')

    def set_passaport_name(self, value):
        return self.context.setMemberProperties({'passaport_name': value})
    passaport_name = property(get_passaport_name, set_passaport_name)

    def get_company_name(self):
        return self.context.getProperty('company_name', '')

    def set_company_name(self, value):
        return self.context.setMemberProperties({'company_name': value})
    company_name = property(get_company_name, set_company_name)

    def get_company_website(self):
        return self.context.getProperty('company_website', '')

    def set_company_website(self, value):
        return self.context.setMemberProperties({'company_website': value})
    company_website = property(get_company_website, set_company_website)

    def get_mini_resume(self):
        return self.context.getProperty('mini_resume', '')

    def set_mini_resume(self, value):
        return self.context.setMemberProperties({'mini_resume': value})
    mini_resume = property(get_mini_resume, set_mini_resume)

    def get_need_special_care(self):
        return self.context.getProperty('need_special_care', '')

    def set_need_special_care(self, value):
        return self.context.setMemberProperties({'need_special_care': value})
    need_special_care = property(get_need_special_care, set_need_special_care)

    def get_social_networks(self):
        return self.context.getProperty('social_networks', '')

    def set_social_networks(self, value):
        return self.context.setMemberProperties({'social_networks': value})
    social_networks = property(get_social_networks, set_social_networks)

    def get_student_or_APyB_affiliated(self):
        return self.context.getProperty('student_or_APyB_affiliated', '')

    def set_student_or_APyB_affiliated(self, value):
        return self.context.setMemberProperties({'student_or_APyB_affiliated': value})
    student_or_APyB_affiliated = property(get_student_or_APyB_affiliated, set_student_or_APyB_affiliated)

    def get_address(self):
        return self.context.getProperty('address', '')

    def set_address(self, value):
        return self.context.setMemberProperties({'address': value})
    address = property(get_address, set_address)

    def get_city(self):
        return self.context.getProperty('city', '')

    def set_city(self, value):
        return self.context.setMemberProperties({'city': value})
    city = property(get_city, set_city)

    def get_state(self):
        return self.context.getProperty('state', '')

    def set_state(self, value):
        return self.context.setMemberProperties({'state': value})
    state = property(get_state, set_state)

    def get_country(self):
        return self.context.getProperty('country', '')

    def set_country(self, value):
        return self.context.setMemberProperties({'country': value})
    country = property(get_country, set_country)

    def get_zip_code(self):
        return self.context.getProperty('zip_code', '')

    def set_zip_code(self, value):
        return self.context.setMemberProperties({'zip_code': value})
    zip_code = property(get_zip_code, set_zip_code)

    def get_citizenship(self):
        return self.context.getProperty('citizenship', '')

    def set_citizenship(self, value):
        return self.context.setMemberProperties({'citizenship': value})
    citizenship = property(get_citizenship, set_citizenship)

    def get_phone(self):
        return self.context.getProperty('phone', '')

    def set_phone(self, value):
        return self.context.setMemberProperties({'phone': value})
    phone = property(get_phone, set_phone)

    def get_mobile_phone(self):
        return self.context.getProperty('mobile_phone', '')

    def set_mobile_phone(self, value):
        return self.context.setMemberProperties({'mobile_phone': value})
    mobile_phone = property(get_mobile_phone, set_mobile_phone)

    def get_accept(self):
        return self.context.getProperty('accept', '')

    def set_accept(self, value):
        return self.context.setMemberProperties({'accept': value})
    accept = property(get_accept, set_accept)


