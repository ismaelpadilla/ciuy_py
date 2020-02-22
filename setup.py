from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='ciuy',
      version='0.3.3',
      description='Python package for validating Uruguayan identity document numbers.',
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
