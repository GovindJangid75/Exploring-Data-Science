# Yeh function hai fetch_sales jo sales data ko fetch karta hai
def fetch_sales():
    print("Fetching the sales data")

# Yeh function hai filter_valid_sales jo valid sales data ko filter karta hai
def filter_valid_sales():
    print("Filtering valid sales data")

# Yeh function hai summarize_data jo sales data ka summary banata hai
def summarize_data():
    print("Summarizing sales data")

# Yeh function hai generate_report jo upar wale functions ko call karta hai aur report generate karta hai
def generate_report():
    fetch_sales()            # Sales data fetch karta hai
    filter_valid_sales()     # Valid sales ko filter karta hai
    summarize_data()         # Data ko summarize karta hai
    print("Report is ready") # Report ready hone ka message print karta hai

# Function ko call kar rahe hain jisse pura process chalega
generate_report()
# Yeh function hai calculate_total jo total sales ko calculate karta hai