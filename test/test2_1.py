def calculate_total(sales_list):
    sum = 0
    for i in sales_list:
        sum += i
    return f"Total sales is {sum}"

def calculate_conmmission(sales, rate):
    return sales * rate

def find_top_seller(sales_dict):
    top = max(sales_dict, key=sales_dict.get)
    return f"Top seller: {top} with {sum(sales_dict[top])}"

def calculate_avg_daily_sales(sales_dict):
    daily = {name: sum(sales) / len(sales) for name, sales in sales_dict.items()}
    return daily

def filter_high_perf(sales_dict, threshold):
    list_high = []
    high_perf = {name for name, sales in sales_dict.items() if sum(sales) >= threshold}
    list_high.append(high_perf)
    return list_high

sales_data = {
    "John": [1000, 1500, 2000, 1200],
    "Mary": [2000, 1800, 2200, 1900],
    "Peter": [800, 900, 100, 850]
}

print(calculate_total([1000, 1500, 2000]))
print(calculate_conmmission(500, 0.05))
print(find_top_seller(sales_data))
print(calculate_avg_daily_sales(sales_data))
print(filter_high_perf(sales_data, 6000))