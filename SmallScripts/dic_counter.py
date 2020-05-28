sample_data = [
    {'id': 1, 'success': True, 'name': 'Lary'}, 
    {'id': 2, 'success': False, 'name': 'Rabi'}, 
    {'id': 3, 'success': True, 'name': 'Alex'}
]

count = 0

for elem in sample_data:
    if elem['success'] == True:
        count += 1
print(count) 
