# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.component import getUtility
from zope.annotation.interfaces import IAnnotations
from auslfe.formonline.pfgadapter.interfaces import IFormSharingProvider

from collective.powertoken.core.interfaces import IPowerTokenUtility

class EmailWithTokenSharingProvider(object):
    implements(IFormSharingProvider)
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    def share(self, formonline, overseer):
        """
        Gives to an unknow overseer (an e-mail adress):
         * a temporary Editor role
         * a permanent Reader role
        
        Using collective.powertoken
        """
        utility = getUtility(IPowerTokenUtility)
        tokenView = utility.enablePowerToken(formonline,
                                             'view.viewDocument',
                                             roles=['Owner'],
                                             oneTime=False,
                                             view='tinyview')
        #utility.addAction(formonline, token, 'workflow.doAction')
        tokenApprove = utility.enablePowerToken(formonline,
                                                'workflow.doAction',
                                                roles=['Editor'],
                                                workflow_action='approval')
        IAnnotations(formonline)['share-tokens'] = {'email': overseer,
                                                    'view': tokenView,
                                                    'approve': tokenApprove}
