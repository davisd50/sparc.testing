from setuptools import setup, find_packages

version = '0.0.4'

setup(name='sparc.testing',
      version=version,
      description="testing for the SPARC platform",
      long_description=open("README.md").read() + "\n" +
                       open("HISTORY.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Framework :: Zope3',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3"
      ],
      keywords=['zca'],
      author='David Davis',
      author_email='davisd50@gmail.com',
      url='https://github.com/davisd50/sparc.testing',
      download_url = '',
      license='MIT',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sparc'],
      include_package_data=True,
      package_data = {
          '': ['*.zcml']
        },
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.testing', # required for cleanup()
          'zope.testrunner', # required for stand-alone-file test executions
          'zope.interface',
          'zope.component',
          'zope.schema' # needed for vocabulary registry
      ],
      extras_require = {
          'zcml': ['zope.configuration',
                   'zope.i18nmessageid'],
          'security': ['zope.location',
                       'zope.proxy',
                       'zope.security']
      },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
