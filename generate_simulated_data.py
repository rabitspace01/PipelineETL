from faker import Faker
import csv




#Simulado de ventas
def generate_sales_data(num_entries=100):
    fake = Faker()
    sales_data = []


    for _ in range(num_entries): 
        sale = {
            "date": fake.date_between(start_date="-1y", end_date="today"),
            "product": fake.random_element(elements=("Product A", "Product B", "Product C")),
            "quantity": fake.random_int(min=1, max=100),
            "revenue": fake.random_int(min=50, max=1000)
        }
        sales_data.append(sale)

    return sales_data

#Simulado de marketing
def generate_marketing_data(num_entries=100): 
    fake = Faker()
    marketing_data = []

    for _ in range(num_entries):
        campaign = {
            "date": fake.date_between(start_date="-1y", end_date="today"),
            "campaign_name": fake.word(),
            "clicks": fake.random_int(min=10, max=1000),
            "conversions": fake.random_int(min=1, max=100)
        }
        marketing_data.append(campaign)

    return marketing_data


simulated_sales = generate_sales_data()
simulated_marketing = generate_marketing_data()

print("Simulated Sales Data:")
print(simulated_sales)

print("\nSimulated Marketing Data:")
print(simulated_marketing)

def save_data_to_csv(data, filename):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

save_data_to_csv(simulated_sales, "sales_data.csv")
save_data_to_csv(simulated_marketing, "marketing_data.csv")



