from setuptools import setup, find_packages
setup(name = "census-income",
      version  = "0.0.1",
      author = "amin",
      author_email = "amin.ravjani@gmail.com",
      packages = find_packages(),
      install_requires = ["pandas", "numpy","scipy", "flask"]
      )