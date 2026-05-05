# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
# Example: services = {"Web Development": 150, "Data Analysis": 175, ...}
# Include at least 5 different services
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cybersecurity": 220,
    "Cloud Consulting": 200,
    "Technical Support": 95
}

# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
# Create at least 4 customer dictionaries
# Example: customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", ...}
customer1 = {
    "company_name": "Bright Future Inc",
    "contact_person": "Alice Johnson",
    "email": "alice@brightfuture.com",
    "phone": "555-1001"
}

customer2 = {
    "company_name": "Summit Retail",
    "contact_person": "Brian Smith",
    "email": "brian@summitretail.com",
    "phone": "555-1002"
}

customer3 = {
    "company_name": "Nova Health",
    "contact_person": "Carla Gomez",
    "email": "carla@novahealth.com",
    "phone": "555-1003"
}

customer4 = {
    "company_name": "Green Energy Co",
    "contact_person": "David Lee",
    "email": "david@greenenergy.com",
    "phone": "555-1004"
}

# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
# Example: customers = {"C001": customer1, "C002": customer2, ...}
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
# Add your code here to display all customer information
for customer_id, info in customers.items():
    print(f"{customer_id}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print()

# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)

print("\n\nCustomer Lookups:")
print("-" * 60)
# Add your code here
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("C002 info:", c002_info)
print("C003 contact person:", c003_contact)
print("C999 lookup:", c999_info)

# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information

print("\n\nUpdating Customer Information:")
print("-" * 60)
# Add your code here
customers["C001"]["phone"] = "555-7777"
customers["C002"]["industry"] = "Retail"

print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])

# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}

project1 = {"name": "Website Redesign", "service": "Web Development", "hours": 120, "budget": 18000}
project2 = {"name": "Sales Dashboard", "service": "Data Analysis", "hours": 80, "budget": 14000}
project3 = {"name": "Security Audit", "service": "Cybersecurity", "hours": 60, "budget": 13200}
project4 = {"name": "Cloud Migration", "service": "Cloud Consulting", "hours": 90, "budget": 18000}
project5 = {"name": "Help Desk Setup", "service": "Technical Support", "hours": 50, "budget": 4750}
project6 = {"name": "Patient Data Review", "service": "Data Analysis", "hours": 70, "budget": 12250}

projects = {
    "C001": [project1, project2],
    "C002": [project3],
    "C003": [project4, project6],
    "C004": [project5]
}

print("\n\nProject Information:")
print("-" * 60)
# Add your code here
for customer_id, project_list in projects.items():
    print(f"{customer_id}:")
    for project in project_list:
        print(f"  {project}")
    print()

# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)
# Add your code here
for customer_id, project_list in projects.items():
    print(f"{customer_id}:")
    for project in project_list:
        hourly_rate = services[project["service"]]
        cost = hourly_rate * project["hours"]
        print(f"  {project['name']} - Service: {project['service']}, Hours: {project['hours']}, Calculated Cost: ${cost}")
    print()

# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()

print("\n\nCustomer Statistics:")
print("-" * 60)
# Add your code here
print("Customer IDs:", list(customers.keys()))

company_names = [customer["company_name"] for customer in customers.values()]
print("Customer Companies:", company_names)

print("Total Customers:", len(customers))

# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts

print("\n\nService Usage Analysis:")
print("-" * 60)
# Add your code here
service_counts = {}

for project_list in projects.values():
    for project in project_list:
        service = project["service"]
        if service in service_counts:
            service_counts[service] += 1
        else:
            service_counts[service] = 1

print("Service Counts:", service_counts)

# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)

print("\n\nFinancial Summary:")
print("-" * 60)
# Add your code here
all_projects = []
for project_list in projects.values():
    for project in project_list:
        all_projects.append(project)

total_hours = sum(project["hours"] for project in all_projects)
total_budget = sum(project["budget"] for project in all_projects)
avg_budget = total_budget / len(all_projects)
max_budget = max(project["budget"] for project in all_projects)
min_budget = min(project["budget"] for project in all_projects)

most_expensive_project = max(all_projects, key=lambda project: project["budget"])
least_expensive_project = min(all_projects, key=lambda project: project["budget"])

print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Project Budget:", avg_budget)
print("Highest Budget:", max_budget, "-", most_expensive_project["name"])
print("Lowest Budget:", min_budget, "-", least_expensive_project["name"])

# TODO 12: Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget

print("\n\nCustomer Summary Report:")
print("-" * 60)
# Add your code here
for customer_id, info in customers.items():
    customer_projects = projects.get(customer_id, [])
    customer_total_hours = sum(project["hours"] for project in customer_projects)
    customer_total_budget = sum(project["budget"] for project in customer_projects)

    print(f"{customer_id} - {info['company_name']}")
    print(f"  Contact Person: {info['contact_person']}")
    print(f"  Email: {info['email']}")
    print(f"  Phone: {info['phone']}")
    print(f"  Number of Projects: {len(customer_projects)}")
    print(f"  Total Hours: {customer_total_hours}")
    print(f"  Total Budget: ${customer_total_budget}")
    print()

# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
# Add your code here
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}
print(adjusted_rates)

# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects

print("\n\nActive Customers (with projects):")
print("-" * 60)
# Add your code here
active_customers = {customer_id: info for customer_id, info in customers.items() if customer_id in projects and len(projects[customer_id]) > 0}
print(active_customers)

# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
# Add your code here
customer_budgets = {customer_id: sum(project["budget"] for project in project_list) for customer_id, project_list in projects.items()}
print(customer_budgets)

# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension

print("\n\nService Pricing Tiers:")
print("-" * 60)
# Add your code here
service_tiers = {
    service: "Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic"
    for service, rate in services.items()
}
print(service_tiers)

# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results

print("\n\nCustomer Validation:")
print("-" * 60)
# Add your code here
def validate_customer(customer_dict):
    required_fields = ["company_name", "contact_person", "email", "phone"]
    for field in required_fields:
        if field not in customer_dict:
            return False
    return True

for customer_id, info in customers.items():
    print(f"{customer_id}: {validate_customer(info)}")

# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses

print("\n\nProject Status Summary:")
print("-" * 60)
# Add your code here
status_list = ["active", "completed", "pending"]
status_index = 0

for project_list in projects.values():
    for project in project_list:
        project["status"] = status_list[status_index % len(status_list)]
        status_index += 1

status_counts = {}

for project_list in projects.values():
    for project in project_list:
        status = project["status"]
        if status in status_counts:
            status_counts[status] += 1
        else:
            status_counts[status] = 1

print("Status Counts:", status_counts)

# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
# Add your code here
def analyze_customer_budgets(projects_dict):
    results = {}

    for customer_id, project_list in projects_dict.items():
        total = 0
        count = 0

        for project in project_list:
            total += project["budget"]
            count += 1

        average = total / count if count > 0 else 0

        results[customer_id] = {
            "total": total,
            "average": average,
            "count": count
        }

    return results

budget_analysis = analyze_customer_budgets(projects)
print(budget_analysis)

# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations

print("\n\nService Recommendations:")
print("-" * 60)
# Add your code here
def recommend_services(customer_id, customers, projects, services):
    if customer_id not in customers:
        return ["Customer not found"]

    customer_projects = projects.get(customer_id, [])
    used_services = []

    for project in customer_projects:
        used_services.append(project["service"])

    if len(customer_projects) > 0:
        average_budget = sum(project["budget"] for project in customer_projects) / len(customer_projects)
    else:
        average_budget = 0

    recommendations = []

    for service, rate in services.items():
        if service not in used_services:
            estimated_cost = rate * 50  # estimated 50-hour project
            if average_budget == 0 or estimated_cost <= average_budget * 1.2:
                recommendations.append(service)

    return recommendations

for customer_id in customers.keys():
    print(f"{customer_id}: {recommend_services(customer_id, customers, projects, services)}")