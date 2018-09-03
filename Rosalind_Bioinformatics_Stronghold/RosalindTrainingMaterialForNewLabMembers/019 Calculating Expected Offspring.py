#19. Calculating Expected Offspring
prob = {'p0':1, 'p1':1, 'p2':1, 'p3':0.75, 'p4':0.5, 'p5':0}
input_data = [19657,17291,17188,18124,19015,16884]
expect_value=2*(input_data[0] * prob['p0'] + input_data[1] * prob['p1'] + input_data[2] * prob['p2'] 
           + input_data[3] * prob['p3'] + input_data[4] * prob['p4'] + input_data[5] * prob['p5'])

print expect_value
