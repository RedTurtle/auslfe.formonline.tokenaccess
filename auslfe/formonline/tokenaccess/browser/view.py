# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from zope.interface import Interface, implements

class ITinyView(Interface):
    pass

class TinyView(BrowserView):
    implements(ITinyView)
    
    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        self.request.set('disable_border', 1)
        # following two only on Plone 4+
        self.request.set('isable_plone.leftcolumn', 1)
        self.request.set('isable_plone.rightcolumn', 1)
        