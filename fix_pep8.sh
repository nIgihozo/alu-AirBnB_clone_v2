#!/bin/bash

echo "Fixing PEP8 issues..."

# Fix bare except in test_base_model.py
sed -i 's/^        except:$/        except Exception:/' tests/test_models/test_base_model.py

# Fix bare except in test_file_storage.py
sed -i 's/^        except:$/        except Exception:/' tests/test_models/test_engine/test_file_storage.py

echo "Manual fixes needed for test_db_storage.py long lines"
echo "Opening file for editing..."

