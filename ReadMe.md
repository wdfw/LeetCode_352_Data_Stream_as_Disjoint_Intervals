# 題目
![image](https://user-images.githubusercontent.com/111077328/215264556-82487c4e-789d-4360-8815-0d660c65bf65.png)
# 例子
![image](https://user-images.githubusercontent.com/111077328/215264566-a7ca6bf1-4a63-44db-812f-836717ea89b4.png)
![image](https://user-images.githubusercontent.com/111077328/215264572-7210760d-c28e-41c6-b6f7-1ec0d72f4b94.png)  
# 思路
這題要找數字間的區間，每次輸入一個數字，當數字不連續時，形成一個區段，而當數字連續時，將兩個區段合併。因為一次只會輸入一個數字，所以在合併上只考慮有value+1跟value-1衍生的四種情況:  
1. value-1 存在 -- 新的value成為randes的最左端
2. value+1 存在 -- 新的value成為randes的最右端
3. value-1 跟 value+1 都存在 -- value-1 跟 value+1 合併
4. value-1 跟 value+1 都不存在 -- 新的value自己成為一個區段

此時題目分成2個小問題
1. 如何找出value前後是否有值
2. 如何將區段合併

所以先解決問題1，我透過union find的方式將新加入的值存入字典中，將value的值指向區段中最小的數，同時映對一個ranges，而ranges的key就代表ranges這個區
段的最小值，因此每次新加入value時，只需檢查head裡面是否存在value，value+1，value-1並進行剛剛的判斷  
![image](https://user-images.githubusercontent.com/111077328/215266127-87a85c4c-c96d-42e2-9a42-cc41119f6412.png)  
接著解決問題2，當case4發生時則ranges創建一個新的區段，對應的key是value  
當case1發生時，ranges[value-1] 的最大值更新為value，同時將head[value]指向value-1的頭(最小值)  
當case2發生時，ranges[value+1] 的最小值更新為value，同時將head[value+1]指向value(因為value為此區段的最小值)
當case3發生時，ranges[value-1]的尾更新為ranges[value+1]的尾，並刪掉ranges[value+1]，同時將head[value+1]指向value-1的頭  
這樣就可以完成區段更新的部分
