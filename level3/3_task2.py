import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def data_viz_tool(df):
    sns.set_theme(style="whitegrid")

    fig,axes=plt.subplots(2,2,figsize=(15,10))
    fig.suptitle('Data Visualization Dashboard',fontsize=20)

    sns.histplot(df.iloc[:,0],kde=True,ax=axes[0,0],color='skyblue')
    axes[0,0].set_title('Feature Distribution (Histogram)')
    
    numeric_df=df.select_dtypes(include=['float64','int64'])
    
    sns.boxplot(data=numeric_df,ax=axes[0,1],palette='Set2')
    axes[0,1].set_title('Data Spread & Outliers (Box Plot)')

    sns.scatterplot(x=df.iloc[:,0],y=df.iloc[:,1],hue=df.iloc[:,-1],ax=axes[1,0])
    axes[1,0].set_title('Feature Correlation (Scatter)')

    sns.heatmap(numeric_df.corr(),annot=True,cmap='coolwarm',ax=axes[1,1])
    axes[1,1].set_title('Correlation Heatmap')

    plt.tight_layout(rect=[0,0.03,1,0.95])
    plt.show()

dataset=sns.load_dataset('iris')
data_viz_tool(dataset)