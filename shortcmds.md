# create requirements file 

"
conda list --export > requirements.txt
"

# read requirement file

"
conda create --name tf-gpu --file requirements.txt
"