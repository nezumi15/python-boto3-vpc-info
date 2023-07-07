from setuptools import setup, find_packages

setup(
    name='my_package',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'boto3',
    ],
    entry_points={
        'console_scripts': [
            'vpc_menu = my_package.vpc_menu:main',
            'vpc_ngw = my_package.vpc_ngw:lambda_handler',
            'vpc_rt = my_package.vpc_rt:lambda_handler',
            'vpc_s3_endpoints = my_package.vpc_s3_endpoints:lambda_handler',
            'vpc_tgw = my_package.vpc_tgw:lambda_handler',
            'vpc_vpg = my_package.vpc_vpg:lambda_handler',
        ],
    },
)
