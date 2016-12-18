# Indexing
# To access ith element
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December']

year = raw_input('Enter Year :')
month = raw_input('Enter Month (1-12):')
date = raw_input('Enter Date (1-31):')

# Indexing
month_name = months[int(month)-1]

print "You Entered : " + date + " " + month_name + " " + year


string_value = 'This is String Value'
print string_value[2]
