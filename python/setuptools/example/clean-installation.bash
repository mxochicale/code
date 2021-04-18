rm -rf build 
rm -rf dist
rm -rf My_First_Setup_File.egg-info
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf # https://stackoverflow.com/questions/28991015
