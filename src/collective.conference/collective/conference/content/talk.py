# -*- coding:utf-8 -*-
from five import grok
from zope import schema
from collective.conference import _
from plone.directives import form
from plone.directives import dexterity


class ITalk(form.Schema):
    """
    A talk in a conference
    """

    estimated_duration = schema.TextLine(
        title=_(u'Estimated duration'),
        description=_(u'How long you want to talk (in minutes)'),
        required=True,
        default=u'60',
    )

    preferred_period = schema.Choice(
        title=_(u"Preferred period"),
        required=True,
        description=_(u"Which track this talk is"),
        vocabulary='collective.conference.periods',
    )

    language_talk = schema.Choice(
        title=_(u"Language"),
        required=True,
        description=_(u"Language this talk will be given"),
        vocabulary='collective.conference.languages',
    )

    global_theme = schema.Choice(
        title=_(u"Global theme"),
        required=True,
        description=_(u"What is the subject of your talk"),
        vocabulary='collective.conference.theme',
    )

    level = schema.Choice(
        title=_(u"Level"),
        required=True,
        description=_(u"Level of this talk"),
        vocabulary='collective.conference.levels',
    )

    observations = schema.Text(
        title=_(u"Observations"),
        required=False,
        description=_(u"Do you want to give us any other information ?"),
    )


class Talk(dexterity.Item):
    grok.implements(ITalk)
