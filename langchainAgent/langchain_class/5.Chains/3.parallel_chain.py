from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1 = PromptTemplate(template="Generate short and simple notes for the following {topic}",
                         input_variables=['topic'])


prompt2 = PromptTemplate(template="Generate 5 short and question answer  for the following {text}",
                         input_variables=['text'])

prompt3 = PromptTemplate(template="merge the provided notes and quiz into a single document \n notes : {notes}, quiz: {quiz}")

parser = StrOutputParser()

runnable_chain = RunnableParallel(
    {
        "notes" : prompt1 | model | parser ,
        "quiz": prompt2 | model | parser
    }
)

final_chain = prompt3 | model | parser 

chains = runnable_chain | final_chain 

text = """
Support Vector Machine (SVM) is a supervised machine learning algorithm used for both classification and regression tasks, although it is mainly popular for classification problems. The main idea behind SVM is to find the optimal boundary (called a hyperplane) that separates data points of different classes as clearly as possible.

In a two-dimensional space, this hyperplane is simply a line dividing the data into two categories. In higher dimensions, it becomes a plane or hyperplane. The best hyperplane is the one that maximizes the margin, which is the distance between the hyperplane and the nearest data points from each class.

The data points that lie closest to the decision boundary are called support vectors. These points are crucial because they directly influence the position and orientation of the hyperplane. If these points move, the hyperplane will also change.

SVM can handle both linear and non-linear classification. For linearly separable data, a straight line (or hyperplane) is sufficient. However, for non-linear data, SVM uses a technique called the kernel trick. Kernels transform the original data into a higher-dimensional space where it becomes easier to separate using a linear boundary. Common kernels include the linear kernel, polynomial kernel, and radial basis function (RBF) kernel.

SVM is known for its effectiveness in high-dimensional spaces and its ability to work well even when the number of features is larger than the number of samples. It is also memory efficient because it uses only a subset of training points (support vectors).

However, SVM has some limitations. It can be less efficient on very large datasets and may require careful tuning of parameters such as the regularization parameter (C) and kernel parameters. Additionally, it is not very suitable for datasets with a lot of noise or overlapping classes.

Overall, SVM is a powerful and versatile algorithm widely used in applications such as image classification, text categorization, and bioinformatics.

"""

result = chains.invoke(text)
print(result)
