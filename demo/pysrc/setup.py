from setuptools import setup, find_packages

package_name = 'demo'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(),
    package_data={package_name: ['*.so']},    # also copy .so during installation
    include_package_data=True,
)
