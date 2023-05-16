from setuptools import setup
from setuptools import find_packages

# to install required packages run -  pip install -e .
setup(
    name="etif",
    version="1.0.0",
    url="http://localhost/",
    description="API template using Flask Python",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[ 
        "Flask==2.2.3",
        "Flask-Injector==0.14.0",
        "injector==0.20.1",
        "pymongo==3.11.4",
        "pyclean==2.0.0",
        "flask-cors==3.0.10",
        "boto3==1.24.75",
]
)