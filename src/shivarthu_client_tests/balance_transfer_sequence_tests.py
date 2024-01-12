import unittest
from test_class.balance_tranfer import BalanceTransfers

# Load the test case class
class_name = BalanceTransfers

# Create a test loader
loader = unittest.TestLoader()

# Load the test methods in the desired order
class_methods = [
    class_name('test_balance_transfer'),
    class_name('test_balance_transfer2'), 
    class_name('test_balance_transfer3'),  
    class_name('test_balance_transfer4'),  
    class_name('test_balance_transfer5'),  
    # class_name('test_balance_transfer6'),  
    # class_name('test_balance_transfer7'),   
    # class_name('test_balance_transfer8'),  
]

# Create a test suite
test_suite = unittest.TestSuite(class_methods)

runner = unittest.TextTestRunner()


# Run the test suite
runner.run(test_suite)