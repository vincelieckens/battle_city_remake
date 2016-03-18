try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description' : 'A personal interpretation of the classic NES game Battle City',
        'author' : 'Vince Lieckens',
        'url' : 'URL to get it at.',
        'download_url' : 'Where to download it.',
        'author_email' : 'vincelieckens@msn.com',
        'version' : '0.1',
        'install_requires' : ['nose'],
        'packages' : ['battle_city_remake'],
        'scripts' : [],
        'name' : 'battle_city_remake'
    }
    
setup(**config)
 
