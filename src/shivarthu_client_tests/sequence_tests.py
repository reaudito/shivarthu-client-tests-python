import unittest
from test_class.profile_validation import ProfileValidationTests

# Load the test case class
profile_validation_class = ProfileValidationTests

# Create a test loader
loader = unittest.TestLoader()

# Load the test methods in the desired order
profile_validation_methods = [
    profile_validation_class('test_add_profile'),
    profile_validation_class('test_add_profile_stake'),    
]

# Create a test suite
test_suite = unittest.TestSuite(profile_validation_methods)

runner = unittest.TextTestRunner()


# Run the test suite
runner.run(test_suite)