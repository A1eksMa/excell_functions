# web
import urllib.parse
import xml.etree.ElementTree as ET
import requests

# ENCODEURL function
def ENCODEURL(url):
    '''
    Returns a URL-encoded string
    
    The function converts a URL into a URL-encoded format, making it safe to use in web addresses.
    '''
    encoded_url = urllib.parse.quote(url, safe='')
    return encoded_url


# FILTERXML function
def FILTERXML(xml_content, xpath_query):
    '''
    Returns specific data from the XML content by using the specified XPath
    
    The FILTERXML function is used to extract data from XML content based on a specified XPath query.
    '''
    root = ET.fromstring(xml_content)
    result = root.findall(xpath_query)
    return [elem.text for elem in result]


# WEBSERVICE function
def WEBSERVICE(url):
    '''
    Returns data from a web service
    
    The WEBSERVICE function allows users to retrieve data from a web service by sending an HTTP request to a specified URL.
    '''
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


