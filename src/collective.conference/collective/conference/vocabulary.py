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

class DurationVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        terms = []
        levels = [('half_day', _(u'Half day')),
                  ('one_day', _(u'1 day')),
                  ('two_days', _(u'2 days')),
                ]
        for code, text in levels:
            term = (code, code, text)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(DurationVocabulary,
                    name=u"collective.conference.duration")


class LanguagesVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        terms = []
        levels = [('english', _(u'English')),
                  ('portuguese', _(u'Portuguese')),
                  ('spanish', _(u'Spanish')),
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
        levels = [('cloud_system_administration_networks', _(u'Cloud, System Administration and Networks')),
                  ('community_education', _(u'Community and Education')),
                  ('django', _(u'Django')),
                  ('enterprise_management', _(u'Enterprise and Management')),
                  ('media_networks', _(u'Media and Networks')),
                  ('mobility_embedded_systems', _(u'Mobility and Embedded Systems')),
                  ('plone', _(u'Plone')),
                  ('pyramid', _(u'Pyramid')),
                  ('scipy', _(u'Scipy')),
                  ('web_wevelopment', _(u'Web Development')),
                  ('other', _(u'Other')),
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
                  ('advanced', _(u'Advanced')),
                ]
        for code, text in levels:
            term = (code, code, text)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(LevelsVocabulary,
                    name=u"collective.conference.levels")
