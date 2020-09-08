from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='wagtailrestaurantmenus',
    version="0.0.1",
    description='StreamField code blocks for the Wagtail CMS framework to easily create restaurant menus.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Kay Wilkinson',
    author_email='kaywilkinson@cerealboxmedia.com',
    url='https://github.com/CerealBoxMedia/wagtail-restaurant-menus',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'wagtail>=2',
    ],
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)