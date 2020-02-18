from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='ciuy',
      version='0.3.1',
      description='Package for validating Uruguayan ids (work in progress).',
      long_description=long_description,
      long_description_content_type="text/markdown",
      keywords=["Uruguay", "dni", "id", "eid", "validation"],
      url='https://github.com/ismaelpadilla/ci_uy_py',
      author='Ismael Padilla',
      author_email='padillaismael92@gmail.com',
      license='MIT',
      classifiers=[
          "Development Status :: 4 - Beta",
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      packages=['ciuy'],
      include_package_data=True,
      zip_safe=True)

'''
TODO
    long_description
    keywords
READ
    https://packaging.python.org/guides/distributing-packages-using-setuptools/
'''
