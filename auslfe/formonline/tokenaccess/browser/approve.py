# -*- coding: utf-8 -*-

from collective.powertoken.core.exceptions import PowerTokenSecurityError
from collective.powertoken.core.browser.consume_token import ConsumePowerTokenView
from zope.interface import Interface, implements

class ApproveFormOnlineView(ConsumePowerTokenView):
    
    def __call__(self, *args, **kw):
        self.request.set('disable_border', 1)
        # following two only on Plone 4+
        self.request.set('disable_plone.leftcolumn', 1)
        self.request.set('disable_plone.rightcolumn', 1)
        self.error = False
        try:
            self.result = ConsumePowerTokenView.__call__(self, *args, **kw)[0]
        except PowerTokenSecurityError:
            self.result = None
            self.error = True
        return self.index()