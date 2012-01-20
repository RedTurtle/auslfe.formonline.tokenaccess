# -*- coding: utf-8 -*-

from Acquisition import aq_inner
from zope.component import getMultiAdapter
from zope.annotation import IAnnotations
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common

class ChangeStateLinkViewlet(common.ViewletBase):
    
    render = ViewPageTemplateFile('change_state_link.pt')

    @property
    def portal_workflow(self):
        context = aq_inner(self.context)
        return getMultiAdapter((context, self.request), name=u'plone_tools').workflow()

    @property
    def tokens(self):
        return IAnnotations(self.context).get('share-tokens')

    def approveUrl(self):
        portal_url = getToolByName(self.context, 'portal_url')
        targetUrl = self.request.get('path').replace("%s/" % portal_url(), "")
        return "%s/@@approveFormOnline?path=%s&token=%s" % (self.site_url, targetUrl, self.tokens['approve'])

    def rejectUrl(self):
        portal_url = getToolByName(self.context, 'portal_url')
        targetUrl = self.request.get('path').replace("%s/" % portal_url(), "")
        return "%s/@@approveFormOnline?path=%s&token=%s" % (self.site_url, targetUrl, self.tokens['reject'])

    def checkToken(self):
        token = self.request.form.get('token')
        saved_tokens = self.tokens
        if saved_tokens and saved_tokens.get('view'):
            return saved_tokens.get('view') == token
        return False
