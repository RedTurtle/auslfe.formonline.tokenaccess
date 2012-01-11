Introduction
============

Enable anonymous use of `auslfe.formonline.pfgadapter`__ features using e-mail containing a secret token.
Token feature came from `collective.powertoken`__ suite.

__ http://plone.org/products/auslfe.formonline.pfgadapter
__ http://plone.org/collective.powertoken.core

How to install
==============

Simply add ``auslfe.formonline.tokenaccess`` to your buildout::

    [instance]
    recipe = plone.recipe.zope2instance
    ...
    eggs =
        Plone
        ...
        auslfe.formonline.pfgadapter
        auslfe.formonline.tokenaccess

How to use
==========

``auslfe.formonline.pfgadapter`` (version 0.4 or better) already check your Zope installation looking for
``auslfe.formonline.tokenaccess``. If it is found you'll get some new features:

* The "*Overseer e-mail*" can also not be an internal e-mail (a new check option in the PFG adapter
  "*Overseer must be a site member*" will be found).
* An external overseer can now access a special site's page, where he can see the sent form and approve it.

The overseer will receive the common confirmation e-mail with a special link that show the document (even if
in not accessible state). Note that **this link is permanently valid**.
From this view another link is shown, for approve the document. This second link is valid only once.

**Please note** that the e-mail sent to the external overseer is a clean way to bypass Plone security. If
this e-mail and data inside is used by a malicous user, he will be able to see reserver data and approve it.

I want Anonymous users also for posting new forms
-------------------------------------------------

You can also configure your Plone site to allow anonymous users to add Form Online. What you simply need is
to give to ``Anonymous`` role following permission:

* ``auslfe.formonline.content: Add FormOnline``
* ``Request review``

For security reason is better to give those permissions only onto the folder where you want to store generated
document.

You can do this using a specific workflow, a workflow policy or (**not suggested**) simply giving this
permission directly from ZMI on the target folder.

Credits
=======

Developed with the support of `S. Anna Hospital, Ferrara`__;
S. Anna Hospital supports the `PloneGov initiative`__.

.. image:: http://www.ospfe.it/ospfe-logo.jpg 
   :alt: S. Anna Hospital logo

__ http://www.ospfe.it/
__ http://www.plonegov.it/

Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.it/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/
