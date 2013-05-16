# -*- coding: utf-8 -*-
from five import grok
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from collective.conference import _


class PeriodsVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        terms = []
        levels = [('morning', _(u'Morning')),
                  ('afternon', _(u'Afternon')),
                ]
        for code, text in levels:
            term = (code, code, text)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(PeriodsVocabulary,
                    name=u"collective.conference.periods")


class LanguagesVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        terms = []
        levels = [('english', _(u'English')),
                  ('spanish', _(u'Spanish')),
                  ('portuguese', _(u'Portuguese')),
                ]
        for code, text in levels:
            term = (code, code, text)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(LanguagesVocabulary,
                    name=u"collective.conference.languages")


class ThemeVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        terms = []
        levels = [('django', _(u'Django')),
                  ('pyramid', _(u'Pyramid')),
                  ('scipy', _(u'Scipy')),
                  ('plone', _(u'Plone')),
                  ('web_wevelopment', _(u'Web Development')),
                  ('mobility_embedded_systems', _(u'Mobility and Embedded Systems')),
                  ('enterprise_management', _(u'Enterprise and Management')),
                  ('community_education', _(u'Community and Education')),
                  ('cloud_system_administration_networks', _(u'Cloud, System Administration and Networks')),
                  ('media_networks', _(u'Media and Networks')),
                ]
        for code, text in levels:
            term = (code, code, text)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(ThemeVocabulary,
                    name=u"collective.conference.theme")


class LevelsVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        ''' Look for an enclosing program
            list available languages in it '''
        terms = []
        levels = [('basic', _(u'Basic')),
                  ('intermediate', _(u'Intermediate')),
                  ('advanced', _(u'Advanced')),
                ]
        for code, text in levels:
            term = (code, code, text)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(LevelsVocabulary,
                    name=u"collective.conference.levels")
