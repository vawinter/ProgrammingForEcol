###################################X
#--- Programming for ecologists ---X
#--Program: R Homework Lesson 3----X 
#------- Author: V. Winter --------X
#-------  Created: 10/17/2022 -----X
#---- Description: ggplot ---------X 
###################################X
#------ Last edited xx/xx/2022 ----X
###################################X

# Load in data and library
data(iris)
library(ggplot2)
library(dplyr)

# 1)  Using the “iris” dataset, you will be making two different plots that visualize 
# differences between the three species of iris. You can get the iris dataset by typing: 
# 
# a) Make a scatterplot with sepal width on the x axis and sepal length on the y axis. 
# Color code each species. Add axes labels. Pick a theme. Change the font size of 
# the different elements to your liking. Make any other adjustments you want to 
# make the figure appealing to you. Include both the code and the final figure in 
# your answer. 

plot1 <- iris %>% 
  # plot iris data set with following aesthetics
  ggplot(aes(x = Sepal.Width, y = Sepal.Length, col = Species)) +
  # change point size
  geom_point(size = 3) +
  # change labels
  labs(x = "Sepal Width",
       y = "Sepa Length",
       title = "Question 1a graph", ) +
  # theme
  theme_bw() +
  # change text size and font
  theme(text=element_text(size=16,  family="serif")) +
  # center title
  theme(plot.title = element_text(hjust = 0.5)) 

# Save output
ggsave(plot1, "Homework3_question1a.pdf")

# b) Use a different type of plot to visualize some part of the iris data and edit it to 
# make it look “publication ready”. Include both the code and the final figure in 
# your answer. 

plot2 <- iris %>% 
  # plot iris data set with following aesthetics
  ggplot(aes(x = Sepal.Width, y = Sepal.Length, fill  = Species)) +
  # change point size
  geom_boxplot() +
  # change labels
  labs(x = "Sepal Width",
       y = "Sepa Length",
       title = "Question 1b graph") +
  # theme
  theme_classic() +
  # change text size and font
  theme(text=element_text(size=16,  family="sans-serif")) +
  # center title
  theme(plot.title = element_text(hjust = 0.5)) 

# Save output
ggsave(plot2, "Homework3_question1a.pdf")

# 2) (20pts) Find a figure you like in a publication or newspaper. Write out all the different 
# layers that would be required to generate it in ggplot2. Think of this as a pseudocode 
# exercise, but for graphics. 






