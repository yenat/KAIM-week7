import os

# Create the project directory
os.makedirs('my_project/models', exist_ok=True)

# Create the dbt_project.yml file
with open('my_project/dbt_project.yml', 'w') as file:
    file.write("""
name: 'my_project'
version: '1.0'
config-version: 2

profile: 'default'

models:
  my_project:
    +enabled: true
    +materialized: 'view'
""")

# Create the my_model.sql file
with open('my_project/models/my_model.sql', 'w') as file:
    file.write("""
-- models/my_model.sql
select *
from cleaned_data
""")
