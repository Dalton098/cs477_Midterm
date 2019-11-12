#!/bin/bash
for rate in 0.1 0.01 0.001
do 
    for batch_size in 32 64 128 
    do 
         for func in LeakyReLU relu softmax
         do  
             py cifar10_cnn.py \
                     --learning_rate ${rate} \
                     --batch_size ${batch_size} \
                     --activation ${func} > lr_${rate}_batch_${batch_size}_activation_${func}_log.log 

             py format_output.py \
                     --log lr_${rate}_batch_${batch_size}_activation_${func}_log.log \
                     --batch ${batch_size} \
                     --lr ${rate} \
                     --func ${func} \

         done
    done
done
