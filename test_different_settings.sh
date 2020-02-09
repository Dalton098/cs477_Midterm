#!/bin/bash
for rate in 0.001
do 
    for batch_size in 32 #64 128 
    do 
        py cifar10_cnn_leaky.py \
           --learning_rate ${rate} \
           --batch_size ${batch_size} > lr_${rate}_batch_${batch_size}_activation_leaky_log.log

      #   py cifar10_cnn_softmax.py \
      #      --learning_rate ${rate} \
      #      --batch_size ${batch_size} > lr_${rate}_batch_${batch_size}_activation_softmax_log.log

      #   py cifar10_cnn_relu.py \
      #      --learning_rate ${rate} \
      #      --batch_size ${batch_size} > lr_${rate}_batch_${batch_size}_activation_relu_log.log     

<<<<<<< HEAD
        # py format_output.py \
        #    --leaky_log lr_${rate}_batch_${batch_size}_activation_leaky_log.log \
        #    --softmax_log lr_${rate}_batch_${batch_size}_activation_softmax_log.log \
        #    --relu_log lr_${rate}_batch_${batch_size}_activation_relu_log.log \
        #    --batch ${batch_size} \
        #    --lr ${rate}
=======
        python3 format_output.py \
           --relu_log lr_${rate}_batch_${batch_size}_activation_relu_log.log \
           --batch ${batch_size} \
           --lr ${rate}
>>>>>>> e24e7fbb75ad25c5333815f4ef14f710cd0802c9

    done
done
