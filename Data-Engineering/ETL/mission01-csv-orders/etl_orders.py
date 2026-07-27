import csv

# CSV 파일 읽기
with open("orders_raw.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    orders = list(reader)

# Transform: 최소 주문 제거
paid_orders = []

for order in orders:
    if order["status"] != "canceled":
        price = int(order["price"])
        quantity = int(order["quantity"])
        order["total_price"] = price * quantity

        paid_orders.append(order)

for order in paid_orders:
    print(order)


# Load: 정제된 데이터를 새로운 CSV 파일로 저장
fieldnames = [
    "order_id",
    "user_id",
    "product_name",
    "category",
    "total_price",
    "order_date",
]

with open("orders_clean.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames,
        extrasaction="ignore",
    )

    writer.writeheader()
    writer.writerows(paid_orders)

print("orders_clean.csv 저장 완료")