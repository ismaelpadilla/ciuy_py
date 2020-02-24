from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='ciuy',
      version='0.3.5',
      description='Python package for validating Uruguayan identity document numbers.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      keywords=["Uruguay", "dni", "id", "eid", "validation", "cédula", "cédula uruguaya"],
      url='https://github.com/ismaelpadilla/ciuy_py',
      project_urls={
          "Documentation": "https://ciuy.readthedocs.io/"
      },
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
