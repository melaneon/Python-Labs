#Melaniia Frolova
#A01391948

def get_book_info():
    '''
    Ask use to input information about the book and format it accordingly
    Take tne information and store it as a string separated by slashes

    :return: book info as a string separated with slashes
    :rtype: string
    '''
    book_title = input("Enter book name: ").title().strip()
    book_isbn = input("Enter book ISBN: ").upper().strip()
    book_author_last_name = input("Enter book author last name: ").title().strip()
    book_publisher = input("Enter book publisher: ").title().strip()
    book_year_published = int(input("Enter year when published: "))
    book_price_cad = float(input("Enter book price in CAD: "))
    book_info_seperated = "%s,%s,%s,%s,%d,%.2f"%(book_title, book_isbn, book_author_last_name, book_publisher, book_year_published, book_price_cad)
    book_info = "/".join(book_info_seperated.split(","))
    return book_info

def to_csv_format(book_info_slashed):
    '''
    format book info string from file path format to CSV

    :param book_info_slashed: book info string separated by slashes
    :type book_info_slashed: str

    :return: book info as a string separated by commas with no whitespace
    :rtype: str
    '''
    book_info_csv = ",".join(book_info_slashed.split("/"))
    print("The CSV format string:")
    print(book_info_csv)
    return book_info_csv

def to_JSON_format(book_info_csv):
    '''
    Take the book info as SCV string with no spaces and convert it to JSON

    :param book_info_csv: book info as a CSV format string
    :type book_info_csv: str

    :return: book info as a JSON formated string
    :rtype: str
    '''

    #convert string into array of strings
    book_info_csv_array = book_info_csv.split(',')

    # find needed info in the array using array index
    book_info_JSON = f'''{{
    "book_title:":"{book_info_csv_array[0]}",
    "book_isbn:":"{book_info_csv_array[1]}",
    "book_author_last_name:":"{book_info_csv_array[2]}",
    "book_publisher:":"{book_info_csv_array[3]}",
    "book_year_published:":"{str(book_info_csv_array[4])}",
    "book_price_cad:":"{str(book_info_csv_array[5])}"
}}'''
    print("The JSON format string:")
    print(book_info_JSON)
    return book_info_JSON




