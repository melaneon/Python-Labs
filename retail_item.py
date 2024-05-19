# Melaniia Frolova
# A01391948

#get the item description
def get_retail_item_description():
    """

    :return: Description of retail item
    :rtype: str
    """
    item_description = input("Enter retail item description: ")
    return item_description

#get the number of purchased items
def get_number_of_purchased_items():
    """

    :return: Number of purchased items
    :rtype: int
    """
    number_of_purchased_items = int(input("Enter quantity purchased: "))
    return number_of_purchased_items

#get the item price in CAD
def get_price_per_unit_cad():
    """

    :return: Price per unit cad
    :rtype: float
    """
    price_per_unit_cad = float(input("Enter price per unit in CAD: "))
    return price_per_unit_cad

#get the float tax rate
def get_tax_rate():
    """

    :return: Tax rate
    :rtype: float
    """
    tax_rate = float(input("Enter the decimal tax rate like (where 1% is 0.01) : "))
    return tax_rate

#get the subtotal in CAD (total before tax)
def calculate_subtotal_cad(price_in_cad, quantity_sold):
    """

    :param price_in_cad: Price per unit cad
    :type price_in_cad: float
    :param quantity_sold: Quantity of items sold
    :type quantity_sold: int
    :return: Subtotal cad
    :rtype: float
    """
    subtotal_cad = price_in_cad * quantity_sold
    return subtotal_cad

#get the tax amount based on the subtotal and tax rate given
def calculate_tax_cad(subtotal_cad, tax_rate):
    """

    :param subtotal_cad: Subtotal in CAD
    :type subtotal_cad: float
    :param tax_rate: Tax rate
    :type tax_rate: float
    :return: Tax amount in CAD
    :rtype: float
    """
    tax_cad = subtotal_cad * tax_rate
    return tax_cad

#get the total in CAD (after tax)
def calculate_total_cad(subtotal_cad, tax_cad):
    """

    :param subtotal_cad: Subtotal in CAD
    :type subtotal_cad: float
    :param tax_cad: Tax amount in CAD
    :type tax_cad: float
    :return: Total cad after tax
    :rtype: float
    """
    total_cad = subtotal_cad + tax_cad
    return total_cad




def main():
    #Call all defining functions and assign returned values to internal values
    item_description = get_retail_item_description()
    number_of_purchased_items = get_number_of_purchased_items()
    price_per_unit_cad = get_price_per_unit_cad()
    tax_rate = get_tax_rate()

    #Call all calculating functions and assign returned values to internal values
    subtotal_cad = calculate_subtotal_cad(price_per_unit_cad, number_of_purchased_items)
    tax_cad = calculate_tax_cad(subtotal_cad, tax_rate)
    total_cad = calculate_total_cad(subtotal_cad, tax_cad)

    #RECEIPT PRINT
    print(" ") #line separator
    print("SALES RECEIPT:")
    print("Item Description:", item_description)
    print("Number of Purchased Items:", number_of_purchased_items)
    print("Unit Price:", price_per_unit_cad)
    print("Tax Rate:", tax_rate)
    print("Subtotal:", subtotal_cad)
    print("Tax:", tax_cad)
    print("Total:", total_cad)

if __name__ == '__main__':
    main()

