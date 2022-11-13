import csv

def main():
    PRODUCT_NAME_INDEX = 0
    products_dict = read_dict('products.csv', PRODUCT_NAME_INDEX)
    FILENAME = 'request.csv'
    print (products_dict)
    print('Requested Items')
    
    with open (FILENAME, 'rt') as clients_request:
        reader = csv.reader(clients_request)
        next(reader)
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row in reader:
            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row) != 0:
                # Pull out Product info from request.csv
                # Assign both quantity and product code to variables
                product_code = row[0]
                requested_quantity = row[1]
                # Look up product code in products_dict
                product_info = products_dict[product_code]
                # Assign product name and price to variables
                product_name = product_info[1]
                product_price = product_info[2]
                  # Print product name and price
                print(f'{product_name}: {requested_quantity} @ {product_price}')
                   
            
def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    products_dictionary = {}
    
    #Open the file and store a reference to the opened file in a variable named products
    with open (filename, 'rt') as products:
        #Use the CSV module to create a reader
        #object that will read from the opened file
        reader = csv.reader(products)
        #The first line of the CSV file contains column headings
        #and not information about products, so this statement akips the first line of the CSV file
        next(reader)
        
        #for each product one at a time as a list
        for product in reader:
            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(product) != 0:
                key = product[key_column_index]
                #Add values (product) to the products_dictionary
                products_dictionary[key] = product
            
    return products_dictionary

# Call main to start this program.
if __name__ == "__main__":
    main()
        