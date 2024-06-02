import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()
    
    print(users)
    

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')
    
    assert user[0][0] == 'Maydan Nezalezhnosti 1'   
    assert user[0][1] == 'Kyiv'   
    assert user[0][2] == '3127'   
    assert user[0][3] == 'Ukraine'   
    
    
@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qut_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)
    
    assert water_qnt[0][0] == 25
    
    
@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30 
    
    
    
@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'test', 'data', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)
    
    assert len(qnt) == 0
    
    
    
@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1
    
    #Check strukture of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'
       
@pytest.mark.database
def test_invalid_data_type_insertion():
    db = Database()
    with pytest.raises(Exception):
        db.insert_product_invalid(5, 123, 'солодке', 30)  # name should be a string, not a number

@pytest.mark.database
def test_string_data_handling():
    db = Database()
    db.insert_product(6, 'новий продукт', 'опис продукту', 10)
    product = db.select_product_qnt_by_id(6)
    assert product[0][0] == 10

@pytest.mark.database
def test_numeric_data_handling():
    db = Database()
    db.update_product_qut_by_id(1, 50)
    product_qnt = db.select_product_qnt_by_id(1)
    assert product_qnt[0][0] == 50

@pytest.mark.database
def test_date_time_handling():
    db = Database()
    orders = db.get_detailed_orders()
    assert isinstance(orders[0][4], str)  # Assuming order_date is stored as a string

@pytest.mark.database
def test_special_characters_handling():
    db = Database()
    db.insert_special_characters(7, "спеціальні символи", "!@#$%^&*()_+", 15)
    product = db.select_product_qnt_by_id(7)
    assert product[0][0] == 15

@pytest.mark.database
def test_large_number_handling():
    db = Database()
    db.update_product_qut_by_id(1, 1000000)
    product_qnt = db.select_product_qnt_by_id(1)
    assert product_qnt[0][0] == 1000000

@pytest.mark.database
def test_null_values_handling():
    db = Database()
    with pytest.raises(Exception):
        db.insert_product_with_null(8, None, 'опис продукту', 20)
