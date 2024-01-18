import unittest
from test_class.profile_validation import ProfileValidationTests

# Load the test case class
class_name = ProfileValidationTests

# Create a test loader
loader = unittest.TestLoader()

# Load the test methods in the desired order
class_methods = [
    class_name('test_add_profile'),
    class_name('test_add_profile_stake'),
    class_name('test_challenge_evidence'), 
    class_name('test_juror_stake'),
    class_name('test_change_period_from_evidence'),
    class_name('test_draw_juror'),
    class_name('test_change_period_from_staking')
]

# Create a test suite
test_suite = unittest.TestSuite(class_methods)

runner = unittest.TextTestRunner()


# Run the test suite
runner.run(test_suite)