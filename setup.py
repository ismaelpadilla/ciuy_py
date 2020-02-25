from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='ciuy',
      version='0.4.0',
      python_requires=">=3.4",
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
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8"
      ],
      packages=['ciuy'],
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'validate_ci = ciuy.command_line:cmd_validate_ci'
          ]
      },
      zip_safe=True)
