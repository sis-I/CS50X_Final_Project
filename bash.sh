echo "BUILD START"
# create a virtual environment named 'venv' if it doesn't already exist
python3.12 -m venv venv

# activate the virtual environment
source venv/bin/activate

echo "Install Dependencies"

pip install -r requirements.txt

echo "BUILD END"