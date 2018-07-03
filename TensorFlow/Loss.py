#coding=utf-8
#损失函数
#损失函数（Loss）：预测（y）与已知答案（y_）的差距
#优化目标：使loss最小    三种方式（1.均方误差  2.自定义  3.交叉熵）
#均方误差：loss_mse=tf.reduce_mean(tf.square(y_-y))
#交叉熵：表征两个概率分布之间的距离

import tensorflow as tf
import numpy as np
BATCH_SIZE=8        #单次个数（不能太大）
seed=23455          #随机数种子，相同的随机数种子，每次随机出来的数列都相同

#基于seed产生随机数
rdm=np.random.RandomState(seed)
#随机数返回32行2列的矩阵，表示32组，体积和重量，作为输入的数据集
X=rdm.rand(32,2)
#从X这个32行2列的矩阵中，取出一行，判断如果和小于1，给Y赋值1，如果和不小于1，给Y赋值0
#作为输入数据集的标签（正确的答案）
#edm.rand()/10.0-0.05           -0.05-0.05  的噪音区间
Y=[[x1+x2+(edm.rand()/10.0-0.05)] for (x1,x2) in X]
print("X:\n",X)
print("Y:\n",Y)

#定义神经网络的输入、参数和输出，定义前向传播过程
x=tf.placeholder(tf.float32,shape=(None,2))
y_=tf.placeholder(tf.float32,shape=(None,1))

w1=tf.Variable(tf.random_normal([2,1],stddev=1,seed=1))
y=tf.matmul(x,w1)

#定义损失函数及反向传播方法
#定义损失函数为MSE，反向传播方法为梯度下降
loss_mse=tf.reduce_mean(tf.square(y-y_))                                        #求平均值   （square平方）
train_step=tf.train.GradientDescentOptimizer(0.001).minimize(loss_mse)          #均方误差
#train_step=tf.train.MomentumOptimizer(0.001,0.9).minimize(loss_mse)            #梯度下降
#train_step=tf.train.AdamOptimizer(0.001).minimize(loss_mse)                    #随机梯度下降

#生成会话，训练STEPS轮
with tf.Session() as sess:
    init_op=tf.global_variables_initializer()
    sess.run(init_op)
    #输出目前（未经训练）的参数取值
    print("w1:\n",sess.run(w1))
    print("\n")

    #训练模型
    STEMP=3000
    for i in range(STEMP):
        start=(i*BATCH_SIZE)%32
        end=start+BATCH_SIZE
        sess.run(train_step ,feed_dict={x:X[start:end] ,y_:Y[start:end]})
        if i % 500 == 0:
            total_loss=sess.run(loss_mse,feed_dict={x:X,y_:Y})
            print("After %d training step(s), loss_mse on all data is %g" % (i,total_loss))

    #输出训练后的参数取值
    print("\n")
    print("w1:\n",sess.run(w1))