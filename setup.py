from setuptools import setup


setup(name="systeminfo1",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="Pavinee Kavanagh",
      author_email="pavinee.kavanagh@ucdconnect.ie",
      licence="GPL3",
      packages=['systeminfo'],
      entry_points={
          'console_scripts':['comp30670_systeminfo1=systeminfo.main:main'],
        }
      )
