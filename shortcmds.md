# create requirements file 

"
conda list --export > requirements.txt
or
pip freeze > requirements.txt
"

# read requirement file

"
conda create --name tf-gpu --file requirements.txt
or 
pip install -r requirements.txt
"

Note: make sure you have admin rights to install packages and run the system