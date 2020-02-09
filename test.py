log = open('lr_0.001_batch_128_activation_relu_log.log')
for line in log:
    if 'Test accuracy' in line:
       acc = line.split(':')[1]

print(acc)
