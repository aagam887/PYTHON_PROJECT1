import pandas as pd

# Load data from Excel file
data = pd.read_excel('hotels_data.xlsx')

# Function to extract numerical cost value from range format
def extract_cost(cost):
    if isinstance(cost, str):
        cost = cost.replace(',', '')   # Remove commas
        cost = cost.strip()            # Remove leading/trailing whitespace
        
        # Split range values and take the average
        if '-' in cost:
            low, high = map(int, cost.split('-'))
            return (low + high) / 2
        else:
            return float(cost)
    else:
        return cost

# Apply function to 'Cost' column
data['Cost'] = data['Cost'].apply(extract_cost)

# Define a function to filter hotels by city and price range
def filter_hotels(city, min_price, max_price):
    filtered_hotels = data[(data['City'] == city) & (data['Cost'] >= min_price) & (data['Cost'] <= max_price)]
    if filtered_hotels.empty:
        print("No hotels found in your specified range in", city)
    else:
        print("Hotels available in", city, "within your price range:")
        print(filtered_hotels[['Hotel Name', 'City', 'Cost']].sort_values(by='Cost'))

# Display options to the user
print("Choose a state:")
states = data['State'].unique()
for state in states:
    print(state)

# Take input from the user
selected_state = input("Enter the state you want to search in: ").title()

# Validate user input and proceed accordingly
if selected_state in states:
    cities = data[data['State'] == selected_state]['City'].unique()
    print("Cities available in", selected_state, ":")
    for city in cities:
        print(city)
    
    selected_city = input("Enter the city you want to search in: ").title()
    min_price = float(input("Enter minimum price range: "))
    max_price = float(input("Enter maximum price range: "))
    
    filter_hotels(selected_city, min_price, max_price)
else:
    print("Invalid state selected.")
