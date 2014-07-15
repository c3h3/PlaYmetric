from setuptools import setup, find_packages

setup(
    name='PlaYmetric',
    version='0.0.1dev',
    description='metric learning',
    author='Chia-Chi Chang & Yin-Chen Liao',
    author_email='c3h3.tw@gmail.com & qmalliao@gmail.com',
    packages=find_packages(),
    package_data={'': ['*.coffee']},
    install_requires=["numpy",
                      "scipy",
                      "cvxopt",
                      "pandas"],
)
