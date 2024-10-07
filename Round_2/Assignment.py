# Simulate database using a dictionary
collections = {}

# Create new collection
def createCollection(p_collection_name):
    collections[p_collection_name] = []
    print(f"Collection '{p_collection_name}' created.")

# Index data into collection while excluding a specified column
def indexData(p_collection_name, p_exclude_column):
    employees = [
        {'EmployeeID': 'E02001', 'Name': 'John', 'Department': 'IT', 'Gender': 'Male'},
        {'EmployeeID': 'E02002', 'Name': 'Jane', 'Department': 'HR', 'Gender': 'Female'},
        {'EmployeeID': 'E02003', 'Name': 'Doe', 'Department': 'IT', 'Gender': 'Male'}
    ]

    # Exclude specified column and index the rest
    for emp in employees:
        indexed_data = {key: value for key, value in emp.items() if key != p_exclude_column}
        collections[p_collection_name].append(indexed_data)

    print(f"Data indexed into collection '{p_collection_name}', excluding column '{p_exclude_column}'.")

# Search for records where column matches specified value
def searchByColumn(p_collection_name, p_column_name, p_column_value):
    result = [emp for emp in collections[p_collection_name] if emp.get(p_column_name) == p_column_value]
    print(f"Search result in '{p_collection_name}' for {p_column_name} = '{p_column_value}': {result}")
    return result

# Get the count of employees in collection
def getEmpCount(p_collection_name):
    count = len(collections[p_collection_name])
    print(f"Employee count in collection '{p_collection_name}': {count}")
    return count

# Delete an employee by ID
def delEmpById(p_collection_name, p_employee_id):
    collections[p_collection_name] = [emp for emp in collections[p_collection_name] if emp.get('EmployeeID') != p_employee_id]
    print(f"Employee with ID '{p_employee_id}' deleted from '{p_collection_name}'.")

# Retrieve count of employees grouped by department
def getDepFacet(p_collection_name):
    dept_count = {}
    for emp in collections[p_collection_name]:
        dept = emp.get('Department', 'Unknown')
        if dept in dept_count:
            dept_count[dept] += 1
        else:
            dept_count[dept] = 1

    print(f"Department facet for collection '{p_collection_name}': {dept_count}")
    return dept_count

# Function executions

v_nameCollection = 'Hash_Vigithra'
v_phoneCollection = 'Hash_9055'

# Creating collections
createCollection(v_nameCollection)
createCollection(v_phoneCollection)

# Get employee count
getEmpCount(v_nameCollection)

# Index data, excluding specific columns
indexData(v_nameCollection, 'Department')
indexData(v_phoneCollection, 'Gender')

# Delete employee by ID
delEmpById(v_nameCollection, 'E02003')

# Get employee count again
getEmpCount(v_nameCollection)

# Search by column
searchByColumn(v_nameCollection, 'Department', 'IT')
searchByColumn(v_nameCollection, 'Gender', 'Female')
searchByColumn(v_phoneCollection, 'Department', 'IT')

# Get department facet (group by department)
getDepFacet(v_nameCollection)
getDepFacet(v_phoneCollection)