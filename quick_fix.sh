#!/bin/bash

echo "=== Checking PEP8 issues in console.py ==="
pycodestyle console.py

echo -e "\n=== Checking PEP8 issues in models/ ==="
pycodestyle models/

echo -e "\n=== Checking PEP8 issues in tests/ ==="
pycodestyle tests/

echo -e "\n=== Checking if all models have __tablename__ ==="
grep -n "__tablename__" models/state.py || echo "✗ state.py missing __tablename__"
grep -n "__tablename__" models/city.py || echo "✗ city.py missing __tablename__"
grep -n "__tablename__" models/user.py || echo "✗ user.py missing __tablename__"
grep -n "__tablename__" models/place.py || echo "✗ place.py missing __tablename__"
grep -n "__tablename__" models/review.py || echo "✗ review.py missing __tablename__"
grep -n "__tablename__" models/amenity.py || echo "✗ amenity.py missing __tablename__"

echo -e "\n=== Testing imports ==="
python3 -c "from models.base_model import BaseModel; print('✓ BaseModel imports OK')" 2>&1
python3 -c "from models.state import State; print('✓ State imports OK')" 2>&1
python3 -c "from models.city import City; print('✓ City imports OK')" 2>&1
python3 -c "from models.user import User; print('✓ User imports OK')" 2>&1
python3 -c "from models.place import Place; print('✓ Place imports OK')" 2>&1
python3 -c "from models.review import Review; print('✓ Review imports OK')" 2>&1
python3 -c "from models.amenity import Amenity; print('✓ Amenity imports OK')" 2>&1
python3 -c "from models.engine.db_storage import DBStorage; print('✓ DBStorage imports OK')" 2>&1
python3 -c "from models.engine.file_storage import FileStorage; print('✓ FileStorage imports OK')" 2>&1

echo -e "\n=== Running basic test ==="
python3 -m unittest discover tests 2>&1 | tail -n 5

