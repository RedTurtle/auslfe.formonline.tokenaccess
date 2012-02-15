# -*- coding: utf-8 -*-

from zope.annotation import IAnnotations
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common

class ChangeStateLinkViewlet(common.ViewletBase):
    
    render = ViewPageTemplateFile('change_state_commands.pt')

    @property
    def tokens(self):
        return IAnnotations(self.context).get('share-tokens')

    def checkToken(self):
        token = self.request.form.get('token')
        saved_tokens = self.tokens
        if token and saved_tokens and saved_tokens.get('view'):
            return saved_tokens.get('view') == token
        return False
