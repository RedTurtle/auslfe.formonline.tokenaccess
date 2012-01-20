from setuptools import setup, find_packages
import os

version = '0.2.0'

setup(name='auslfe.formonline.tokenaccess',
      version=version,
      description="Plone add-on that enable anonymous use (with secret token) of auslfe.formonline features",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 3.3",
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        ],
      keywords='plonegov form plone token',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='http://plone.org/products/auslfe.formonline.pfgadapter',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['auslfe', 'auslfe.formonline'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'auslfe.formonline.pfgadapter>=0.4.1',
          'auslfe.formonline.content>=0.4.0',
          'collective.powertoken.workflow',
          'collective.powertoken.view'
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
