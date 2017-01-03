"""
Configuration for the test suite.

"""
import os

TEST_SERVICE = 'http://esgf-index1.ceda.ac.uk/esg-search'
CACHE_FILE = os.path.join(os.path.dirname(__file__), 'url_cache')
