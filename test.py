def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    
    return total
    
def test_calculate_total_with_empy_list():
    #assert verifica que la condicion planteada sea True
    print("se ejecuta funcion: test_calculate_total_with_empy_list")
    assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
    products = [
        {
            "name": "Notebook", 
            "price": 5
        }
    ]
    print(calculate_total(products))
    assert calculate_total(products) == 5
    
def test_calculate_total_with_multiple_product():
    products = [
        {
            "name": "Notebook", 
            "price": 10
        },
        {
           "name": "Pen", 
            "price": 2
        }
        
    ]
    print(calculate_total(products))
    assert calculate_total(products) == 12
    
if __name__ == "__main__":
    test_calculate_total_with_empy_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()