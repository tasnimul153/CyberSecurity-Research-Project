from distutils.core import setup
setup(
  name = 'BingImages',         # How you named your package folder (MyLib)
  packages = ['BingImages'],   # Chose the same as "name"
  version = '0.62',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Use the bing image search engine to get image-links for your topics',   # Give a short description about your library
  author = 'Joel Barmettler',                   # Type in your name
  author_email = 'joel.barmettler@uzh.ch',      # Type in your E-Mail
  url = 'https://github.com/joelbarmettlerUZH/BingImages',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/joelbarmettlerUZH/BingImages/archive/v_062.tar.gz',    # I explain this later on
  keywords = ['Bing', 'Images', 'Search', 'engine', 'download', 'scraping'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',   # Again, pick a license

    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)