from setuptools import setup, find_packages

setup(
    name='ckanext-remove_login_icon',
    version='0.1',
    description='CKAN extension to remove login symbol from the starting page',
    author='Your Name',
    author_email='your.email@example.com',
    license='AGPL',
    url='https://github.com/your-repo/ckanext-remove_login_icon',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points='''
        [ckan.plugins]
        remove_login_icon=ckanext.remove_login_icon.plugin:RemoveLoginIconPlugin
    ''',
)