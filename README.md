<img src="https://user-images.githubusercontent.com/64495168/129553804-9baec55b-e3bf-407c-a5f5-8b229490bd27.png" alt="Rossmann logo" title="Rossmann" align="right" height="60" class="center"/>

# Rossmann stores - 6 weeks sales forecast

**Disclaimer**: this project was inspired by the "Rossmann Store Sales" challenge published on kaggle (https://www.kaggle.com/c/rossmann-store-sales). Although it is a fictitious project it will follow all steps of a real project.

## Business Issue
The sales director of the Rossmann stores wants to estimate the sales forecast for the next 6 weeks on its different units spread across Europe. So that each store manager can plan the budget with reforms (If the store has a high sales prediction) or with cost reduction (If the store has a low sales prediction)

## Solution methodology
The resolution of the challenge was carried out following the CRISP-DM (CRoss-Industry Standard Process for data mining) methodology, which is a cyclical approach that streamlines the delivery of value to the business through fast and valuable MVPs.

Benefits of Using CRISP-DM
This method is cost-effective as it includes a number of processes to take out simple data mining tasks.
CRISP-DM encourages best practices and allows projects to replicate.
This methodology provides a uniform framework for planning and managing a project.
Being cross-industry standard, CRISP-DM can be implemented in any Data Science project irrespective of its domain.

For more details about CRISP-DM metodology: https://analyticsindiamag.com/why-is-crisp-dm-gaining-grounds/


![image](https://user-images.githubusercontent.com/73034020/180753015-7945d745-3420-4fd0-9681-6487fb066c80.png)


## Data collection
The data was collected in Kaggle and all the columns attributes are explained below:

Most of the fields are self-explanatory. The following are descriptions for those that aren't.

![image](https://user-images.githubusercontent.com/73034020/180752785-0bfd3ab4-4460-4122-88e0-5a1b58b63b96.png)


For more detail about data, feel free to access the kaggle page:
https://www.kaggle.com/competitions/rossmann-store-sales/data.

## Data Understanding through mind map Hypotesis
In this section we will list some hypothesis that can be tested using this data, these hypothesis generally comes from brainstorming 
with business areas and are very important to drive our analyses.
If they are not enough to explain the stores sales we would search for more data and formulate new hypotheses

Through the mind map, we can separe our hypothesis by factors (like Stores, Products etc...) and their attributes (Store Size, Product Price, etc...)

There are some hypotesis judged to be most relevant and could drive our Exploratory Data Analysis. They are listed below.

1. Stores with larger assortments should sell more.
2. Stores with closer competitors should sell less.
3. Stores with longer competitors should sell more.
4. Stores with longer active promotions should sell more.
5. Stores with more promotion days should sell more.
6. Stores with more agressive promotion should sell more
7. Stores with more consecutive promotions should sell more.
8. Stores open on the Christmas holiday should sell more.
9. Stores should sell more over the years.
10. Stores should sell more in the second half of the year.
11. Stores should sell more after the 10th of each month.
12. Stores should sell less on weekends.
13. Stores should sell less during school holidays.

Some of them might not be tested in advance for lack of information in this DataSet. Thus it can be tested in the next CRISP-DM circle.

Below are the summary of three tested hypoteses.
1. Stores with larger assortments should sell more -- TRUE

![image](https://user-images.githubusercontent.com/73034020/180753446-e35fd0a4-9b15-44c5-80f7-3104ccbe1079.png)

![image](https://user-images.githubusercontent.com/73034020/180751961-8b4593ec-df14-441b-afd7-b97414b57818.png)

There is proportionally more sales in biggers assortments than the basic ones.

1. Stores with larger assortments should sell more -- TRUE




