from zope.interface import Interface, implements
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from collective.conference import _
from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.userdataschema import IUserDataSchema

gender_options = SimpleVocabulary(
    [SimpleTerm(value=u'f', title=_(u'Female')),
     SimpleTerm(value=u'm', title=_(u'Male'))])


def validateAccept(value):
    if not value == True:
        return False
    return True


class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema


class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """
    fullname = schema.TextLine(
        title=_(u'label_fullname', default=u'Full name'),
        description=_(u'help_fullname',
                      default=u"Fill in your full name."),
        required=True,
        )
    identity_document = schema.TextLine(
        title=_(u'label_identity_document', default=u'Identity Document'),
        description=_(u'help_identity_document',
                      default=u"Fill in your ID (for Brazillians only)."),
        required=False,
        )
    issuing_body = schema.TextLine(
        title=_(u'label_issuing body', default=u'Issuing Body'),
        description=_(u'help_issuing body',
                      default=u"Fill in the Issuing body of the ID (for Brazillians only)."),
        required=False,
        )
    cpf = schema.TextLine(
        title=_(u'label_cpf', default=u'CPF'),
        description=_(u'help_cpf',
                      default=u"Fill in your CPF (for Brazillians only)."),
        required=False,
        )
    gender = schema.Choice(
        title=_(u'label_gender', default=u'Gender'),
        description=_(u'help_gender',
                      default=u"Are you a girl or a boy ?"),
        source=gender_options,
        required=True,
        default=u'm',
        )
    passaport_number = schema.TextLine(
        title=_(u'label_passaport_number', default=u'Passaport number'),
        description=_(u'help_passaport_number',
                      default=u"Fill in your passaport number (for non-Brazillians only)."),
        required=False,
        )
    passaport_name = schema.TextLine(
        title=_(u'label_passaport_name', default=u'Passaport name'),
        description=_(u'help_passaport_name',
                      default=u"Your name as wirte in your passaport (for non-Brazillians only)."),
        required=False,
        )
    company_name = schema.TextLine(
        title=_(u'label_company_name', default=u'Company name'),
        description=_(u'help_company_name',
                      default=u"Where do you work ?"),
        required=False,
        )
    company_url = schema.TextLine(
        title=_(u'label_company_url', default=u'Company URL'),
        description=_(u'help_company_url',
                      default=u"Is there an internet site of your Company ?"),
        required=False,
        )
    mini_curriculum = schema.Text(
        title=_(u'label_mini_curriculum', default=u'Mini Curriculum'),
        description=_(u'help_mini_curriculum',
                      default=u"A little description of yourself, if you are a instructor or panelist"),
        required=False,)

    need_special_care = schema.Text(
        title=_(u'label_need_special_care', default=u'Special Care'),
        description=_(u'help_need_special_care',
                      default=u"Do you need special care ?"),
        required=False,)
    social_networks = schema.TextLine(
        title=_(u'label_social_networks', default=u'Social Networks'),
        description=_(u'help_social_networks',
                      default=u"Give us your Ids of Twitter, Facebook, G+, etc..."),
        required=False,
        )
    student_or_APyB_affiliate = schema.Bool(
        title=_(u'label_student_or_APyB_affiliate', default=u'Student or APyB affiliate'),
        description=_(u'help_student_or_APyB_affiliate',
                      default=u"Are you a student or a APyB affiliate (for discount in the fees)"),
        required=True,
        )
    address = schema.TextLine(
        title=_(u'label_address', default=u'Address'),
        description=_(u'help_address',
                      default=u"The address of your home"),
        required=False,
        )
    city = schema.TextLine(
        title=_(u'label_city', default=u'City'),
        description=_(u'help_city',
                      default=u"Fill in the city you live in."),
        required=True,
        )
    state = schema.TextLine(
        title=_(u'label_state', default=u'State'),
        description=_(u'help_state',
                      default=u"Fill in with the state of your city."),
        required=True,
        )
    zip_code = schema.TextLine(
        title=_(u'label_zip_code', default=u'Zip'),
        description=_(u'help_zip_code',
                      default=u"The Zip code of your address"),
        required=False,
        )
    country = schema.TextLine(
        title=_(u'label_country', default=u'Country'),
        description=_(u'help_country',
                      default=u"Fill in the country you live in."),
        required=True,
        )
    citizenship = schema.TextLine(
        title=_(u'label_citizenship', default=u'Citizenship'),
        description=_(u'help_citizenship',
                      default=u"Fill in with your citizenship."),
        required=True,
        )
    phone = schema.TextLine(
        title=_(u'label_phone', default=u'Telephone number'),
        description=_(u'help_phone',
                      default=u"+CountryCode-DDD-Number"),
        required=False,
        )
    cellphone = schema.TextLine(
        title=_(u'label_cellphone', default=u'Cellphone number'),
        description=_(u'help_cellphone',
                      default=u"Leave your phone number so we can reach you. +CountryCode-DDD-Number"),
        required=True,
        )
    accept = schema.Bool(
        title=_(u'label_accept', default=u'Accept terms of use and the Conduct code of the event'),
        description=_(u'help_accept',
                      default=u"Tick this box to indicate that you have found,"
                      " read and accepted the terms of use for this site and the Conduct code of the event. "),
        required=True,
        constraint=validateAccept,
        )

