
# Validator: Function to check if value is a valid decimal
def is_valid_decimal(value):
  is_valid = False
  try:
      value_in_float = float(value)
      if value_in_float > 0:
        is_valid = True
  except ValueError:
    is_valid = False
  return is_valid

# Validator: Function to use if there is no validator required
def no_validation(value):
  return value

# Validator: Function to check if value is a valid name
def is_valid_name(value):
  is_valid = False
  if value != '' and all(lett.isalpha() or lett.isspace() for lett in value):
    is_valid = True
  return is_valid

# Validator: Function to check if value is a valid name
def is_valid_product_name(value = ''):
  is_valid = False
  if value != '' and all(lett.isalpha() or lett.isnumeric() or lett.isspace() for lett in value):
    is_valid = True
  return is_valid

# Validator: function to check valid unit
def is_valid_unit(value):
  is_valid = False
  valid_values = ['G', 'KG', 'GRAMS', 'KILOGRAMS']
  valid_values_set = set(valid_values)
  if value.upper() in valid_values_set :
    is_valid = True
  return is_valid
