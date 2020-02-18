
1- First, just using PyCharm to install Scrapy which is a library/package could be able to scrape data from webpage. 
In PyCharm, using `pip install scrapy` to install. 
 ![](https://i.imgur.com/HtR4TWa.png)


2-Then we need to build a project by using `scrapy startproject <project name>`. In this case, I use “mece4520” as my name. 

  ![](https://i.imgur.com/fyZVV6C.png)

3-In spiders file, building a python file named “main.py” as my main file. 


![](https://i.imgur.com/OmoK5KT.png)

4-I will write my main file, and explain my code in python file. 


5-In the end, in the terminal, I will run my coding using `scrapy crawl posts`, the coding will be executed. Then in the terminal, using 
` scrapy crawl posts -o data.json`
the output data will be transferred to json file.
![](https://i.imgur.com/1JZKgQ9.png)


6-we are done. This is the data which I scraped from a blog. It contains title, date and author.

![](https://i.imgur.com/zBg4HcA.png)

