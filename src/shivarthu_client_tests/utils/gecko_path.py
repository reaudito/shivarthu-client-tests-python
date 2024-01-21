import os


current_directory = os.path.dirname(os.path.realpath(__file__))

project_src = os.path.abspath(os.path.join(current_directory, '..', '..'))
gecko_driver_path = os.path.join(project_src, 'geckodriver', 'geckodriver')