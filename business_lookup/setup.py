from setuptools import setup, find_packages

setup(
    name='business_lookup',
    version=open('business_lookup/VERSION').readlines()[0].strip(),
    author="FreshBooks",
    author_email="dev@freshbooks.com",
    description="Looks up businesses based on location",
    url="https://github.2ndsiteinc.com/dev/business_lookup",
    packages=find_packages(exclude=['*.test', '*.test.*']),
    include_package_data=True,
    install_requires=open('requirements.txt').readlines(),
    dependency_links=[
        'https://optimus.2ndsiteinc.com/packages/eggs/releases/business_lookup/',
    ],
    entry_points={},
    test_suite='nose.collector'
)
