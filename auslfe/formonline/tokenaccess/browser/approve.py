# -*- coding: utf-8 -*-

from zope.annotation import IAnnotations
from collective.powertoken.core.exceptions import PowerTokenSecurityError
from collective.powertoken.core.browser.consume_token import ConsumePowerTokenView
from auslfe.formonline.tokenaccess import messageFactory as _

class ApproveFormOnlineView(ConsumePowerTokenView):
    
    def __call__(self, *args, **kw):
        context = self.context
        request = self.request
        request.set('disable_border', 1)
        # following two only on Plone 4+
        request.set('disable_plone.leftcolumn', 1)
        request.set('disable_plone.rightcolumn', 1)
        self.error = False
        
        token = request.form.get('token')
        path = request.form.get('path')
        comment = request.form.get('comment', None)
        
        doc = context.unrestrictedTraverse(path)
        conf = IAnnotations(doc).get('share-tokens')
        
        if conf.get('reject') and conf.get('reject')==token and not comment.strip():
            # comment when rejecting is required
            context.plone_utils.addPortalMessage(_(u'When rejecting, a motivation is required'),
                                                 type='error')
            request.response.redirect(request.form.get('came_from') or context.absolute_url())
            return
        
        try:
            self.result = ConsumePowerTokenView.__call__(self, comment=comment, **kw)[0]
        except PowerTokenSecurityError:
            self.result = None
            self.error = True
        return self.index()