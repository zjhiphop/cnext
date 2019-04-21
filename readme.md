Content Extractor
================

> A text based extractor based on modern tech such as Machine Learning.

Road Map
========
1. Web content Extractor
2. Email content Extractor
3. IM content Extractor

TODO
====
1. Chinese content extractor
>
    (1) 预处理：将网页解析成DOM树，并剔除不可视节点.
    (2) 获取待提取文本块：根据网页DOM树计算各个块的文本密度，并将文本密度大于<body>块的文本块的上一级文本块作为待提取块.
    (3) 获取标签路径集合：计算每条标签路径的TPR值，设定阈值，获取正文节点候选的路径集合.
    (4) 提取正文：将 (3) 的候选路径集合与 (2) 获取的文本块中的路径集合求交集，将交集中路径节点的文本提取，输出为网页正文.