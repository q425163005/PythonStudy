#coding=utf-8
import tensorflow as tf

a=tf.constant([1.0,2.0])        #两行一列
b=tf.constant([3.0,4.0])        #两行一列
result=a+b                      #相加
print(result)

#计算图（Graph）：搭建神经网络的计算过程，只搭建，不运算
x=tf.constant([[1.0,2.0]])      #输入（一行两列）
w=tf.constant([[3.0],[4.0]])    #权重（两行一列）
y=tf.matmul(x,w)                #张量运算，矩阵相乘
print(y)

#会话（Session）：执行计算图中的节点运算
with tf.Session() as sess:
    print(sess.run(y))          #1.0*3.0 + 2.0*4.0 = 11.0 