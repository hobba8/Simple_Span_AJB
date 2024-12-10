import csv
'''
Adam Becker
1620
12/09/2024
'''

def write_to_csv(results):
    '''
    This definition takes the simple span load results in list form and outputs them into
    a csv file that can be easily copied into a design file.

    :param results: This is a list of lists that has the simple span load results.
    :return:
    '''

    with open('simple span results.csv', 'w', newline = '') as new_file:
        writer = csv.writer(new_file)
        header = ['Distance (ft)', 'Max Shear (k)', 'Max Moment (k*ft)']
        writer.writerow(header)
        writer.writerows(results)
