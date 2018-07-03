#coding=utf-8
#两层简单神经网络（全连接）
import tensorflow as tf

#定义输入和参数
#用placeholder实现输入定义 （sess.run喂入多组数据）
x=tf.placeholder(tf.float32,shape=(None,2))
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
    print("y in ForwardPropagation3.py is:\n",sess.run(y,feed_dict={x:[[0.7,0.5],[0.2,0.3],[0.3,0.4],[0.4,0.5]]}))       #喂入多组数据
    print("w1:\n",sess.run(w1))
    print("w2:\n",sess.run(w2))

'''
y in ForwardPropagation3.py is:
[[3.0904665]
 [1.2236414]
 [1.7270732]
 [2.2305048]]
w1:
[[-0.8113182   1.4845988   0.06532937]
 [-2.4427042   0.0992484   0.5912243 ]]
w2:
[[-0.8113182 ]
 [ 1.4845988 ]
 [ 0.06532937]]

'''