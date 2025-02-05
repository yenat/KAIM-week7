import os

# Create the .dbt directory
dbt_dir = os.path.expanduser('~/.dbt')
os.makedirs(dbt_dir, exist_ok=True)

# Create the profiles.yml file
with open(os.path.join(dbt_dir, 'profiles.yml'), 'w') as file:
    file.write("""
default:
  outputs:
    dev:
      type: sqlite
      threads: 1
      database: '/home/enat/KAIM-week7/notebooks/my_database.db'
  target: dev
""")
