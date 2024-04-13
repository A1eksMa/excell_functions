# users
import requests
import itertools

# CALL function
def CALL(dll_path, function_name, *args):
    '''
    Calls a procedure in a dynamic link library or code resource
    
    CALL() function is used to call a procedure or function defined in a dynamic link library (DLL) or code resource.
    '''
    dll = ctypes.CDLL(dll_path)
    func = getattr(dll, function_name)
    return func(*args)


# EUROCONVERT function
def EUROCONVERT():
    '''
    Converts a number to euros, converts a number from euros to a euro member currency, or converts a number from one euro member currency to another by using the euro as an intermediary (triangulation)
    
    The EUROCONVERT function converts a currency amount to euros, given the amount, source currency, target currency, and an optional date for conversion.
    '''
    
    url = "https://api.exchangerate-api.com/exchange"
    
    if date:
        url += f"/{date}"
    
    url += f"/{source_currency}/{target_currency}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        conversion_rate = response.json()
        converted_amount = amount * conversion_rate
        return converted_amount
    else:
        return "Error in conversion. Please check your inputs."


# REGISTER.ID function
def REGISTER_ID():
    '''
    Returns the register ID of the specified dynamic link library (DLL) or code resource that has been previously registered
    
    The function generate unique IDs sequentially.

    Example Usage:
    id_generator = REGISTER_ID()
    next(id_generator)  # Output: 1
    next(id_generator)  # Output: 2
    next(id_generator)  # Output: 3
    '''
    for i in itertools.count(1):
        yield i


