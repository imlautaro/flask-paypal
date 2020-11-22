from setuptools import setup


setup(
    name="Flask-PayPal",
    version="0.1",
    url="https://github.com/imlautaro/flask-paypal",
    license="MIT",
    author="Lautaro Pereyra",
    author_email="dev.lautaropereyra@gmail.com",
    description="An easy way to integrate PayPal with Flask",
    long_description=__doc__,
    packages=['flask_paypal']
    zip_safe=False,
    include_package_data=True,
    platform="any",
    install_requires=[
        'Flask',
        'requests'
    ]
)
