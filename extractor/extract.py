# -*- coding: utf-8 -*-

'''
预处理：将网页解析成DOM树，并剔除不可视节点.
'''
def preprocess():
    pass

'''
获取待提取文本块：根据网页DOM树计算各个块的文本密度，并将文本密度大于<body>块的文本块的上一级文本块作为待提取块.
设T为网页解析树，Tbv是T上以节点v为根节点的子树，其中v为非文本节点，若Tbv不为空，则称Tbv为一个文本块. 
同时，设定v的文本块密度(Text block density, TBD)TBDv为节点v所有子节点为根的文本块中非链接文本字符总数
与块内非链接标签总数的比值，公式为
￼TBDv=Cv+1/Tv+1
'''
def text_density():
    pass

'''
根据标签路径相同的节点多同为正文或同为噪音的特征，设p为网页解析树T的一个标签路径，定义文本标签路径比
(Text to tag path ratio, TPR)TPRp等于路径为p的文本节点的字符之和与节点个数的比值. 同时设定标点
标签路径比(Punctuation to tag path ratio, PPR)PPR等于路径为p的文本节点的标点之和与节点个数的比值.
，文本长度和标点个数均能在一定程度上区分正文节点和噪音节点.
定义融合特征TPF. 其计算公式为
￼TPFp=TPRp×PPRp
'''
def text_tpr():
    pass


'''
文本标签距离： 文本节点距离根结点（body）的节点距离值， 值越小，为网页内容的概率越大
'''
def text_pdr():
    pass