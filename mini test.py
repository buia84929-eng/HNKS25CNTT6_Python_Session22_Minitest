inventory = [
    {'id': 'G01', 'name': 'Gạo tẻ', 'quantity': 50},
    {'id': 'G02', 'name': 'Mì tôm', 'quantity': 120}
]

def show_inventory(inventory_list):
    if len(inventory_list) == 0:
        print("Kho hàng hiện đang trống!")
        return
    print(f"{'ID':<5} | {'Tên hàng hóa':<20} | {'Số lượng tồn':<15}")
    print("-----------------------------------------------------")
    for item in inventory_list:
        print(f"{item['id']:<5} | {item['name']:<20} | {item['quantity']:<15}")
    print("-----------------------------------------------------")

def add_item(inventory_list):
    item_id = input("Nhập mã hàng hóa (ID): ")
    item_name = input("Nhập tên hàng hóa: ").strip()
    quantity = int(input("Nhập số lượng tồn kho: "))

    new_item = {
        'id': item_id,
        'name': item_name,
        'quantity': quantity
    }
    inventory_list.append(new_item)
    print("Thêm hàng hóa vào kho thành công!")

def update_quantity(inventory_list):
    print("--- CẬP NHẬT SỐ LƯỢNG TỒN KHO ---")
    item_id = input("Nhập mã hàng hóa cần sửa: ")
    
    for item in inventory_list:
        if item['id'] == item_id:
            print(f'Tìm thấy hàng hóa: {item['name']} (Số lượng hiện tại: {item['quantity']})')
            inventory_list['quantity'] = input("Nhập số lượng mới: ")
            print("Cập nhật số lượng thành công!")
            return
        print(f'Không tìm thấy hàng hóa có mã [{item_id}]!')
            
    
while True:
    print('''
---- NHẬP HÀNG HÓA MỚI ----
1. Xem danh sách hàng tồn kho
2. Nhập thêm hàng hóa mới 
3. Cập nhật số lượng tồn kho 
4. Thoát chương trình
''')
    choice = int(input('Mời bạn chọn chức năng (1-4): '))
    match choice:
        case 1:
            show_inventory(inventory)
        case 2:
            add_item(inventory)
        case 3:
            update_quantity(inventory)
        case 4:
            print('''Cảm ơn bạn đã sử dụng phần mềm! 
[Chương trình kết thúc]''')
            break
        case _:
            print("Lỗi vui lòng nhập lại lựa chọn của bạn")