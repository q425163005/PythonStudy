#coding=utf-8
#两层简单神经网络（全连接）
import tensorflow as tf

#定义输入和参数
x=tf.constant([[0.7,0.5]])
w1=tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2=tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

#定义前向传播过程
a=tf.matmul(x,w1)
y=tf.matmul(a,w2)

#用会话计算结果
#变量初始化、计算图节点运算都要用会话（with结构）实现
with tf.Session() as sess:
    #变量初始化：在sess.run函数中用tf.global_variables_initializer()
    init_op=tf.global_variables_initializer()
    sess.run(init_op)
    #计算图节点运算：在sess.run函数中写入待运算的节点
    #sess.run(y)
    print("y in ForwardPropagation.py is:\n",sess.run(y))

'''
y in ForwardPropagation.py is:
[[3.0904665]]
'''