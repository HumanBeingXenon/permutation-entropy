# 排列熵 Permutation Entropy
排列熵(Permutation Entropy, PE)算法是 *Bandt, Pompe(2001)* 提出的一种度量时间序列复杂性的方法，它首先通过相空间重构以及子序列排序提取序列模式的概率分布，再根据概率分布计算出这段时间序列的熵值。

## 相空间重构
假设有一段长度为![](https://render.githubusercontent.com/render/math?math=n)的非线性系统的离散时间序列![](https://render.githubusercontent.com/render/math?math=%5C%7Bx_i%2Ci%3D1%2C2%2C%5Ccdots%2Cn%5C%7D)，我们希望从这段时间序列中提取信息，比如信号的复杂程度，这时候就需要对时间序列进行相空间重构。  
*Packard et al. (1980)* 对于时间序列的相空间重构，提出了两种重构方法，分别是导数重构法和坐标延迟重构法，这里采用的是坐标延迟法。使用坐标延迟法对相空间重构涉及到两个参数，一个是嵌入维度(Embedding Dimension) ![](https://render.githubusercontent.com/render/math?math=m)，它控制生成的列向量的维度；另一个是延迟时间(Delay Time) ![](https://render.githubusercontent.com/render/math?math=\tau)，它控制子序列的采样间隔，比如当 ![](https://render.githubusercontent.com/render/math?math=\tau)=1 时，即是连续取点；当 ![](https://render.githubusercontent.com/render/math?math=\tau)=2 时，即是间隔1个数取值。选定好参数 ![](https://render.githubusercontent.com/render/math?math=m) 和 ![](https://render.githubusercontent.com/render/math?math=\tau) 以后，可以得到一个矩阵：  
<img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;x_1&space;&&space;x_{1&plus;\tau}&space;&&space;\cdots&space;&&space;x_{1&plus;(m-1)\tau}\\&space;x_2&space;&&space;x_{2&plus;\tau}&space;&&space;\cdots&space;&&space;x_{2&plus;(m-1)\tau}\\&space;\vdots&space;&&space;\vdots&space;&&space;&\vdots\\&space;x_j&space;&&space;x_{j&plus;1}&space;&&space;\cdots&space;&&space;x_{j&plus;(m-1)\tau}\\&space;\vdots&space;&&space;\vdots&space;&&space;&&space;\vdots\\&space;x_k&space;&&space;x_{k&plus;\tau}&space;&&space;\cdots&space;&&space;x_{k&plus;(m-1)\tau}&space;\end{bmatrix}"/>  
其中![](https://render.githubusercontent.com/render/math?math=k=n-(m-1)\tau;j=1,2,\cdots,k)。

## 排列熵计算
一维序列![](https://render.githubusercontent.com/render/math?math=X_i)进行相空间重构后可以得到一个![](https://render.githubusercontent.com/render/math?math=k\times%20m)的矩阵，对矩阵行分块，分为![](https://render.githubusercontent.com/render/math?math=k)个行向量，第![](https://render.githubusercontent.com/render/math?math=i)行的向量![](https://render.githubusercontent.com/render/math?math=%5C%7Bx_i%2C%20x_%7Bi%2B%5Ctau%7D%2C%5Ccdots%2Cx_%7Bi%2B(m-1)%5Ctau%7D%5C%7D)称为<img src="https://latex.codecogs.com/gif.latex?X_i,1\le&space;i\le&space;k" />。  
在![](https://render.githubusercontent.com/render/math?math=X_i)内部进行排序，使得：  
<img src="https://latex.codecogs.com/gif.latex?x_{i&plus;(j_1-1)\tau}&space;\le&space;x_{i&plus;(j_2-1)\tau}&space;\le&space;\cdots&space;\le&space;x_{i&plus;(j_m-1)\tau}" />  
由此可得到一个序列<img src="https://latex.codecogs.com/gif.latex?\{j_1,j_2,\cdots,j_m\}" />，![](https://render.githubusercontent.com/render/math?math=j_1,j_2,\cdots,j_m)表示已好排序的新数组内的元素原本在<img src="https://latex.codecogs.com/gif.latex?X_i"/>内的索引且<img src="https://latex.codecogs.com/gif.latex?1\le&space;j_1,j_2,\cdots,j_m\le&space;m" />。【注：这个操作类似于`numpy.argsort(arr)`，将数组内的元素进行排序然后返回各个数据的索引，但是在Python里面索引范围是0\~len(arr)-1】  
1~![](https://render.githubusercontent.com/render/math?math=m)，共![](https://render.githubusercontent.com/render/math?math=m)个数，可有![](https://render.githubusercontent.com/render/math?math=m!)种排列(permutation)，将这些排列按照字典序排序，然后编号为<img src="https://latex.codecogs.com/gif.latex?\pi_1,\pi_2,\cdots,\pi_{m!}" />。统计序号向量组中![](https://render.githubusercontent.com/render/math?math=\pi_1,\pi_2,\cdots,\pi_{m!})的频数，再计算出每一个排列出现的概率![](https://render.githubusercontent.com/render/math?math=p_1,p_2,\cdots,p_{m!})。  
最后再根据香农熵(Shannon Entropy)的定义计算出排列熵：  
<img src="https://latex.codecogs.com/gif.latex?H_{pe}=-\sum_{j=1}^{k}p_j\log_2(p_j)" />  
为了方便，可以将![](https://render.githubusercontent.com/render/math?math=H_{pe})进行归一化处理，即：  
<img src="https://latex.codecogs.com/gif.latex?0&space;\le&space;\frac{H_{pe}}{\log_2(m!)}&space;\le&space;1"/>  
![](https://render.githubusercontent.com/render/math?math=H_{pe})的大小表示时间序列![](https://render.githubusercontent.com/render/math?math=X_i)的随机程度。![](https://render.githubusercontent.com/render/math?math=H_{pe})的值越小，说明时间序列越规律；反之，则时间序列越接近随机。![](https://render.githubusercontent.com/render/math?math=H_{pe})的变化反映并放大了时间序列的微小细节变化。
## 使用排列熵进行信号分析
由于心电信号的时间序列一般十分庞大，比如10秒的时间得到了2500个甚至3600个采样数据，在MIT-BIH的数据库里，有的记录时长甚至达到了24小时。因此，分析这些序列需要截短分段分析，将长度为 ![](https://render.githubusercontent.com/render/math?math=T) 的心电信号长时间序列分为若干长度为 ![](https://render.githubusercontent.com/render/math?math=%5Comega) 的子序列。这些子序列的截取相互之间可以重叠也可以不重叠。若截取片段的步长为1（也就是向后移动一位得到下一个子序列），这样可以得到的子序列个数为 ![](https://render.githubusercontent.com/render/math?math=T-%5Comega%2B1) ，然后再分别求每一段子序列的排列熵，最后将排列熵的图像画出。
### 不同类型信号的对比
下面是正常的窦性心律：
![](figures/正常2.png)
下面是心室颤动：
![](figures/心室颤动.png)
可以看到，心室颤动的排列熵曲线震荡幅度较大，排列熵值总体还有向下走的趋势。心室颤动的平均熵值比正常窦性心律要小，说明正常的心电信号的复杂程度比较高。  
下面这张图是突发的信号突变，在下面的图中可以看到突变的位置熵值有一定程度地变大。

### 不同![](https://render.githubusercontent.com/render/math?math=%5Comega)的对比
此处对![](https://render.githubusercontent.com/render/math?math=%5Comega)的取值进行研究，令![](https://render.githubusercontent.com/render/math?math=%5Comega=50,200,500)，绘制出对应的排列熵曲线，进行比较。  
下面是ω=50：
![](figures/心室颤动-50.png)
下面是ω=200：
![](figures/心室颤动.png)
下面是ω=500：
![](figures/心室颤动-500.png)
从图中可以看到，随着![](https://render.githubusercontent.com/render/math?math=%5Comega)的增大，排列熵曲线的震荡幅度逐渐收窄。
