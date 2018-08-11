version = '0.1'
REQUIRED_PYTHON = (3, 0)

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='Mage knight API',
    version=version,
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
    url='',
    author='Gus',
    author_email='guillaume1.dubus@gmail.com',
    description=('A full API to handle mage knight board game actions'),
    long_description=read('README.md'),
    license='MIT',
    project_urls={
        'Documentation': '',
        'Source': 'https://github.com/suipotryot/mage_knight',
    },
)
